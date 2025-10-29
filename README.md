# 🎛️ Raspberry Pi Pico W – Analog LED Brightness Control (ADC + PWM)

This project demonstrates how to control an LED’s brightness **proportionally** to the position of a **potentiometer** using **ADC (Analog-to-Digital Converter)** and **PWM (Pulse Width Modulation)** on the **Raspberry Pi Pico W**.

---

## ⚙️ Working Principle
- The **potentiometer** acts as an adjustable voltage divider.
- The **ADC** reads this voltage as a value between **0 and 65535**.
- The **PWM** output adjusts the LED brightness based on this ADC value.

Essentially, turning the potentiometer changes the voltage → changes the ADC value → updates the LED brightness instantly.

---

## 🧩 Components Required

| Component | Quantity | Description |
|------------|-----------|-------------|
| Raspberry Pi Pico W | 1 | Microcontroller board |
| LED | 1 | Any color |
| Potentiometer | 1 | 10kΩ recommended |
| 220Ω Resistor | 1 | Current limiting for LED |
| Breadboard & Jumper Wires | — | For easy connections |

---

## 🧠 Circuit Connections

| Component | Pico W Pin | Description |
|------------|-------------|-------------|
| LED Anode (+) | GPIO17 | PWM Output |
| LED Cathode (–) | GND | Ground |
| Potentiometer VCC | 3.3V | Power |
| Potentiometer GND | GND | Ground |
| Potentiometer Signal | ADC0 (GP26) | Analog Input |

💡 Note: On the Pico W, **ADC(0)** refers to **GP26** by default.

---
