# LazyPad-HACKPAD-

A custom mechanical hackpad designed and built for **Highway/Undercity**, a Hack Club hackathon.

---

## Motivation

I created LazyPad to build a compact, personalized mechanical keypad that speeds up my workflow and helps me learn hardware design. Since Fusion360’s free trial is limited to high schoolers, I chose Onshape as a free, powerful alternative. This project helped me explore CAD design, PCB layout, soldering, and microcontroller programming.

---

## Design Process

- **CAD Modeling:** Designed the case and layout in Onshape focusing on ergonomics and compactness.
- **PCB Design:** Created the circuit board using KiCad, integrating Cherry MX switches and SK6812 MINI RGB LEDs.
- **Firmware:** Programmed the Seeed XIAO RP2040 microcontroller using KMK firmware to manage keys and LEDs.
- **Assembly:** Soldered components and assembled the final product, turning digital designs into a physical device.

---

# Moved BOM to BOM.csv

---

## Pictures

![Front View](https://github.com/user-attachments/assets/f28dcfbc-5198-44d0-ae44-b32932f7e12b)  
![PCB Close-up](https://github.com/user-attachments/assets/218a70e4-9c8a-48ef-a3ef-6b89092487b2)  
![Assembly Process](https://github.com/user-attachments/assets/fcb8847d-e03a-42eb-afd3-8ec0492d0dad)  
![Finished Product](https://github.com/user-attachments/assets/152ee721-99f1-4840-8f9b-1bf962af744e)

---

## Challenges Faced

- Fusion360 trial limitations led to switching to Onshape, which required adapting to a new CAD tool.
- Finding compatible parts and footprints for PCB design took time and trial.
- Soldering tiny LEDs and switches pushed my patience and precision.
- Learning KMK firmware and Python programming for the microcontroller was a rewarding challenge.

---

## Future Improvements

- Add dynamic RGB lighting effects with SK6812 MINI LEDs.
- Expand key count and add programmable macros.
- Design and 3D print a custom case for a professional finish.
- Explore wireless connectivity options like Bluetooth.

---

## How to Use

1. Flash the KMK firmware to the Seeed XIAO RP2040.
2. Connect the hackpad to your computer via USB.
3. Customize keymaps and macros in the KMK firmware code.
4. Use the hackpad to boost your productivity with custom key combos.

---