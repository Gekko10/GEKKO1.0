#greeting
print('Hello, I am Gekko, a virtual AI tasked with telling your future,but first ill need some information.')
#info inputs
name = input('What is your name ? ')
age = input('What is your age ? ')
sex = input('Are you male, female or non-bianary ? ')
while sex.lower() not in ['male','female','non-binary','nonbianary','non bianary']:
      print(sex + ' is not a valid input.')
      print('Try again, you typed' + sex)
      sex = input('Are you male, female or non-bianary ? ')
orientation = input('Do you like men or women ? ')
while orientation.lower() not in ['men', 'women']:
      print(orientation +' is not a valid input.')
      print('Try again, ' + 'you typed '+ orientation)
      orientation = input('Do you like men or women ? ')
scale = input('On a scale of 1/10 how good looking would you say you are ? ')
      
# control flow for scale input
while not scale.isnumeric() or int(scale) > 10:
        if not scale.isnumeric():
         print('I said 1/10, numbers not letters bozo.')
         scale = input('Lets try again, On a scale of 1/10 how good looking would you say you are ? ')
        else:
         print('I said 1/10.')
         print(scale + ' is crazy lol.')
         scale = input('Lets try again, On a scale of 1/10 how good looking would you say you are ? ')

if int(scale) <= 10 :
          print('Scanning......')
          print('Thats generous.')
marital_status = input('Are you single or taken? ')
#control flow for marital status
while marital_status.lower() != 'taken' and marital_status.lower() != 'single':
    print('I didn\'t get that, try typing Single or Taken.')
    marital_status = input('Let\'s try again. Are you single or taken? ')
if marital_status.lower() == 'taken':
        print('Then there\'s hope for me yet!')
elif marital_status.lower() == 'single':
        rate = int(scale) / 2
        statement = 'Not surprised a solid ' + str(rate) + ' out of 10 is single even my standards are higher than that! '
        print(statement)

ssn = input('Lastly whats your SSN ? ')
while not ssn.isdigit() or len(ssn) != 9:
        print('SSN consist of numbers not letters or special characters and also must be 9 digits long, you typed, ' + ssn)
        ssn = input('what\'s your SSN ? ')
print('OMG! Dont give out that information dumbass!')
print('Calculating data....')
print('Calculated')
print('So '+ name+' age '+ age +' for which year would you like to know the future for')
year = input('')
while not year.isdigit() or len(year) != 4:
        print('Please use numbers to represent the year,be sure to incese year in format \'####\'')
        year = input('')
if int(year) <=2023 :
    print('Dawg thats the past nvm Goodbye')
if int(year) == 2024 and marital_status.lower() =='single':
   if sex.lower() == 'male' and orientation.lower() == 'women':
     print('HUH??? it would seem that you end up marring the man of your dreams, good for you for finally coming out the closet.')
     print('Lol lil bro switched sides.')
   elif sex.lower() == 'female' and orientation.lower() == 'man' or 'men':
       print('Girl now why when i looked at yo future i seen you licking on sum cat..........Is there something you want to tell me ?')
if int(year) == 2024 and marital_status.lower()== 'taken' : 
      if sex.lower() == 'male' and orientation.lower() == 'women':
            print('Sorry to tell you this but your significant other, she will get into a car accident in 2024, which will cause you to go into a deep depression and eventually.............')
            print('Anyway LOL XD.')
      elif sex.lower() == 'women' and orientation.lower() == 'men':
            print('Yea girl, soo you know that bitch he keep telling you was \'Just\' his best friend? well in 2024 they have a baby.')
            print('OOP !')

out_comes = [ "Well, well, well, you choose, " + year + " Prepare yourself for a groundbreaking revelation: your future involves not being bored out of your mind. I know, groundbreaking stuff. Get ready for the wild ride of... well, not complete mediocrity!", "Behold, the grand spectacle of year" + year + " unfolds.Yyou find yourself in a mundane yet strangely captivating scenario — waiting in line at the post office. Suddenly, something compels you to strike up a conversation with a person whose main talent seems to be discussing the riveting world of postage stamps. This peculiar encounter will leave you questioning both the mysteries of the universe and your life choices. Your new hobby becomes collecting post stamps.",'For some reason I cant see that far into your future weird', "In " + year + ' a truly exceptional event awaits. You, adorned in the latest fashion-forward potato sack (fashion trends are subjective, after all), find yourself in the peculiar scenario of a \'Potato Sack Fashion Show.\' As you strut down the makeshift runway, the crowd erupts and serverly \'Boo\'s\' you off the stage. tramatizingly unforgettable and extreamly embarrasing, even your pet rock will be rolling with laughter. Oh yea you got a pet rock. ',  "Behold the wonders of the year " + year + ' ! You are in the heart of a gripping saga, where you accidentally discover your latent talent for extreme ironing. Yes, extreme ironing — the sport that combines the thrill of adventure with the satisfaction of wrinkle-free clothing. Get ready for an adrenaline-pumping quest to iron your garments in the most absurd and dangerous locations. Who knew domestic chores could be this riveting?.']
import random
if int(year) >= 2024 :

    print(random.choice(out_comes))
            

input('')


        
    