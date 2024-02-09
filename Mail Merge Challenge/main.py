#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

letter_file = open("/Users/PRIYASHA/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt")
contents = letter_file.read()



file = open("/Users/PRIYASHA/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt","r")
name_list = file.readlines()

for name in name_list:
    stripped_name = name.strip()
    new_letters = contents.replace("[name]", stripped_name)
    with open (f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letters:
        completed_letters.write(new_letters)






    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
