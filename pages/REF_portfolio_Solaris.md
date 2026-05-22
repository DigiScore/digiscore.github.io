---
layout: page
title: REF Portfolio - *Solaris*
tags: impact
thumbnail-img: /assets/img/solaris.jpg
cover-img: /assets/img/solaris.jpg
---


# **Solaris: AI Jazz Quartet investigating embodied AI, togetherness and artificial perception.**

## **Description**
*Solaris* is a live‑performance jazz quartet that pairs three Embodied‑Intelligence‑driven AI agents (piano, bass, and 
a TR‑909 drum machine) with a single human drummer, embodying the Human‑AI Musicking Framework to generate core musical 
impetus from within the real‑time flow of music‑making. Acting as the centerpiece of a systematic musicological method, 
Solaris provides a concrete test‑bed for probing human‑AI co‑creativity—specifically relationship building, togetherness, 
and embodied meaning‑making—by examining how musicians perceive AI behaviour and using those insights to iteratively 
fine‑tune the AI’s operational parameters.


## **Questions**

***Core: How an artificial musician can be built, what minimal capacities it must possess, and whether the concrete 
system they have created (Solaris) actually fulfils those capacities in practice.?***

**Sub-Questions**

- How might we craft an artificial musician? (the overarching design problem that drives the whole study)
- What are the minimal conditions—a “basic‑package”—that an AI system must satisfy to exhibit perceptual experience in a musical context? (the theoretical foundation drawn from Kirk(2017))
- Does Solaris meet the criteria for perceptual experience as defined by Kirk’s basic‑package? (empirical test of the theoretical construct)
- Can Solaris achieve and sustain a sense of musical togetherness with human partners? (one of the three nested guiding principles)
- Is Solaris—or Creative‑AI more generally—sentient, or does it possess a form of mind when viewed through Peirce’s notion of synechism? (philosophical‑empirical question that follows from perceptual experience)
- How does the digital‑score interface communicate the AI’s internal state and support human perception of liveness, responsivity, and flow? (evaluation of the mediating visual medium)
- How does repeated co‑performance with Solaris affect human musicians’ trust, perceived responsiveness, and sense of togetherness? (longitudinal human‑AI interaction study)
- Is an embodied musicking dataset that captures physiological and psychological parameters from professional jazz improvisers sufficient to train AI models that generate co‑creative improvisation? (assessment of the data foundation)
- How do the four modular layers (Percept input, AI Factory, Gesture manager, Belief system) together enable real‑time, flow‑based music generation? (technical design question linking architecture to behavioural goals)
- Do the three nested guiding principles
  - (1) cope with dynamic flow, 
  - (2) have a musically‑attuned basic‑package, 
  - (3) maintain togetherness—constitute a robust framework for evaluating artificial musicians? (meta‑evaluation of the authors’ own framework)

## **System Design**
Solaris is a bottom‑up, flow‑driven artificial‑musician system that supplies three AI “instrument” agents (piano, bass, 
TR‑909‑style drum machine) to improvise in real time with a single human drummer. Its engineering rests on a purpose‑built, 
embodied‑musicking dataset that records audio, video‑based body motion, physiological signals (EEG and electro‑dermal 
activity) and self‑rated flow from professional jazz pianists. From this data five tightly coupled neural‑network models 
are trained to predict movement, affect, and their cross‑modal relationships; the models run continuously at ≈10Hz, 
producing streams that constitute the AI’s internal “mind”. Those streams are fed through a four‑layer runtime architecture
which together realise a self‑sustaining, affect‑driven improvisation engine:
- (1) Percept Input
- (2) AI Factory
- (3) Gesture Manager, and 
- (4) Belief System 

A “startled” interrupt forces an immediate behavioural reset when the acoustic environment spikes, reinforcing the 
perception of liveness. The Belief System maps the selected affective stream onto concrete musical actions (note 
generation, instrument selection, Lydian‑Chromatic tonal scaffolding) and simultaneously drives a visual digital‑score 
projection that conveys the AI’s internal state to the human performer, closing the perception‑action loop. 
Design choices (non‑symbolic training data, closed‑loop predictive ensembles, multimodal affective feedback, visual 
embodiment) embody the authors’ philosophical stance that music is an embodied joint‑action process and that a minimal 
“basic‑package” of perception, reflex, control, information, interdependence and conceptual language is sufficient for 
a machine to exhibit perceptual experience and, by extension, a form of sentient creative agency.

*Embodied musicking dataset*
- Audio of a standard jazz backing track + piano sound.
- Video‑derived 3‑D skeleton (nose‑position X) for expressive motion.
- Physiological recordings: EEG (BrainBit) and EDA (Bitalino) for arousal.
- Post‑performance flow self‑ratings (used for selecting “good‑flow” takes).
- 10 professional jazz pianists → 3‑5 improvisations each → 5‑chorus structure → best three retained.- 

*Neural‑network core (AI Factory) – five models, all running at ~10Hz*
- MoveRNN – LSTM, predicts next nose‑position from its own past.
- AffectRNN – 2‑D CNN, maps movement → EDA (arousal).
- MoveAffect-CONV2 – alternative movement → EDA predictor.
- AffectMove - CONV2 – inverse mapping EDA → movement. 
- Live‑Amplitude model – uses instantaneous audio amplitude to influence movement/EDA and to trigger “startled” events.

*Four‑layer real‑time architecture*
- Percept Input & Forming – captures live audio amplitude (and future sensor streams). 
- AI Factory – generates continuous streams of internal predictions from the five models. 
- Gesture Manager (Affect) – randomly selects one stream (duration 2‑8 sec), applies a “startled” interrupt when amplitude or prediction exceeds a threshold, and assigns an affective weight (high/med/low). 
- Belief System – rule‑based mapping of the chosen stream to concrete musical actions (instrument, note, velocity) using a compact Lydian‑Chromatic Concept matrix; controls “temperature” (density/stochasticity) and updates the visual digital score.

*Digital‑score interface*
- Visual grammar of abstract shapes and colours reflects AI affect (e.g., hue=arousal, shape‑complexity=note density).
- Projects in real time for the human drummer to anticipate AI intention, fostering trust and togetherness. 
- Can be ignored for a purely auditory focus, providing a flexible modality.

*Key design choices that differentiate Solaris*
- No symbolic music representation (no MIDI or notation) → AI operates directly in the flow of perception‑action. 
- Multimodal physiological training data → embeds a minimal “basic‑package” of perceptual experience (Kirk 2017). 
- Closed‑loop predictive ensemble → self‑sustaining mental dynamics that continue when external input momentarily drops. 
- Startled interrupt → guarantees rapid, observable reaction to salient musical events (liveness). 
- Visual embodiment (digital score) → supplies a second sensory channel for co‑creative interaction. 
- Philosophical alignment with embodied AI and synechism → treats the system as a continuous mind‑matter continuum rather than a purely computational black‑box.


## **Methodology**
The Solaris project was grounded in a practice‑based research design that treated the authors themselves as the primary 
musician‑participants. Starting from a theoretical scaffold that combined musical togetherness (Bishop 2024), Robert 
Kirk’s “basic‑package” of perceptual experience (2017), and the authors’ own Embodied Intelligence/Human‑AI Musicking 
Framework, the team distilled three nested guiding principles: (1) the system must cope with the dynamic flow of 
improvisation, (2) it must embody the minimal perceptual‑experience package, and (3) it must sustain a sense of 
togetherness with human partners. These principles acted simultaneously as design constraints and as the evaluative 
rubric for the whole system.

To instantiate the required perceptual capacities, the researchers constructed a bespoke embodied musicking dataset.
Ten professional jazz pianists performed a familiar standard (“How Deep Is the Ocean”) while their audio, 3‑D skeleton 
motion (nose‑position extracted from a depth camera), electro‑dermal activity, and EEG were recorded. After each 
improvisation the performers self‑rated their flow, and only the three takes each musician judged to be “good‑flow" 
were retained, yielding a multimodal corpus that couples movement, affect, and acoustic context without any symbolic 
(MIDI) representation. From this dataset five tightly coupled neural networks were trained – a movement‑predicting LSTM, 
two CNNs mapping movement to arousal and back, a second CNN for movement‑only prediction, and a simple feed‑forward model 
that reacts to live audio amplitude. All models run at roughly 10Hz, generating continuous prediction streams that 
constitute the AI’s internal “mind”.

These streams are processed by a four‑layer real‑time architecture. The first layer ingests live audio amplitude; the 
second (the AI Factory) supplies the prediction streams; the third (the Gesture Manager) randomly selects one stream for 
a 2–8‑second window, weights it with an affective level, and applies a “startled’’ interrupt whenever audio or a 
prediction exceeds a preset intensity—thereby guaranteeing an immediate, observable reaction that reinforces liveness. 
The fourth layer (the Belief System) maps the selected affective stream onto concrete musical actions (instrument choice, 
pitch, velocity) using a compact Lydian‑Chromatic tonal matrix and a temperature parameter that controls note density. 
Simultaneously it drives a digital‑score visualiser, a projected abstraction of shapes, colours and motion that encodes 
the AI’s internal state and provides the human drummer with a second sensory channel for anticipating the machine’s 
intentions.

Evaluation proceeded iteratively. Solaris performed in a series of public concerts (recorded and posted on Bandcamp) to 
test system stability in uncontrolled environments. Controlled laboratory sessions invited three professional drummers 
(representing free‑jazz, mainstream, and hybrid backgrounds) to improvise with Solaris across multiple tracks; after 
each session the drummers completed an eight‑item Likert questionnaire probing perceived competence, responsiveness, 
trust, and togetherness, and offered free‑form comments. A broader RENCON listening test presented a single Solaris 
recording to a music‑technology community, asking listeners to attribute authorship (AI vs. human) and to comment on 
artistic quality. The data from these evaluations fed back into the system: temperature, affect weighting, and startle 
thresholds were tuned, and the visual‑score mapping was refined. Across repeated sessions participants reported 
increasing trust and a stronger sense of musical togetherness, especially when they engaged with the visual score, 
while the free‑jazz specialist’s withdrawal highlighted the influence of prior musical expectations.

Overall, the methodology combined a theoretically informed, embodied data collection with a layered, affect‑driven AI 
architecture and a multimodal evaluation loop, all conducted from an insider perspective. This practice‑based approach 
allowed the authors to iteratively craft a system that meets their minimal perceptual‑experience criteria and demonstrates 
 genuine co‑creative interaction with human musicians.


## **Findings**
Insights from the Solaris project suggest that a bottom‑up, embodied‑AI approach could produce an artificial musician 
that is experienced by human players as a genuine, co‑creative partner. By training on a multimodal “embodied musicking” 
dataset (audio, motion, EEG/EDA and self‑reported flow) and wiring the models into a four‑layer, affect‑driven architecture, 
the Solaris quartet generates real‑time improvisations that satisfy the behavioural criteria for musical togetherness 
(awareness of intentional partners, mutual perception of liveness and responsivity) and the minimal “basic‑package” of 
perceptual experience proposed by Kirk. The visual “digital‑score” interface further mediates the AI’s internal state, 
making the machine’s intentions perceptible and strengthening trust and joint attention. 

Empirical tests with professional drummers and a broader listening audience confirm that musicians perceive Solaris as 
a competent, sometimes surprising jazz improviser, report increasing feelings of togetherness and flow over repeated 
interactions, and react positively when the digital score is used. On the philosophical side, the authors argue—using 
Peirce’s notion of synechism—that such context‑bound, embodied behaviour justifies speaking of sentience for a 
Creative‑AI system, while also emphasizing that sentience should be understood relationally rather than as an absolute, 
human‑only property. In short, the work validates the three nested guiding principles (dynamic flow → basic‑package → 
togetherness) as sufficient for an artificial musician and demonstrates that contextual, embodied AI can co‑create 
music in a way that feels sentient, collaborative and artistically valuable.

*Core findings*
- Embodied dataset → richer AI behaviour 
  - Multimodal recordings (audio, 3‑D skeleton, EEG, EDA, flow self‑ratings) from professional jazz pianists provide the minimal “basic‑package” of perception, control, information, interdependence, and conceptual language that Kirk identifies as necessary for perceptual experience.

- Four‑layer AI architecture produces continuous, affect‑driven music
  - Percept input (live audio & self‑awareness). 
  - AI Factory (five tightly coupled neural nets generating prediction streams).
  - Gesture manager (random‑duration selection, affect weighting, “startled” interrupt for immediate liveness).
  - Belief system (Lydian‑Chromatic tonal matrix, temperature control, generation of notes and visual cues).

- Digital‑score visual interface bridges machine–human perception
  - Abstract shapes and colours convey affect, density and instrument role in real time, giving the human drummer a perceptible window onto the AI’s “mental state” and enhancing joint action. 

- Empirical evidence of musical togetherness 
  - Professional drummers rated Solaris higher on competence, responsiveness, trust and flow after repeated sessions.
  - Those who attended to the digital score reported significantly stronger feelings of togetherness.

- Surprising, creative decisions emerge from the system
  - “Startled” events and affect‑driven gesture selection lead to spontaneous, musically coherent turns (e.g., unexpected quiet passages that force the human player to adapt), mirroring the improvisational dynamics of human jazz ensembles.

- Validation of the three nested guiding principles
  - (i) Coping with dynamic flow – Solaris maintains performance despite fluctuating musical inputs.
  - (ii) Musically‑attuned basic‑package – the embodied dataset satisfies Kirk’s perceptual‑experience criteria.
  - (iii) Maintenance of togetherness – musicians experience the four Bishop conditions in real time.

- Contextual sentience claim
  - Using Peirce’s synechism, the authors argue that Solaris exhibits a form of mind‑continuity: it perceives, reacts, and communicates within the musical environment, justifying the term “sentient” when the concept is taken as relational and contextual rather than absolute.

- Implications for AI‑human artistic collaboration
  - The study demonstrates that creative‑AI need not mimic symbolic representations (MIDI, scores) to be musically meaningful; instead, grounding AI in embodied perception and affect yields a partnership that expands human creative horizons.
  - It challenges Cartesian dualism by showing that an artificial system can participate in the flow of musicking, thereby opening new avenues for symbiotic human‑AI ecosystems in the arts.
  - These findings collectively support the view that sentient‑like, co‑creative artificial musicians are achievable today when design is rooted in embodied practice, multimodal data, and interactive visual mediation.


## **Dissemination**
- a. Conference papers
    - i. Vear, C., Benford, S., Avila, J. M., & Moroz, S. (2023, August 30-September 2). Human-AI Musicking: A Framework for Designing AI for Music Co-creativity [Paper presentation]. Artificial Intelligence and Music Creativity 2023, Sussex University. https://aimc2023.pubpub.org/pub/zd46ltn3/release/2
    - ii. Vear, C., & Poltronieri, F., (2024) “Musicking with Solaris – a systematic musicology method to identifying relationship building, togetherness and meaning-making in human-AI co-creativity”. Proceedings of First International Conference of MAI Music Studies, Stockholm, December 2024
    - iii. Vear, C., Poltronieri, F., DiDonato, B., Zhang, Y., Benerradi, J., Hutchinson, S., Turowski, P., Shell, J., & Malekmohamadi, H. (2024, April). Building an Embodied Musicking Dataset for co-creative music-making. Presented at 13th International Conference on Artificial Intelligence in Music, Sound, Art and Design (EvoMUSART) 2024, Aberystwyth University, Wales
    - iv. Poltronieri, F., & Vear, C. (2024, June). Towards sentience: A path through jazz, datasets and digital scores. Paper presented at International Symposium of Electronic Art 2024, Brisbane, AustraliaBenford, S., Hazzard, A., Vear, C., Webb, H., Chamberlain, A., Greenhalgh, C., Ramchurn, R., & Marshall, J. (Eds.). (2023). Five Provocations for a More Creative TAS [Edited Proceedings]. First International Symposium on Trustworthy Autonomous Systems (TAS 23), Edinburgh, UK. https://doi.org/10.1145/3597512.3599709
    - v. Poltronieri, F., & Vear, C. (2025, October 25-27). AI sentience is just around the corner: SOLARIS 2, a creative-AI score and punk rock band with human in the loop [Paper presentation]. TENOR2025: The 10th International Conference on Technologies for Music Notation and Representation, Beijing, China. https://www.tenor-conference.org/
    - vi. Vear, C. (2025, October 25). Digital Musicking -Transformational Encounters with the Digital Score [Keynote]. TENOR2025: The 10th International Conference on Technologies for Music Notation and Representation, Beijing. https://doi.org/10.1145/3771594.3771600
- b. Book Chapters
  - i. Vear, C., & Poltronieri, F. (2025). Crafting Artificial Musicians: Building Solaris as a Co-operative, Perceiving and Creative AI. In N. Zagalo, & D. Keller (Eds.), Artificial Media: Emerging Trends in Narratives, Education and Creative Practice (Part F717, pp. 215-239). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-89037-6_11
  - ii. in *Digital Musicking* - Vear, C., & Poltronieri, F., *Under Development*
  - iii. Vear, C. (2022). Embodied AI and Musicking Robotics. In C. Vear, & F. Poltronieri (Eds.), The Language of Creative AI: Practices, Aesthetics and Structures (pp. 113-135). Springer International Publishing. https://doi.org/10.1007/978-3-031-10960-7_7
- c. Full AI  code (CV as main designer, Dr Fabrizio Poltronieri as designer of visual score) [LINK](https://github.com/DigiScore/AI_jazz_trio) 
- d. Complete Recordings of Live and Studio Performance [LINK](https://solarisjazz.bandcamp.com/)
- e. Documented performances
    - [Blue in Green](https://www.youtube.com/watch?v=KZwHuRAml78&t=112s)
    - [Breaking the Law](https://www.youtube.com/watch?v=15zECmGMX4I)
    - [Franks Mood](https://www.youtube.com/watch?v=8ZP70jMoGxQ)
    - [Giant Steps](https://www.youtube.com/watch?v=kw9n1-pwiFE&t=29s)
    - [Intergallactic](https://www.youtube.com/watch?v=dGXQqj0zh9s)
    - [Giant Steps - Zurich](https://www.youtube.com/watch?v=PXzWlM4BunM)
    - [Giant Steps - Premiere](https://www.youtube.com/watch?v=6C74E3V0NOs)
    - [Experimenting with Steinway Piano](https://www.youtube.com/watch?v=XrooTB_g4_0)
  

