---
layout: post
title: Neoscore competition commission 
subtitle: GuitaRPG by Xavier Davenport
cover-img: /assets/img/GuitaRPG.jpg
thumbnail-img: /assets/img/TENORg.png
tags: case_study
---
**DigiScore TENOR commission: Xavier Davenport**

Data set: [http://doi.org/10.17639/nott.7318](http://doi.org/10.17639/nott.7318)

Digital Score Github: [https://github.com/Xavman42/GuitaRPG](http://doi.org/10.17639/nott.7318)

_GuitaRPG_ is a digital score created through the Neoscore platform by musician Xavier Davenport. The digital score incorporates game-like behaviour such as role-playing when the performer is in different regions of the digital score. These regions display a distinct set of influences on the performer through a different colour palette for symbols, glyphs and sound worlds. The performer has to incorporate these elements to progress through the digital score. Another aspect of this role-playing is skill acquisition whereby in exploring each region, the performer comes across different guitar techniques and sound worlds - the accumulation of these skills progressively gets more complex and complicated as one moves through different regions of the game. The piece is driven by these two factors - a sense of geographic exploration and the players' progression through skill acquisition contributing to the structure and flow of the piece. The player has control over how long they stay in each region to explore a certain technique through macro and micro involvement with the piece. For instance, in macro involvement, the player navigates the map with a single button moving through regions of the digital score where certain types of materials will appear. On the other hand, by engaging with each region through playing techniques as they randomly appear, one engages with the piece on the micro level. The changing density of the visual materials denoted by different colours for playing techniques is controlled by a weighted algorithm. Through the accumulation of visual materials that the performer can respond to, one loses track of the exact and improvised interpretation, freeing up the performer towards more improvisatory playing when the exact interpretation becomes no longer possible. 
 
The project was realised with the novel digital score platform Neoscore and was supported by Andrew Yoon and Craig Vear and commissioned through the Digital Score project.
 
**Objectives**
 
The composer/performer intended to create a series of distinct sound worlds where the performer does not initially fit in. The primary focus was to create a map as a navigation tool where the performer could explore different sound worlds by interacting with visual and sonic materials. By passing through these worlds the performer could accumulate different playing techniques as well as ways to blend into the sound world of each region. 
In addition to interacting with visual materials, the composer/performer wanted to build interactivity through sound processing controlled by Supercollider in each region. 
 
 
**Process**
 
To realise the objectives of making _GuitaRPG_, Xavier engaged with the Neoscore platform. In doing so a lot of back and forth between the developer of Neoscore and Xavier had to happen.
 
Xavier systematically divided up his work in programming/coding the digital score for weeks and months proceeding to the premier at TENOR23. He focused region by region in his digital score starting with SuperCollider programming of the effects and sound files then moving on to working on Python (Neoscore) programming. 
 
Initially, in Neoscore, Xavier focused on the macro-level decisions to do with map navigation according to the different regions of the map. Later getting into the beautification part of the score as well as the visualisation of the SuperCollider output. 
 
Working systematically through the regions, he decided to focus on different sound qualities something to explore in each of the three regions. Moving on to Python programming with Neoscore, Xavier was able to discover new features that could be useful for his digital score. Through the back-and-forth with Andrew Yoon, he was able to implement new features into the libraries that he was working with:

- Adding built-in support for keyboard and mouse input: [https://github.com/DigiScore/neoscore/issues/57](http://doi.org/10.17639/nott.7318)

- Allowing animation without re-rendering the items on the screen: [https://github.com/DigiScore/neoscore/issues/91](http://doi.org/10.17639/nott.7318)

- Rotating staff objects and their children: [https://github.com/DigiScore/neoscore/issues/9](http://doi.org/10.17639/nott.7318)


**Critical Insights from the Data Set Analysis**

**Materials**

- connection to the digital score for the performer is visually driven (colours, symbols and glyphs) and accounts for most references in the data 
- performer made strong associations between colours and specific guitar techniques to improvise with them as they reappear in the later stages of the work
- when the appearance of glyphs and symbols became very dense, the performer was able to react to their colour and use it as an inspiration for improvisation rather than a notation to interpret
- the timed visual stimuli in the scrolling score pushed the performer to make compelling musical decisions that he has not done previously in the moment of performance

**Sound-world**
- _GuitaRPG_ incorporated the concept of geographic exploration through a series of soundscapes
- each region of the map has a distinct soundscape which becomes modified through the player’s technique level and engagement with the digital score
- the player is trying to fit into the soundscapes in a particular region to change them and to move through the region
- the electronic sounds in the piece and the player's interaction with them acted as a partner with whom the performer could collaborate and improvise 

**Interactivity**
- the use of Neoscore made reaching higher levels of interactivity more possible  
- by using Neoscore, the performer feels that he reached new levels of visual complexity in addition to incorporating electronics and sound effects into the work
- normally, he is distracted thinking about interactivity which takes him away from his music making while in GuitaRPG he was able to just focus on the performance
- in _GuitaRPG_, everything is simplified through programming, interaction was made more direct through the use of a single button to navigate the piece

**Algorithmic agents**
- there was a certain level of algorithmic randomness in each geographic region that even the performer was not aware of
- this helped the musician to retain a sense of exploration in the moment of performing the work
- implicitly structured randomness is desirable as it gives the piece a sense of purity rather than predetermined structural decisions
- using the weighted probability distribution algorithm in the piece freed the musician from making complicated decisions in interpretation during the performance

**Flow**

The flow in the digital score was maintained through the performer’s engagement with the sense of macro and micro navigation of the digital score.

*Macro:*
- display on the top of the map of the digital score to let the performer know where he has travelled to before and also allows the performer to explore in an informed way
- performer has some control over the types of materials that will appear in different regions of the map
- by choosing to stay in certain areas of the score, the performer increases the probability of certain score elements 

*Micro:*
- the flow of the performance is in the explorative nature of the score – a sense of exploration is built into the score from the point of view of the performer and the audience 
- this allows for exploration in sound that is built on interactivity and anticipation
- the score provides an interesting way for an improviser to explore a diversity of sound, and improvisational structure 

**Surprise**
- a smooth transition from the literal interpretation of symbols to improvised took the performer by surprise in the performance
- the general nature of some elements (in their length and location in the score) when combined can create an element of surprise for the performer who is very familiar with them as a composer


**Digital Musicianship**

**Neoscore and programming**
- builds on performer’s pre-existing skills in coding and improves them greatly 
- in addition, the musician has contributed to fixing issues in the programming of Neoscore:
- better graphical implementation [https://github.com/DigiScore/neoscore/issues/29](http://doi.org/10.17639/nott.7318)
- fixing the math behind the set_viewport_scale function [https://github.com/DigiScore/neoscore/issues/89](http://doi.org/10.17639/nott.7318)
- text with white spaces being clipped correctly [https://github.com/DigiScore/neoscore/issues/34](http://doi.org/10.17639/nott.7318) and [https://github.com/DigiScore/neoscore/issues/93](http://doi.org/10.17639/nott.7318)
- actively contributing to making some glyphs that were used in the score: [https://github.com/Xavman42/GuitaRPG/blob/main/NeoScore/Cells.py](http://doi.org/10.17639/nott.7318)
- using Neoscore allowed Xavier to express ideas that he was already developing in a non-digital format
- these concepts became much more effective with Neoscore 
- allowing him to achieve new levels of visual and interactive complexity

**Learning through the piece**
- for the interpreter, a sense of player progression and skill acquisition is built into the digital score
- the learning curve for approaching this digital score is very low
- one is taught how to interpret the piece throughout the performance

**Performer agency and accessibility**
- the performer can choose which technique to level up by staying in a particular region of the piece for longer periods
- certain regions of the piece can be emphasized by the performer as desired
- performer must make decisions at the moment when reading the scrolling score
- any performer (guitarist) with good sight-reading ability and improvisation experience can navigate the score
- the performer has the freedom to interpret the score, it is not important or necessary how one navigates the score


**Transformations**

**Complexity and liveness as facilitated by Neoscore**
- Xavier finds it accessible allowing him to realize complicated digital score ideas instantly
- was able to incorporate game mechanics at a level of complexity that he has not achieved before
- can deal with a higher level of mathematics in a digital score
- could have complicated algorithms and procedures all under one hood in the score
- the live nature of the score forced him to experience making decisions on the fly that he has not experienced before

**New Innovative experiences** 
- when the material becomes too dense, the performer is not aware when transitioning between reading the score literally and improvising 
- for an inexperienced improviser the score provides an easy way to explore a diverse array of sounds
- at the end of the piece always discovers something new because of the different combinations of symbols and overlapping colours that are experienced at different locations in the piece

**Summary**

The analysis of the data set from the GuitaRPG performance found that the score is driven by visuals, colours, symbols and glyphs to account for most references in the data. The performer made strong associations between specific guitar techniques with colours and used them as an inspiration for improvisation rather than a notation to interpret. The digital score allowed for exploration of soundscapes through geographic exploration and incorporated the concept of interactivity through Neoscore. Algorithmic agents provided a certain level of algorithmic randomness which the performer was not aware of. The flow was maintained through macro and micro navigation and the use of surprise elements while interacting with the digital score offered unexpected surprises. The performer improved existing coding and programming skills which was necessary for creating the piece as well as learning methodologies that could improve accessibility and agency by both experienced and less-experienced improvisors. The digital score facilitated its complexity and liveness while also allowing new innovative experiences to be explored.

**Personnel**

[Xavier Davenport](https://www.xavierdavenport.com/) 


















