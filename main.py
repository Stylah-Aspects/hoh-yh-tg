from tkinter import * #this will let me use the widget for my GUI
import random

global questions_answers
names_list = []
asked = []
score = 0

questions_answers = {
  1: ["What must you do when you see blue and red flashing lights behind you?", "Speed up and get out of the way", "Slow down and drive carefully", "Slow down and stop", "Drive on as usual", "Slow down and stop", 3],
  2: ["You may stop on the motorway only:" , "if there is an emergency" , "To let off or pick up passengers" , "to make a U-turn" , "to stop and take a photo" , "if there is an emergency" , 1],
  3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?" , "Speed up before pedestrians cross" , "Stop and give way to pedestrains on any part of the crossing" , "Sound the horn on your vehicle to warn the pedestrians" , "Slow down to 30kmh" ,  "Stop and give way to pedestrains on any part of the crossing" , 2],
  4: ["Can you stop on a bus stop in a private motor vehicle?", "Only between midnight and 6am" , "Under no circumstances" , "When dropping off passengers" , "Only if it is less than 5 minutes" , "Under no circumstances" , 2],
  5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted (km/h)?" , "70km/h" , "100km/h so you do not hold up traffic" , "80km/h and if the wheel spacer displays a lower limit that applies" , "90km/h" , "80km/h and if the wheel spacer displays a lower limit that applies" , 3],
  6: ["When following another vehicle on a dusty road, you should:" , "Speed up to get past" , "Turn your vehicle's windscreen wipers on" , "Stay back from the dustcloud" , "Turn your vehicle's headlights on" , "Stay back from the dustcloud" , 3],
  7: ["What does the sign containing the letters 'LSZ' mean?" , "Low safety zone" , "Low stability zone" , "Lone star zone" , "Limited speed zone" , "Limited speed zone" , 4],
  8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?" , "20km/h" , "30km/h" , "70km/h" , "10km/h", "20km/h", 1],
  9: ["What is the maximum distance a load may extend in front of a car?" , "2 metres forward of the front edge of the front seat", "4 metres forward of the front edge of the front seat" , "3 metres forward of the front edge of the front seat", "2.5 metres forward of the front edge of the front seat" , "3 metres forward of the front edge of the front seat" , 3],
  10: ["To avoid being blinded by the headlights of another vehicle coming towards you, what should you do?" , "Look to the left of the road" , "Look to the centre of the road" , "Wear sunglasses that have sufficient strength" , "Look to the right side of the road" , "Look to the left of the road" , 1],
}

def randomiser():
  global qnum 
  qnum = random.randint (1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

class QuizStarter:
 def __init__(self, parent):
   background_color = "mint cream"
   #Frame set up
   self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
   self.quiz_frame.grid()#table like structure for the grid
  
   #Create a label widget for the heading
   #widgets goes below
   self.heading_label=Label(self.quiz_frame, text="NZ Road Rules", font=("Helvitica","20","bold"), foreground = 'white', bg= 'light blue') #using label for text
   self.heading_label.grid(row=0, padx=20) 
   self.var1=IntVar() #holds value of radio buttons
   #label for username
   self.user_label=Label(self.quiz_frame, text="Please enter your name below: ", font=("Tw Cen MT","14"),bg=background_color)
   self.user_label.grid(row=1, padx=20, pady=20) 
        
   #entry box
   self.entry_box=Entry(self.quiz_frame)
   self.entry_box.grid(row=2,padx=20, pady=20)
   #continue button
   self.continue_button = Button(self.quiz_frame, text="Continue", font=("Tw Cen MT", "12", 'bold'), foreground = 'white', bg="light blue", cursor = 'hand2', activebackground='lavender', command=self.name_collection)
   self.continue_button.grid(row=3,  padx=20, pady=20)        
        
    #image
    #logo = PhotoImage(file="road.gif")
    #self.logo = Label(self.quiz_frame, image=logo)  
    #self.logo.grid(row=4,padx=20, pady=20)

 def name_collection(self):
    name=self.entry_box.get()
    names_list.append(name) #add name to names list declared at the beginning
    self.quiz_frame.destroy()#destroy the starter
    Quiz(root)#Now in part 3 we will create a new class Quiz #and create an instance of it after we get the name, we #destroy starter the quiz_frame and open the questions #quiz_frame instead which will be part of the Quiz object

class Quiz:
  def __init__(self, parent):
    #colour selections
    background_color= "linen"
    self.quiz_frame=Frame(parent , bg=background_color , padx=100, pady=100)
    self.quiz_frame.grid()

    randomiser()

    #question
    self.question_label=Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Helvitica","16", "bold"), foreground = 'white', bg= 'sandy brown')
    self.question_label.grid(row=1 , padx=20 , pady=20)

   #holds value of radio buttons
    self.var1=IntVar()

    #radio button 1
    self.rb1= Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=1, padx=10, pady=10, variable=self.var1, background = "peach puff", activebackground='sandy brown', cursor = 'hand2')
    self.rb1.grid(row=3, sticky=W)

    #radio button 2
    self.rb2 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=2, padx=10, pady=10, variable=self.var1, background = "peach puff", activebackground='sandy brown', cursor = 'hand2')
    self.rb2.grid(row=5, sticky=W)

    #radio button 3
    self.rb3=Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=3, padx=10, pady=10, variable=self.var1, background = "peach puff", activebackground='sandy brown', cursor = 'hand2')
    self.rb3.grid(row=7, sticky=W)

    #radio button 4
    self.rb4=Radiobutton(self.quiz_frame, text=questions_answers[qnum][4], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=4, padx=10, pady=10, variable=self.var1, background = "peach puff", activebackground='sandy brown', cursor = 'hand2')
    self.rb4.grid(row=9, sticky=W)

    #confirm button
    self.confirm_button= Button(self.quiz_frame , text="Confirm", font=("Helvetica", "12", "bold"), foreground = 'white', bg="sandy brown", cursor = 'hand2', command=self.test_progress)
    self.confirm_button.grid(row=10)

    #Score label to show score (test result so far)
    self.score_label=Label(self.quiz_frame, text="Score:", font=("Helvitica", "14"), bg=background_color)
    self.score_label.grid(row=11, pady=1)

  #Method for editing the question label and radio buttons to the next questions data.
  def questions_setup(self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])
    
  #This is the method that would get invoked when confirm answer button is clicked, to take care of progress.
  def test_progress(self):
    global score
    scr_label = self.score_label
    choice = self.var1.get()
    if len(asked)>9: #If the question is last.
      if choice == questions_answers[qnum][6]: #If the last question is right anwers.
        score +=1
        scr_label.configure(text=score)
        self.confirm_button.config(text="Confirm")
      else: #If last question is wrong answer.
        score+=0
        scr_label.configure(text="The correct answer was " + questions_anwers[qnum][5])
        self.confirm_button.config(text="Confirm")
    else: #If it's not the last question.
      if choice==0: #Check if the user has made a choice.
        self.confirm_button.config(text="Try again please, you didn't select anything")
        choice=self.var1.get()
      else: #If they made a choice and it's not last question.
        if choice==questions_answers[qnum][6]: #If their choice is right.
          score+=1
          scr_label.configure(text=score)
          self.confirm_button(text="Confirm")
          self.questions_setup() #Run this method to move to next question.
        else: #If the choice was wrong.
          score+=0
          scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5])
          self.confirm_button.configure(text="Confirm")
          self.questions_setup()


#********************#
if __name__ == "__main__": #checks name of file before running, it will only work if the name is actually name
 root = Tk() #create the window
 root.title("NZ Road Rules Quiz") #title of the window
 quiz_instance = QuizStarter(root) #Instantation, making an instance of the class Quiz
 root.mainloop() #Keep showing the window until we close it.