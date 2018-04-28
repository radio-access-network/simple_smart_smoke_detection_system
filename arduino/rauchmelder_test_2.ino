#include <OneWire.h>
#include <DallasTemperature.h>
#include <SPI.h>
#include <Ethernet.h>

const int smoke_detector_pin = A0;
const int dallas_pin = 9;
const long bauds = 115200;

byte mac[] = {0xDE, 0xAD, 0xBE, 0x00, 0x00, 0x02};

OneWire oneWire(dallas_pin);

DallasTemperature dallas_sensor(&oneWire);

EthernetServer server(80);

bool first_alarm = false;

void setup(void)
{
  // start serial port
  Serial.begin(bauds);
  Serial.println("Starte!");
  
  pinMode(smoke_detector_pin, INPUT);
  dallas_sensor.begin();

  delay(2000);

  if (Ethernet.begin(mac) == 0) {
    Serial.println("DHCP-Server weist keine IP zu!");
    while (true) {}
  }
  server.begin();
  Serial.println("Verbunden via: " + Ethernet.localIP());
}

void loop(void)
{
  String response = "";
  dallas_sensor.requestTemperatures();
  long is_alarm = analogRead(smoke_detector_pin);
  if (is_alarm > 100) {
    response = "alarm";
    first_alarm = true;
  }
  else {
    if (first_alarm == false) {
      response = "ok";
    }
  }

  double tmp_temp = dallas_sensor.getTempCByIndex(0);
  Serial.println("Status: " + response + ", Temperatur: " + String(tmp_temp, 2));

  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          // send a standard http response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
          //client.println("Refresh: 5");  // refresh the page automatically every 5 sec
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");

          client.print("Rauchmelder_Status: ");
          client.print(response);
          client.print("Temperatur: ");
          client.print(tmp_temp);
          client.println(" <br/>");

          client.println("</html>");
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
    Serial.println("client disconnected");
  }
}
