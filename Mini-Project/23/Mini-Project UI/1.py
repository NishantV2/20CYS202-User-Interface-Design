def menu():
        print("------- Indian Premier League Scheduler !---------")
        print("0.Exit")
        print("1.View IPL Teams")
        print("2.View Team Players")
        print("3.View Match Scheduling")
        print("4.View Details of your Favourite Team")
        print("5. View Stadiums")

def ipl_teams():
        print("1. Chennai Super Kings (CSK)")
        print("2. Mumbai Indians (MI)")
        print("3. Royal Challengers Bangalore (RCB)")
        print("4. Sunrisers Hyderbad (SRH)")
        print("5. Kolkata Knight Riders (KKR)")
    
def team_players():
    team = input("Enter the Team Name:")
    if(team == 'CSK' or team == 'Chennai Super Kings'):
        print("1.  MS Dhoni (Captain + Wicket Keeper)")
        print("2.  Ravindra Jadeja (All - Rounder)")
        print( "3.  Ruturaj Gaikwad (Batter)")
        print( "4.  Deepak Chahar (Bowler)")
        print( "5.  Ambati Rayudu (Batter)")
        print( "6.  Robin Uthappa (All Rounder + Wicket Keeper)")
        print("7.  Moeen Ali (All Rounder)")
        print("8.  Shivam Dube (Bowler)")
        print( "9.  KM Asif (Bowler)")
        print("10. Devon Conway ( Batter)")
        print("11. Narayan Jagadeesan (Batter)")
    elif(team == 'Mumbai Indians' or team == 'MI' or team == 'Mi'):
        print("1.  Rohit Sharma (Captain+ Batter )")
        print("2.  Suryakumar Yadav (Bater) ")
        print("3.  Tim David (Batter)")
        print("4.  Tilak Varma (Batter)")
        print("5.  Ramandeep Singh (All Rounder) ")
        print("6.  Rahul Buddhi (All Rouder) ")
        print("7.  Daniel Sams (Bowler)")
        print("9.  Dewald Brevis (All ROnder) ")
        print("10. Aryan Juyal (Wicket Keper) ")
        print("11. Ishan Kishan (Batter  Wicket Keeper) ")
        print("12. Jasprit Bumrah (Bowle) ")
    elif(team == 'Royal Challengers Bangalore' or team == 'RCB' or team == 'Rcb'):
        print("1.Virat Kolhi (Batter)")
        print("2.Harshal Patel (All-Rouner) ")
        print("3.Dinesh Karthik (Wicket-keeper) ")
        print("4.Mohammed Siraj (Bowler)")
        print("5.Maxwell (Batter) ")
        print("7.Josh Hazelwood (owler ")
        print("8.Anuj Rawat (Wicket-Keepr, All- Rounder) ")
        print("9.David Willey (Batter)")
        print("10.Siddharth Kaul (Bowler)")
        print("11.Finn Allen (Batter)")
    elif(team == 'Sunrisers Hyderbad' or team == 'SRH' or team == 'Srh'):
        print("1. Washington Sundar (Bower + All Rounder)")
        print("2. Bhuvneshwar Kumar (Capain + Bowler)")
        print("3. Kartik Tyagi (Bowler)")
        print("4. T Natarajan (Bowler + All Rounder)")
        print("5. Umran Malik (Bowler)")
        print("6. Fazalhaq Farooqi (All rounder)")
        print("7. Marco Jansen (Batter)")
        print("8. Abishek Sharma (Batter")
        print("9. Glenn Phillips (All Ronder + Batter")
        print("10.Rahul Tripathi (Batter)")
        print("11.Aiden Markram (Batter)")
    elif(team == 'Kolkata Knight Riders' or team == 'KKR' or team == 'Kkr'):
        print("1. Shreyas Iyer (Batter +Captain)")
        print("1. Rinku Singh (Batter)")
        print("1. Nitish Rana (Batter)")
        print("1. Anukul Roy (Bowler)")
        print("1. Andre Russell (All Rouder)")
        print("1. Venkatesh Iyer (All Ronder)")
        print("1. Umesh Yadav (Batter)")
        print("1. Harshit Rana (Bowler)")
        print("1. Tim Southee (Bowler)")
        print("1. Varun Chakaravarthy (Al Rounder)")
        print("1. Sunil Narine (Batter +All Rounder)")


def schedule():
    print("Match No : 1 " "Date : 25/03/2022" "Mumbai Indians VS Chennai Super Kings " "Location : Wankhede Staidum " "Time : 20:00 IST")
    print("Match No : 2 " "Date : 26/03/2022" "Royal Challengers Bangalore VS Sunrisers Hyderbad " "Location : Chinnaswamy Stadium " "Time : 20:00 IST")
    print("Match No : 3 " "Date : 27/03/2022" "Chennai Super Kings VS Kolkata Knight Riders " "Location : Eden Gardens " "Time : 20:00 IST")
    print("Match No : 4 " "Date : 28/03/2022" "Mumbai Indians VS Royal Challengers Bangalore " "Location : Arun Jaitley Stadium " "Time : 20:00 IST")
    print("Match No : 5 " "Date : 29/03/2022" "Sunrisers Hyderbad VS Kolkata Knight Riders " "Location : Chidambaram Stadium " "Time : 20:00 IST")
    print("Match No : 6 " "Date : 31/03/2022" "Mumbai Indians VS Kolkata Knight Riders " "Location : Chidambaram Stadium " "Time : 20:00 IST")
    print("Match No : 7 " "Date : 01/04/2022" "Chennai Super Kings VS Sunrisers Hyderbad " "Location : Eden Garden" "Time : 16:00 IST")
    print("Match No : 8 " "Date : 01/04/2022" "Royal Challengers Bangalore VS Kolkata Knight Riders " "Location : Wankhede Stadium" "Time : 20:00 IST")
    print("Match No : 9 " "Date : 02/04/2022" "Mumbai Indians  VS Sunrisers Hyderbad " "Location : Eden Garden" "Time : 20:00 IST")
    print("Match No : 10 " "Date : 03/04/2022" "Chennai Super Kings  VS Royal Challengers Bangalore " "Location : Chinnaswamy Stadium" "Time : 20:00 IST")

def bro():
    team = input("Enter the team name: ")
    if(team == 'CSK' or team == 'Chennai Super Kings' or team=='Csk'):
        print("Match No : 1 " "Date : 25/03/2022" "Mumbai Indians VS Chennai Super Kings " "Location : Wankhede Staidum " "Time : 20:00 IST")
        print("Match No : 3 " "Date : 27/03/2022" "Chennai Super Kings VS Kolkata Knight Riders " "Location : Eden Gardens " "Time : 20:00 IST")
        print("Match No : 7 " "Date : 01/04/2022" "Chennai Super Kings VS Sunrisers Hyderbad " "Location : Eden Garden" "Time : 16:00 IST")
        print("Match No : 10 " "Date : 03/04/2022" "Chennai Super Kings  VS Royal Challengers Bangalore " "Location : Chinnaswamy Stadium" "Time : 20:00 IST")

    elif(team in ['Mumbai Indians','MI','Mi']):
        print("Match No : 1 " "Date : 25/03/2022" "Mumbai Indians VS Chennai Super Kings " "Location : Wankhede Staidum " "Time : 20:00 IST")
        print("Match No : 4 " "Date : 28/03/2022" "Mumbai Indians VS Royal Challengers Bangalore " "Location : Arun Jaitley Stadium " "Time : 20:00 IST")
        print("Match No : 6 " "Date : 31/03/2022" "Mumbai Indians VS Kolkata Knight Riders " "Location : Chidambaram Stadium " "Time : 20:00 IST")
        print("Match No : 9 " "Date : 02/04/2022" "Mumbai Indians  VS Sunrisers Hyderbad " "Location : Eden Garden" "Time : 20:00 IST")

    elif(team in ['Sunrisers Hyderbad','SRH','Srh']):
    
        print("Match No : 2 " "Date : 26/03/2022" "Royal Challengers Bangalore VS Sunrisers Hyderbad " "Location : Chinnaswamy Stadium " "Time : 20:00 IST")
        print("Match No : 5 " "Date : 29/03/2022" "Sunrisers Hyderbad VS Kolkata Knight Riders" "Location : Chidambaram Stadium " "Time : 20:00 IST")
        print("Match No : 7 " "Date : 01/04/2022" "Chennai Super Kings VS Sunrisers Hyderbad " "Location : Eden Garden" "Time : 16:00 IST")
        print("Match No : 9 " "Date : 02/04/2022" "Mumbai Indians  VS Sunrisers Hyderbad " "Location : Eden Garden" "Time : 20:00 IST")
        
    elif(team == 'Royal Challengers Bangalore' or team == 'RCB' or team =='Rcb'):
        print("Match No : 2 " "Date : 26/03/2022" "Royal Challengers Bangalore VS Sunrisers Hyderbad " "Location : Chinnaswamy Stadium " "Time : 20:00 IST")
        print("Match No : 4 " "Date : 28/03/2022" "Mumbai Indians VS Royal Challengers Bangalore " "Location : Arun Jaitley Stadium " "Time : 20:00 IST")
        print("Match No : 8 " "Date : 01/04/2022" "Royal Challengers Bangalore VS Kolkata Knight Riders " "Location : Wankhede Stadium" "Time : 20:00 IST")
        print("Match No : 10 " "Date : 03/04/2022" "Chennai Super Kings  VS Royal Challengers Bangalore " "Location : Chinnaswamy Stadium" "Time : 20:00 IST")

    elif(team == 'Kolkata Knight Riders' or team == 'KKR' or team == 'Kkr'):
        print("Match No : 3 " "Date : 27/03/2022" "Chennai Super Kings VS Kolkata Knight Riders " "Location : Eden Gardens " "Time : 20:00 IST")
        print("Match No : 5 " "Date : 29/03/2022" "Sunrisers Hyderbad VS Kolkata Knight Riders" "Location : Chidambaram Stadium " "Time : 20:00 IST")
        print("Match No : 6 " "Date : 31/03/2022" "Mumbai Indians VS Kolkata Knight Riders " "Location : Chidambaram Stadium " "Time : 20:00 IST")
        print("Match No : 8 " "Date : 01/04/2022" "Royal Challengers Bangalore VS Kolkata Knight Riders " "Location : Wankhede Stadium" "Time : 20:00 IST")

    else:
        print("Enter a Valid Team")




while(True):
    menu()
    choice = int(input())
    if(choice == 1):
        ipl_teams()

    elif(choice == 2):
        team_players()

    elif(choice == 3):
        schedule()

    elif(choice==4):
        bro()
         

    elif(choice == 5):
        print("S No \t" "Stadium Name \t" "Location\t\n")
        print("1.\t" "Chidambaram Stadium\t" "Chennai\t\n")
        print("2.\t" "Eden Gardens\t" "Kolkata\t\n")
        print("3.\t" "Wankhede Stadium\t" "Mumbai\t\n")
        print("4.\t" "Chinnaswamy Stadium\t" "Bengaluru\t\n")
        print("5.\t" "Arun Jaitley Stadium\t" "Delhi\t\n")

    elif(choice == 0):
        print("Thank You")
        break  
    else:
        print("Enter a valid choice")
     