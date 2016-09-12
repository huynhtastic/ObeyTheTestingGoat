# ObeyTheTestingGoat
Testing repo to follow exercises in "ObeyTheTestingGoat" by Harry J.W. Percival

Starting from Chapter 7, I am including a section in the README for reflections. This is to really ensure and dig the concepts deep instead of just mindlessly reading the book and following instructions. 

### Chapter 7L Getting to the Minimum Viable State

TDD is closely associated with MVPs; avoid lengthy requirements gathering and building; build ASAP with feedback and reiterate
YAGNI - you ain't gonna need it; avoid building things that we won't need; avoid adding complexity of unused code
REST - Representational State Transfer; URL structure to match data structure

#### Creating FTs
 1. Write a FT
 2. Does the FT pass? {
 	Yes: go to 3
 	No: Create a UT
 }
 3. Does the app need refactoring? {
 	Yes: Create a UT
 	No: Create a new FT
 }

#### Creating UTs
 1. Write a UT
 2. Does the UT pass? {
 	Yes: go to 3
 	No: go to 4
 }
 3. Does the app need refactoring? {
 	Yes: go to 4
 	No: go to 2 for FT
 }
 4. Write code and go to 2

#### Red/Green/Refactor
 1. Write a small amount code tests and see it fail (RED)
 2. Write a small amount of production code to see it pass (GREEN)
 3. Rewrite the code and see how you can improve it (REFACTOR)

Test Isolation and Global State - tests should not affect each other
Working State to Working State - don't fix everything at once; fix little bits at a time and ensure all code is still passing tests within refactors