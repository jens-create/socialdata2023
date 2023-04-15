



Ting der kan undersøges:
Hvordan at én slags crash er predominant i forskellige områder. Det kunne være seriøse crash, antallet af biler involveret, typer af biler involveret etc.




Vi kan tilføje traffic volumen (antagelse), og det kan hjælpe med:
at verificere hypotesen om at høj volume fører til flere uheld



# Video requirements (from the course website)

An explanation of the central idea behind your final project, e.g. think about questions such as;
- What is the idea?
> Vi vil gerne undersøge hvordan at sikkerheden på vejene i NYC har udviklet sig gennem årene, og hvordan at sikkerheden kan forbedres.
- Which datasets do you need to explore the idea?,
> Vi har allerede fundet to datasets som vi vil bruge til at undersøge vores ide. Disse er traffic crashes og vejret.
>> Traffic crashes: Indeholder information omkring crashes i NYC. Det er en stor dataset, og det indeholder information omkring tidspunkt, antal biler involveret, type af biler, borough, og andre ting.

>> Vejret: Indeholder information omkring vejret i de forskellige boroughs.
- Why is it interesting?
> Det er interessant fordi at sikkerheden på vejene er vigtig for alle, og det er vigtigt at undersøge hvordan at sikkerheden kan forbedres.



A mock up of the visualization that you wish to build. (Anything is fine here. Pen and paper, MS Paint, Inkscape, D3, anything.).

- What is the visualization?

Vi vil gerne lave følgende plots:
> Time series plot - se udviklingen af antallet af crashes; kan være grupperet på borough, seriøsitet (antal døde/skadede), vejrtype (diskretisering af vejret)

> Cloropleth map - se hvilke crossings/lyskryds der er mest dødelige gennem årene og gå i dybden med dette -> måske endda finde nyhedsartikler der forklarer hvordan at sikkerheden forbedres. Herigennem kan vi øge sikkerheden ved at anbefale specifikke kritiske lyskryds.

>Polar plot - se hvordan at fatality rate afhænger af døgn og ugedag?

Make sure you answer the questions;

- What genre is it? (for Genres, see section 4.3 of the Segel and Heer paper)
- Why is that genre right for telling the story you want to communicate with the data
- A walk-through of your preliminary data-analysis, addressing
- What is the total size of your data? (MB, number of rows, number of variables, etc)
- What are other properties? (What is the date range? Is is it geo-data?, then a quick plot of locations, etc.)
- Show the fundamental distributions of the data (similar to the work we did on SF crime data for lecture 3)



## Storyline

### Formål: (10 sec)
Vi vil gerne undersøge hvordan at sikkerheden på vejene i NYC har udviklet sig gennem årene, og hvordan at sikkerheden kan forbedres.

### Hvordan vil vi gøre det? (25 sec)

Vi vil belyse følgende spørgsmål:
- Hvordan har udviklingen af dødelige ulykker udviklet sig gennem årene? (Time series plot grupperet på alvorlighed af ulykke)
- Hvilke typer ulykker er mest hyppige?
- Hvilke tidspunkter er mest dødelige? ()
- Hvilke lyskryds er mest dødelige? (cloropleth map)
- Hvordan påvirker vejrforholdene antallet af dødelige ulykker? (Time series: antal ulykker vs vejrforhold)



### Hvordan kan vi svare på det? (15 sec)
Data:
- Traffic data
- Vejr data

Show fundamental distributions of the data, and other information about the data.


### Hvordan vil vi formidle det?  (10 sec)
- Hjemmeside der følger `Magazine` genre med flere faner og interaktive plots.
