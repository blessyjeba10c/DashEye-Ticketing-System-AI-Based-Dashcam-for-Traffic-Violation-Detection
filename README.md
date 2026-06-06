# DashEye-Ticketing-System-AI-Based-Dashcam-for-Traffic-Violation-Detection
Developed an intelligent, edge-based dashcam system designed for real-time automated traffic violation monitoring and evidence logging.

# DashEye Ticketing System
### AI-Based Dashcam for Traffic Violation Detection & Police Verification


---

##  Overview

**DashEye** is an AI-powered dashcam system that automatically detects traffic violations in real-time, packages video evidence, and routes it to law enforcement for human verification before issuing challans/tickets. It transforms every vehicle into a mobile traffic enforcement unit — closing the massive gap left by fixed roadside cameras.

<img width="846" height="466" alt="WhatsApp Image 2026-04-15 at 10 46 07 AM" src="https://github.com/user-attachments/assets/69d70e42-9fb8-4ab3-8945-93b5b888f793" />


---

##  Problem Statement

Traditional traffic enforcement relies on fixed roadside cameras and patrol officers, leaving vast stretches of roads completely unmonitored. This results in:

- Widespread undetected violations (red-light jumping, overspeeding, unsafe overtaking, lane violations)
- Low accountability and careless driving behavior
- High manual labor costs for enforcement
- No visual evidence for disputed challans

---

##  Proposed Solution

DashEye converts every car into a **crowdsourced traffic monitoring node**:

1. **Dashcam continuously captures footage** of surrounding vehicles
2. **On-device AI (Edge AI)** detects violations in real time
3. **Evidence clip + GPS timestamp** is securely transmitted to the cloud
4. **Police verify** the evidence before any challan is issued
5. **Ticket/challan delivered** digitally or physically to the violator

> No direct automated punishment — human verification ensures fairness and prevents false positives.


<img width="1357" height="1600" alt="WhatsApp Image 2026-04-15 at 8 30 07 AM (1)" src="https://github.com/user-attachments/assets/fc455eb4-9219-4be7-b6fd-d71bb8888db9" />


---

##  System Flow

```
Dashcam Capture → AI Violation Detection → Violation Found?
                                               │
                                    Yes ───────┘
                                               ↓
                                       Save Evidence
                                               ↓
                                       Send to Police
                                               ↓
                                    Police Verification
                                               ↓
                                       Ticket Issued
```

### Detailed Pipeline

| Step | Component | Description |
|------|-----------|-------------|
| 1 | AI-Enabled Dashcam | Captures continuous video footage |
| 2 | Edge AI Processing | Real-time violation detection on-device |
| 3 | Secure Cloud Platform | Encrypted data transmission & storage |
| 4 | AI & Human Verification | Evidence review and validation |
| 5 | Ticketing System Interface | Automated citation generation |
| 6 | Ticket Delivery | Digital/physical notification to violator |

---

##  Tech Stack

### Hardware & Edge AI
- AI-Enabled Dashcam
- Edge TPU / GPU
- GPS, Accelerometer, Gyroscope

### Connectivity & V2X
- 5G / 4G LTE
- Wi-Fi 6, Bluetooth LE
- V2X (Vehicle-to-Everything) Communication Module

### Cloud Platform & Processing
- Secure Cloud Infrastructure
- Scalable Data Processing
- Distributed Databases

### AI Models & Analytics
- Computer Vision (Object Detection, OCR)
- Behavioral Analysis Models
- Violation Verification & Analytics

### User Applications
-  Mobile App for Drivers
-  Web Portal for Police Review
-  Law Enforcement Interface

---

##  Violations Detected

-  Red-light jumping
-  Overspeeding
-  Lane violations
-  Unsafe overtaking

---

##  Key Differentiators

| Feature | Traditional (Fixed Cameras) | DashEye |
|---|---|---|
| Coverage | Limited to fixed locations | Everywhere vehicles travel |
| Angle | Fixed angle only | Multi-angle, dynamic |
| Predictability | Predictable — easily avoided | Unpredictable coverage |
| False Positives | No human review | Police verification step |
| Scalability | High infra cost | Scales with vehicle adoption |

---

<img width="1600" height="1000" alt="WhatsApp Image 2026-04-15 at 10 43 28 AM" src="https://github.com/user-attachments/assets/bf3d6654-fe3a-46c6-ae10-99f7be8a33e0" />


##  Feasibility & Viability

###  Technical Feasibility
- Mature AI & Computer Vision models available
- Edge computing enables real-time on-device processing
- Reliable 4G/5G/Wi-Fi connectivity in urban areas

###  Operational Integration
- Seamless API integration with law enforcement systems
- Automated evidence packaging & secure transfer
- Low maintenance, user-friendly hardware

###  Economic Model
- High ROI through increased violation detection
- Reduced manual labor costs
- Scalable SaaS subscription + hardware sales model

###  Legal & Regulatory Compliance
- GDPR/CCPA compliant data handling
- Evidence meets court admissibility standards
- Policy frameworks for automated enforcement

---

##  Impact & Benefits

### Social Impact
- Increased driver accountability through deterrence
- Reduction in reckless and careless driving
- Fairer enforcement through verified evidence

### Economic Impact
- Reduced need for manual enforcement infrastructure
- Faster challan processing
- Revenue increase from broader violation detection

---

##  Repository Structure

```
dasheye/
├── hardware/
│   ├── dashcam-firmware/        # Edge AI firmware for dashcam
│   └── schematics/              # Hardware design files
├── ai-models/
│   ├── violation-detection/     # Computer vision models
│   ├── ocr/                     # License plate OCR
│   └── behavioral-analysis/     # Driving behavior models
├── backend/
│   ├── api/                     # REST API for evidence ingestion
│   ├── cloud-processing/        # Scalable processing pipeline
│   └── ticketing-engine/        # Citation generation service
├── frontend/
│   ├── driver-app/              # Mobile app for drivers
│   ├── police-portal/           # Web portal for police verification
│   └── admin-dashboard/         # System management interface
├── docs/
│   ├── architecture.md
│   ├── api-reference.md
│   └── deployment-guide.md
└── README.md
```

---

##  Getting Started

### Prerequisites
- Node.js v18+
- Python 3.10+
- Docker & Docker Compose
- GPU (for AI model training/inference)


<img width="1600" height="938" alt="WhatsApp Image 2026-04-15 at 10 38 20 AM" src="https://github.com/user-attachments/assets/1046c040-88a6-4243-abf2-a492a3cbd7df" />

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/dasheye.git
cd dasheye

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Install frontend dependencies
cd ../frontend/police-portal
npm install

# Start services with Docker
cd ../../
docker-compose up --build
```

### Environment Variables

```env
# Cloud & Storage
CLOUD_STORAGE_BUCKET=your-bucket-name
DATABASE_URL=postgresql://user:pass@localhost:5432/dasheye

# AI Models
MODEL_PATH=./ai-models/violation-detection/model.pt
OCR_MODEL_PATH=./ai-models/ocr/model.pt

# API Keys
JWT_SECRET=your-jwt-secret
ENCRYPTION_KEY=your-encryption-key

# Connectivity
MQTT_BROKER_URL=mqtt://localhost:1883
```

---

##  Research & References

1. **DMR Standards** — [dmrassociation.org](https://www.dmrassociation.org/dmr-standards.html)
2. **CVSD Audio Encoding** — [Wikipedia](https://en.wikipedia.org/wiki/Continuously_variable_slope_delta_modulation)
3. **NavIC Messaging & Positioning** — [nsilindia.co.in](https://www.nsilindia.co.in/sites/default/files/u1/2.11%20NavIC%20Messaging%20and%20Positioning%20Receiver.pdf)
4. **GSAT Communication** — [isro.gov.in](https://www.isro.gov.in/media_isro/pdf/ResourcesPdf/technology_transfer_august_2022.pdf)
5. **Public Safety Communication** — [mha.gov.in](https://www.mha.gov.in/sites/default/files/2022-12/COMMUNICATIONSTANDARDS_25102022_2%5B1%5D.pdf)
6. **Icom IP-M60 Hybrid Radio** — [icomuk.co.uk](https://icomuk.co.uk/IP-M60-Hybrid-LTE-Marine-VHF-Radio)
7. **AN/PRC-163** — [Wikipedia](https://en.wikipedia.org/wiki/AN/PRC-163)
8. **MotoTRBO / DMR** — [radiocoms.co.uk](https://www.radiocoms.co.uk/what-is-mototrbo)
9. **Defence Radios** — [bel-india.in](https://bel-india.in/category/defence/defence-communication-products/radios-basestations-repeaters)


---

##  License

This project is submitted as part of **Smart India Hackathon 2025**. All rights reserved by Team Megatron.

---

##  Contributing

This is a hackathon project. For collaboration inquiries, please open an issue or reach out to the team.

---
