"""
* ask the questions......!
* also distribution of the proze will be held......!
* using the for loop for continue asking the questions...!
* there is a condition weather answer is true or not
* if it is true them this loop will continue otherwise this loop will be break

# """
# 1 : question.....!

questions= [['What is the capital of France?', 'Paris', 'London', 'Berlin', 'Madrid', 1],
            ['What is the largest planet in our solar system?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 3],
            ['What is the chemical symbol for gold?', 'Au', 'Ag', 'Fe', 'Pb', 1],
            ['What is the smallest prime number?', '1', '2', '3', '4', 2],

 ]

 prize= [10000,200000, 300000, 500000 ]
 i=0
 for question in questions:
    
    print(question[0])
     print(f'a.{question[1]}')
     print(f'b .{question[2]}')
     print(f' c.{question[3]}')
     print(f' d.{question[4]}')

     user= int(input("enter the input from the user: 1 for a, 2 for b, 3 for c, 4 for d"))
     if user==question[5]:
         print(f'coreect answer.........!')
         print(f' proze is: {prize[i]}')
     else:
         print(f' wrong answer try again next time.........!')
         break
     print(f'you won........!{prize[i]}')
     i+=1

# 2 : question....!

questions= [['what is the name of the person? ', 'riya', 'raghav', 'sharma', 'tuli', 2  ],
            ['what is capital of the farance? ', "paris", 'farance', 'delhi', 'mumbai', 1 ],
            ['what is the largest planet on this earth? ', 'earth', 'mars', 'jupiter', 'saturn', 3],
            ['what is the chemical symbol for gold? ', 'au', 'ag', 'fe', 'pb', 1],
            ['what is the smallest prime number? ', '1', '2', '3', '4', 2],
            ['what is the capital of india? ', 'delhi', 'mumbai', 'kolkata', 'banglore', 1],
            ['what is the capital of nepal? ', 'kathmandu', 'bhaktapur', 'lalitpur', 'pokhara', 1],
            ['what is the capital of bhutan? ', 'thimphu', 'paro', 'punakha', 'phuentsholing', 1],
            ['what is the capital of china? ', 'beijing', 'shanghai', 'guangzhou', 'shenzhen', 1],
            ['what is the capital of japan? ', 'tokyo', 'osaka', 'kyoto', 'nagoya', 1]
           
            
]
prizes= [1000, 2000,3000,4000,5000,6000,7000,8000,9000,10000]
i=0
for question in questions:
    print(question[0])
    print(f' a.{question[1]}')
    print(f' b.{question[2]}')
    print(f' c.{question[3]}')
    print(f' d.{question[4]}')

    user= int(input('enter the user input for the question: '))
    if user==question[5]:
        print(f' the answer is correct baby............{question[5]}')
        print(f' the winning prize is : {prizes[i]}')
    else:
        print('answer is wrong........!')
        print('try again next time baby............!')
        break
    print(f' you won: {prizes[i]}')
    i+=1
