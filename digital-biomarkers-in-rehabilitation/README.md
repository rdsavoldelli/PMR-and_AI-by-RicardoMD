# Digital biomarkers in rehabilitation

This folder is part of the **PMR and AI** initiative by **Ricardo Diaz Savoldelli, MD (Physical and Rehabilitation Medicine)** and aims to bridge **clinical rehabilitation, biomechanics, and artificial intelligence** through the lens of **digital biomarkers**.

## 1. What are digital biomarkers?

Digital biomarkers are **objective, quantifiable physiological and behavioral data** collected through digital devices such as wearables, smartphones, inertial sensors, and connected platforms.  
They can capture and monitor:

- Gait and balance
- Physical activity levels and sedentary behavior
- Sleep patterns
- Cardiovascular and autonomic responses
- Cognitive and motor interaction with digital tasks

In rehabilitation, these signals become clinically meaningful when they are:

- **Continuously measured**
- **Linked to functional outcomes**
- **Used to guide or adapt treatment**

## 2. Why digital biomarkers matter in rehabilitation

Traditional rehabilitation assessment is often:

- Episodic (clinic-based)
- Subjective (scales, questionnaires)
- Limited to short snapshots in time

Digital biomarkers allow us to:

- Monitor patients **in real life**, not only in the clinic
- Detect subtle changes in gait, balance, activity, and function
- Track **recovery trajectories** after stroke, trauma, surgery, or critical illness
- Identify **risk of falls** or deterioration before a major event
- Feed **AI models** that can predict outcomes and recommend personalized interventions

Recent work using wearable sensors in stroke rehabilitation shows how gait patterns collected from inertial sensors can be quantified over time and used to analyze functional improvements and risks such as falls or decreased engagement in therapy. Systematic reviews of wearable and VR-based interventions in stroke survivors show that sensor-supported technologies can improve gait, balance, and engagement when used as an adjunct to conventional rehabilitation. Motion sensors and digital biomarkers are increasingly being used to capture motor recovery patterns and guide individualized rehabilitation strategies.

> As a physiatrist and biomechanical movement specialist, my interest is not only in **measuring** these biomarkers, but in **translating them into clinical decisions**.

## 3. Examples of digital biomarkers in rehabilitation

### 3.1 Gait and balance

- Gait speed
- Step length and variability
- Stance/swing phase proportions
- Asymmetry indices
- Center-of-mass or center-of-pressure dynamics

**Applications:**

- Post-stroke gait recovery
- Parkinson’s disease and other movement disorders
- Risk of falls in older adults
- Performance optimization in athletes

### 3.2 Activity and participation

- Daily step count and activity intensity
- Time spent sitting or lying down
- Adherence to home-exercise programs
- Patterns of use of affected limb in unilateral injuries

**Applications:**

- Post-ICU rehabilitation
- Post-COVID functional recovery
- Long-term follow-up in musculoskeletal and neurological conditions

### 3.3 Digital biomarkers in sports and high performance

In athletes, digital biomarkers can be used to:

- Monitor load and fatigue
- Detect early signs of overuse or asymmetry
- Optimize return-to-sport after injury
- Combine **movement data + performance metrics + subjective load** into AI-based decision support

This connects elite sports performance with the same principles used to prevent falls and functional decline in older adults — a continuum of **human movement health**.

## 4. From signal to decision: the AI bridge

The value of digital biomarkers is not only in collecting signals, but in:

1. **Pre-processing and feature extraction** from raw sensor data (e.g., IMUs, smart insoles)
2. **Designing clinically meaningful features**, such as:
   - Gait speed
   - Variability
   - Symmetry
   - Complexity of movement
3. **Training AI/ML models** to:
   - Predict risk of fall
   - Classify functional status
   - Recommend intensity or type of intervention
4. **Integrating outputs into clinical workflows**, in a way that supports:
   - Physicians
   - Therapists
   - Patients and caregivers

As a bridge-builder between **Rehabilitation Medicine, Biomechanics, and AI**, my focus is to design pipelines that are:

- Clinically interpretable
- Grounded in real patient journeys
- Useful both in elite sports and in vulnerable populations (older adults, post-ICU, post-COVID)

## 5. Example: conceptual gait biomarker pipeline

In this folder, you will find a conceptual Python script:

- `example_gait_biomarkers_pipeline.py`

It illustrates how a simple time-series of gait-related signals (e.g., from inertial sensors) can be:

1. Loaded as data
2. Processed into features (speed, variability, symmetry)
3. Used in a basic machine learning model to classify, for example:
   - “Low fall risk” vs “High fall risk”
   - “Ready for next rehab phase” vs “Needs current level”

This is **not** production code, but a didactic bridge between **clinical questions** and **AI thinking** in rehabilitation.

## 6. Future directions and open questions

Some of the open questions that I explore as a clinician and researcher:

- How can we integrate digital biomarkers into routine rehabilitation, without overwhelming clinicians?
- Which biomarkers are most relevant for:
  - Falls in older adults
  - Post-ICU and post-COVID recovery
  - Elite sports and return-to-play?
- How can we ensure equity and access, so that digital biomarkers **reduce**, and not **increase**, health disparities?
- How can AI models trained on digital biomarkers remain explainable and trustworthy for clinical use?

These questions will guide future content in this folder, including:

- Example datasets (when possible)
- Jupyter notebooks
- Case-based examples connecting patient stories, movement data, and AI.

---

📧 For collaboration or discussion on digital biomarkers, AI, and rehabilitation:  
**ricardo.diaz@extremityrehab.com**

> This content is part of the broader project: **PMR and AI by RicardoMD** — exploring the future of Physical and Rehabilitation Medicine at the intersection of biomechanics, technology, and human performance.
