answers = []
grade = 'poor'
while grade == 'poor' or grade == 'regular' or grade == 'great':
     print('\nThank you for visiting the Movie Theater.\nPlease complete our quality survey.')
     grade = input('Rate the quality of the service provided in: "poor", "regular" or "great":\n')
     if grade == 'poor' or grade == 'regular' or grade == 'great':
         answers.append(grade)
         p = answers.count('poor')
         rg = answers.count('regular')
         g = answers.count('great')
poor = (p / len(answers)) * 100
regular = (rg / len(answers)) * 100
great = (g / len(answers)) * 100
print(f'\n{len(answers)} answered the survey, with {poor}% answering poor, {regular} answering regular and {great} answering great.')
