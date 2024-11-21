int exteriorldrPin = 13;
int lowLED = 16;
int medLED = 17;
int highLED = 18;
int maxLED = 19;
int interiorlowLED = 23;
int interiormedLED = 22;
int interiorhighLED = 21;
int interiormaxLED = 5;
int trigPin = 2;
int echoPin = 15;
int interiorLED = 4;
int potencPin = 26;
int pwm = 0;
int valorpot= 0;
int interiorldrPin = 25;
int botaoPin = 34;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(lowLED, OUTPUT);
  pinMode(medLED, OUTPUT);
  pinMode(highLED, OUTPUT);
  pinMode(maxLED, OUTPUT);
  pinMode(interiorlowLED, OUTPUT);
  pinMode(interiormedLED, OUTPUT);
  pinMode(interiorhighLED, OUTPUT);
  pinMode(interiormaxLED, OUTPUT);
  pinMode(interiorLED, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(potencPin, INPUT);
  pinMode(botaoPin, INPUT_PULLUP);
}



void loop() {

  int botaoState = HIGH;
  botaoState = digitalRead(botaoPin);
  // ativando o sonar
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(2);
  digitalWrite(trigPin, LOW);

  // calculando a distancia
  long duration = pulseIn(echoPin,HIGH);
  int distance = duration * 0.034/2;

  int interiorLDR = analogRead(interiorldrPin);
  int exteriorLDR = analogRead(exteriorldrPin);


  
  // caso o sonar detecte movimento o led sinalizando as luzes internas irá acender
  if(distance < 100){
    Serial.println("Detectou movimento");
    //o potenciometro aumenta ou diminui a intensidade das luzes internas
    if(botaoState == LOW){
      Serial.println("Controle manual do Dimming ativado!");
      valorpot = analogRead(potencPin);//Efetua a leitura do pino analógico A5 
      pwm = map(valorpot, 0, 1023, 0, 255);//Função map() para converter a escala de 0 a 1023 para a escala de 0 a 255
      //Serial.println(pwm);//Imprime valorpot na serial
      analogWrite(interiorLED, pwm);//Aciona o LED proporcionalmente à leitura analógica
      }else{
        Serial.println("Controle manual do Dimming desativado!");
        if(interiorLDR > 1000){
          digitalWrite(interiorlowLED, HIGH);
          digitalWrite(interiormedLED, HIGH);
          digitalWrite(interiorhighLED, HIGH);
          digitalWrite(interiormaxLED, HIGH);
        } else if(interiorLDR > 700 && interiorLDR < 999 ){
          digitalWrite(interiorlowLED, HIGH);
          digitalWrite(interiormedLED, HIGH);
          digitalWrite(interiorhighLED, HIGH);
          digitalWrite(interiormaxLED, LOW);
        } else if (interiorLDR > 400 && interiorLDR < 699){
          digitalWrite(interiorlowLED, HIGH);
          digitalWrite(interiormedLED, HIGH);
          digitalWrite(interiorhighLED, LOW);
          digitalWrite(interiormaxLED, LOW);
        } else if(interiorLDR > 150 && interiorLDR < 399) {
          digitalWrite(interiorlowLED, HIGH);
          digitalWrite(interiormedLED, LOW);
          digitalWrite(interiorhighLED, LOW);
          digitalWrite(interiormaxLED, LOW);
        } else{
          digitalWrite(interiorlowLED, LOW);
          digitalWrite(interiormedLED, LOW);
          digitalWrite(interiorhighLED, LOW);
          digitalWrite(interiormaxLED, LOW);
        }
      }
    }else{
      Serial.println("Não detectou movimento");
      digitalWrite(interiorLED, LOW);
      digitalWrite(interiorlowLED, LOW);
      digitalWrite(interiormedLED, LOW);
      digitalWrite(interiorhighLED, LOW);
      digitalWrite(interiormaxLED, LOW);
    }

  // os quatro led sinalizam a intensidade das luzes externas, um led representa baixa itensidade, dois media intensidade
  // tres alta intensidade e quatro intensidade maxima 
  // aqui acende os led de acordo com o valor do lux
  
  if(exteriorLDR > 1000){
    digitalWrite(lowLED, HIGH);
    digitalWrite(medLED, HIGH);
    digitalWrite(highLED, HIGH);
    digitalWrite(maxLED, HIGH);
  } else if(exteriorLDR > 700 && exteriorLDR < 999 ){
    digitalWrite(lowLED, HIGH);
    digitalWrite(medLED, HIGH);
    digitalWrite(highLED, HIGH);
    digitalWrite(maxLED, LOW);
  } else if (exteriorLDR > 400 && exteriorLDR < 699){
    digitalWrite(lowLED, HIGH);
    digitalWrite(medLED, HIGH);
    digitalWrite(highLED, LOW);
    digitalWrite(maxLED, LOW);
  } else if(exteriorLDR > 150 && exteriorLDR < 399) {
    digitalWrite(lowLED, HIGH);
    digitalWrite(medLED, LOW);
    digitalWrite(highLED, LOW);
    digitalWrite(maxLED, LOW);
  } else{
    digitalWrite(lowLED, LOW);
    digitalWrite(medLED, LOW);
    digitalWrite(highLED, LOW);
    digitalWrite(maxLED, LOW);
  }
  
  Serial.println("--------");
  delay(500); // this speeds up the simulation
}

/*
0 lux: Noite sem luz.
10 a 100 lux: Amanhecer e lugares com luz fraca (ex. salas com pouca luz natural).
100 a 1.000 lux: Manhã (luz solar média), ambientes internos com boa iluminação.
10.000 a 100.000 lux: Meio-dia, luz solar direta.
1.000 a 10.000 lux: Tarde com céu claro.
100 a 1.000 lux: Final de tarde, luz decrescente.
*/
