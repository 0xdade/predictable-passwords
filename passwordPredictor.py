'''
Really basic wordlist generation using a password base, such as the company name or ticker symbol or something.
"People Pick Predictably Poor Passwords" - Password Policy Pessimist, preaching practical password politics
'''
import sys
import datetime
import itertools

specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', ',', '.', '/', '?', ';', ':', '+', '=', '-', '(', ')', '~', '`', '|', '<', '>']
#specialChars = [''] # Uncomment if your target doesn't require special characters

now = datetime.datetime.now()

'''
If I ever finish this, I'll replace common 1337 characters to that misguided sense of complexity
'''
def strReplace():
	
	replaceChars = {
					'a' : ['@', '4'],
					'e' : ['3'],
					'i' : ['1', '|'],
					'o' : ['0'],
					'l' : ['1', '|'],
					's' : ['$', '5'],
					't' : ['7']
					}
	
	return

'''
Some keyboard patterns might be useful to try, someday
'''
def keyboardPatterns():
	patterns = [
				'qwerty',
				'uiop',
				'asdf',
				'zxcv',
				'123456',
				'12345',
				'1234',
				'123',
				';lkj',
				'jkl;',
				]
	return

def getYear():
	return [str(datetime.datetime.now().year)]

def getSeasons():
	seasons = []
	for season in ['spring', 'summer', 'fall', 'winter']:
		seasons.append(season.title())
		seasons.append(season)
	return seasons

def getMonth():
	return [now.strftime('%b'), now.strftime('%B'), now.strftime('%b').lower(), now.strftime('%B').lower()]

def main():
	targetBase = [sys.argv[1]]
	targetBase.append(sys.argv[1].title())
	likelyPermutations = [[targetBase, getMonth(), getYear(), specialChars], 
					[targetBase, getSeasons(), getYear(), specialChars],
					[getMonth(), getYear(), targetBase, specialChars], 
					[getSeasons(), getYear(), targetBase, specialChars], 
					]
	for perm in likelyPermutations:
		for item in list(itertools.product(*perm)):
			print ''.join(item)

if __name__ == '__main__':
	main()
