---
layout: post
title: DigiScore TENOR Neoscore commission: Lauren McCall 
subtitle: Kaleidoscore by Lauren McCall
cover-img: /assets/img/TENORg.png
thumbnail-img: /assets/img/TENORg.png
tags: case_study
---

**DigiScore TENOR Commission Lauren McCall**

Data Set: [http://doi.org/10.17639/nott.7319](http://doi.org/10.17639/nott.7319)

<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<div class="nv-iframe-embed"><iframe loading="lazy" title="TENOR BOSTON 2023 - CONCERT #1: Monday, May 15, 2023, 5:00 pm" width="100%" height="100%" src="https://www.youtube.com/embed/YrMOZlZ5QP0?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
</div></figure>

_Kaleidoscore_ is a digital score created through a Neoscore platform by composer Lauren McCall. The digital score incorporates digital images, shapes and key codes sending OSC messages in Neoscore to trigger 4 backing track samples in the Max MSP patch. A sense of duality is built through the imagery of the digital score such as changing colours, triangles and squares and the relationship between the two performers. When the shapes change colour it could represent a change between different dissonant material with each player. The digital score is fairly open with just a few instructions such as to play consonant sounds on flower imagery or when the notes appear without stems.

The project was realised with the novel digital score platform Neoscore and was supported by Andrew Yoon and Craig Vear and commissioned through the Digital Score project.

**Objective**

For a Neoscore graphic score, Lauren wanted to create an animated graphic score that is similar to a kaleidoscope. Thus, the intention was to build a graphic score that would be in the shape of a circle, and inside this circle is where the shapes could move, and change colour and order based on key codes set up through the Python live coding interaction. The design for the graphic images would draw inspiration from biomorphic patterns, and notated music will be interwoven into the design. The main setup for this project would be through a precoded Python script in Neoscore, and the key code interactions that will change the movement of the shapes would be used in the Python live coding environment so users can press single key codes to change the shapes within the circle in different ways.

**Process**

*Animation*
Initially, Lauren cut out images and experimented with image duplication to arrive at the kinds of shapes (circles, squares and triangles) that were used as an inspiration for drawing objects in Neoscore. In later stages, Lauren started to experiment with colour changes and object rotation, learning that it is easier to rotate images rather than drawn objects. For the Kaleidoscore eye object, Lauren used an image of a camera eyepiece with different circumferences. In the final design, Lauren started to use pyOSC to send values to Max/MSP. Through some feedback during a showcase at Georgie Tech, Lauren decided to incorporate more duality with the symbolism she used as well as animating the camera eyepiece in the digital score towards the end of the piece. In programming, using dictionaries for some of the shapes and condensing animation code helped and was assisted by Craig Vear. 

*Sound Design*
In sound design, Lauren experimented with using a sampler object in Max/MSP playing shorter and longer sample sizes. Eventually, she settled on a longer sample size using a conditional setup with a clocker object which created a slight delay between an image change and a sound sample change when a key code was sent from Neoscore. She designed her longer sound samples in LogicPro:

1. One sample had just a drumbeat. 
2. Another sample used the sound chain of a noise gate to map the drum beat to some underlying chord progressions. 
3. In one sample version, a remix effect was used on a drum beat in LogicPro. 
4. One sample version added a bass part. 
5. A final sample version added underlying strings (which can ultimately be substituted with live violinists).


**Critical Insights**

*Materials*

-the interpretation of the digital score was driven by interactions between sound and visual materials as well as between the musicians 
-the translation of visuals to music was fairly open with a few instructions for consonant sounds when flower images appeared
-overall, musicians preferred the parts that were more explained in the instructions as it was easier for them to make connections with the digital score and with each other 
-interaction with the composer helped to establish some other relationships to the materials such as camera eyepiece movement suggesting cross-rhythms, camera eyepiece opening suggesting musical idea being expanded, colour changes – the intensity of the musical ideas.
-otherwise, the openness of the digital score gave musicians the freedom to experiment with the materials and to try new things which is what the composer intended
-the duality of images and their colours were meant to give musicians a chance to explore different dissonant material and their changes with each other
-musicians felt that they would have developed a more interesting relationship with images and their behaviour in the piece if they had more time

*Flow*

-the composer was satisfied with the way the musicians were able to add dissonance to the music with backing tracks that were mostly consonant, this added flow to the music
-one of the performers appreciated this sense of flow and learned something new about improvising freer dissonances over consonant backing tracks
-because the performers had different roles (one of them triggering sections of the piece and playing, the other just playing), they had different experiences of flow in the digital score
-for the performer who was triggering the keycodes a sense of flow was more difficult to reach as he was mostly concerned with triggering the next section than how he was interacting with another performer
-the other musician also felt these interruptions in the flow due to the changes that the other musician had to make
-the composer also feels that it would have been more beneficial to have a third person change the triggers (keycodes) in the digital score

*Digital Musicianship*

*New Skills & Musical Experiences*
-Lauren learned how to build on her coding abilities, using dictionaries, to simplify and organise code in Neoscore 
-she feels like Neoscore makes the possibility of animated graphic scores easier to develop
-one can use a variety of possibilities in the music like text, images and sound this makes the platform very accessible, especially with students in schools with different backgrounds where Lauren teaches
-she thinks musicians should think more about how code contributes to the creation of music
-the musician operating Neoscore during the piece learned new command lines in Python 
-he also learned a lot about various Python dependencies and what one should do in the future if using Python programmes as part of a performance
-this builds on his previous coding experience
-one of the composer’s intentions was to provide a form when it comes to the structure of the piece so that graphic images could be easily interpreted
-as a result, one of the performers felt like he learned to go out of the structured melodic parts into more dissonant parts all while playing over consonant backing tracks
-the same performer does not feel like he would arrive at the same result without Lauren’s piece

*Accessibility*
-musicians felt like the graphic interface of the piece made it accessible to any performer at ease with improvisation 
-however, they felt like both the technical and score instructions could be clearer so as not to second guess what the composer intended
-musicians learned that having clear instructions in their music which uses technology could be very beneficial to the rehearsal process

*Transformations*
-the musicians found the compositional approach in this piece novel as they were able to play different score materials than they are normally used to
-one of the musicians enjoyed the combination of tonal-conventional music with freer possibilities as well as the animation which he hopes to engage with more in the future
-for Lauren, this experience opens possibilities of developing graphic scores geared towards musicians with a jazz-based improvisatory or other backgrounds
-Lauren thinks that the possibilities with Neoscore are very diverse as creatively her and Xavier’s pieces were so different 
-she finds Neoscore platform inclusive as it does not require any particular music background thus students from diverse musical backgrounds could benefit from it

*Summary*

In Kaledoscore, the interpretation was influenced by interactions between sound and visuals, as well as between the musicians themselves. The translation of visuals to music allowed for some openness, with specific instructions for consonant sounds when flower images appeared. Musicians preferred the parts that were more explained in the instructions, as it made it easier for them to connect with the digital score and each other. Interaction with the composer helped establish additional relationships to the materials, such as using camera eyepiece movement and color changes to convey musical ideas. The openness of the digital score allowed musicians to experiment and try new things. The duality of images and colours encouraged the exploration of different dissonant materials. Musicians felt they would have developed a more interesting relationship with the visuals if they had more time.
The composer was satisfied with how musicians added dissonance to the music with consonant backing tracks, enhancing the flow. One performer learned about improvising freer dissonances over consonant tracks. Different roles affected the flow experience, as the performer who was triggering sections was more focused on transitions rather than interaction. The composer suggests having a third person handle triggers for better flow in the future. Digital musicianship led to new skills and experiences. Lauren improved her coding abilities and found Neoscore helpful for creating animated graphic scores. The platform's variety of possibilities, including text, images, and sound, make it accessible for musicians with diverse backgrounds. The performer operating Neoscore learned Python commands and dependencies. Providing a structured form in the score allowed one performer to explore dissonant parts while playing over consonant tracks. Accessible graphic interfaces benefited performers comfortable with improvisation, but clearer technical and score instructions were desired. 
The piece's compositional approach was novel, allowing musicians to play different score materials. This digital score experience with Neoscore opened up possibilities for Lauren in developing graphic scores for musicians with jazz-based improvisatory backgrounds. Lauren finds Neoscore to be an inclusive platform that could benefit students with diverse musical backgrounds.

*Personnel*

[Lauren McCall](https://www.laurencmccall.com/) 

Ben Eidson saxophone

[Emiliano Lopez](https://www.instagram.com/emiliano_9409/) guitar
