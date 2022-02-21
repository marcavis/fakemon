#!/usr/bin/python3
from PIL import Image

class Character:
	def __init__(self):
		self.name = ""
		self.owner = " "
		self.gender = "female"
		self.stats = [0, 0, 0, 0, 0, 0]
		self.types = ["normal"]
		self.moves = [0, 0, 0, 0]
		self.moves[0] = ["normal", "tackle", 40]
		
		self.ability = "NOTHING"
		self.abText = ["Does nothing.", "", ""]
		
		self.custom = ["Does nothing.", ""]
		self.customPower = 0
		# leave accuracy at 0 if it never misses
		self.customAccuracy = 0
		
		
char = Character()
char.name = "LUCILLE R"
char.owner = "MARCAVIS, FRISKY"
char.gender = "herm"
char.stats = [110, 100, 90, 50, 70, 60]
char.types = ["fighting"]
char.moves[0] = ['steel', 'pin down']
char.moves[1] = ['rock', 'smack down']
char.moves[2] = ['fighting', 'bulk up']
char.moves[3] = ['fighting', 'superpower']
char.ability = "natural fitness"
char.abText[0] = "Recovers HP when its stats"
char.abText[1] = "are raised."
char.custom[0] = "Shoots an arrow that may"
char.custom[1] = "lower the foe's speed."
char.customPower = 75
char.customAccuracy = 95
char.hasArt = False

char.art = "art/" + char.name.lower() + ".png"

def draw(img, output, x, y):
	nr, ng, nb, na = img.split()
	imgMain = Image.merge("RGB", (nr, ng, nb))
	imgMask = Image.merge("L", (na,))
	output.paste(imgMain, (x, y), imgMask)

def repaint(img, fontColor, fontShadowColor):
	imgData = img.getdata()
	newImg = []
	for item in imgData:
		if item == (0, 0, 0, 255):
			newImg.append(fontColor)
		elif item == (208, 208, 200, 255):
			newImg.append(fontShadowColor)
		else:
			newImg.append(item)
	img.putdata(newImg)
	return img

types = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost',
		 'steel', '???', 'fire', 'water', 'grass', 'electric', 'psychic',
		 'ice', 'dragon', 'dark', 'fairy']
typeDict = dict(zip(types, range(len(types))))

genders = ['herm', 'male', 'female']
genderDict = dict(zip(genders, range(len(genders))))

typePage = Image.open("src/fakemon7.png")
statsPage = Image.open("src/fakemon8.png")
movesPage = Image.open("src/fakemon9.png")
customMovePage = Image.open("src/movethis.png")
numberFont = Image.open("src/numbers.png")
letterFont = Image.open("src/letters.png")
minusFont = Image.open("src/small.png")
typeFont = Image.open("src/types.png")
genderFont = Image.open("src/gender.png")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-.,'"
minusAlphabet = "abcdefghijklmnopqrstuvwxyz-.,'"
alp = dict([(x, alphabet.find(x)) for x in alphabet])
alp2 = dict([(x, minusAlphabet.find(x)) for x in minusAlphabet])

statsPos = [0] * 6
statsPos[0] = (168, 60) #HP
statsPos[1] = (168, 76) #ATK
statsPos[2] = (168, 92) #DEF
statsPos[3] = (230, 60) #SPA
statsPos[4] = (230, 76) #SPD
statsPos[5] = (230, 92) #SPE

movesPos = [0] * 4
movesPos[0] = (120, 36)
movesPos[1] = (120, 52)
movesPos[2] = (120, 68)
movesPos[3] = (120, 84)

moveTypesPos = [0] * 4
moveTypesPos[0] = (85, 32)
moveTypesPos[1] = (85, 48)
moveTypesPos[2] = (85, 64)
moveTypesPos[3] = (85, 80)

for i in range(6):
	#turn stats into strings
	stat = str(char.stats[i])
	pos = 0
	for j in stat[::-1]:
		thisNum = numberFont.crop((0+(int(j)*6), 0, 6+(int(j)*6), 10))
		draw(thisNum, statsPage, statsPos[i][0] + (6*pos), statsPos[i][1])
		pos = pos - 1
		
for i in range(4):
	#print moves
	#fontcolor - from 0,0,0 to 248,248,248;
	#fontshadowcolor - from 208, 208, 200 to 96, 96, 96
	type = char.moves[i][0].lower()
	move = char.moves[i][1]
	pos = 0
	kern = 0
	thisType = typeFont.crop((0 + (typeDict[type] * 32), 0, 32 + (typeDict[type] * 32), 16))
	draw(thisType, movesPage, moveTypesPos[i][0], moveTypesPos[i][1])
	for j in move.upper():
		if j == ' ':
			kern += 3
			continue
		thisLet = letterFont.crop((0+(alp[j]*6), 0, 6+(alp[j]*6), 12))
		thisLet = repaint(thisLet, (248, 248, 248, 255), (96, 96, 96, 255))
		draw(thisLet, movesPage, movesPos[i][0] + (6 * pos) + kern, movesPos[i][1])
		pos = pos + 1

#print types and ability
type1 = typeDict[char.types[0].lower()]
thisType = typeFont.crop((0 + (type1 * 32), 0, 32 + (type1 * 32), 16))
draw(thisType, typePage, 120, 48)
if len(char.types) == 2:
	type2 = typeDict[char.types[1].lower()]
	thisType = typeFont.crop((0 + (type2 * 32), 0, 32 + (type2 * 32), 16))
	draw(thisType, typePage, 152, 48)
	
pos = 0
kern = 0
for j in char.ability.upper():
	if j == ' ':
		kern += 3
		continue
	thisLet = letterFont.crop((0 + (alp[j] * 6), 0, 6 + (alp[j] * 6), 12))
	thisLet = repaint(thisLet, (248, 248, 248, 255), (96, 96, 96, 255))
	draw(thisLet, typePage, 88 + (6 * pos) + kern, 76)
	pos = pos + 1


for i in range(3):
	pos = 0
	kern = 0
	for j in char.abText[i]:
		if j == ' ':
			kern += 3
			continue
		if j.islower():
			thisLet = minusFont.crop((0 + (alp2[j] * 6), 0, 6 + (alp2[j] * 6), 12))
		else:
			thisLet = letterFont.crop((0 + (alp[j] * 6), 0, 6 + (alp[j] * 6), 12))
		draw(thisLet, typePage, 88 + (6 * pos) + kern, 92 + (i * 16))
		pos = pos + 1
		if j in 'il.,':
			kern -= 2
		if j in 'rj':
			kern -= 1

#draw name
pos = 0
kern = 0
for j in char.name.upper():
	if j == ' ':
		kern += 3
		continue
	thisLet = letterFont.crop((0 + (alp[j] * 6), 0, 6 + (alp[j] * 6), 12))
	thisLet = repaint(thisLet, (248, 248, 248, 255), (96, 96, 96, 255))
	draw(thisLet, typePage, 8 + (6 * pos) + kern, 100)
	draw(thisLet, typePage, 14 + (6 * pos) + kern, 116)
	draw(thisLet, statsPage, 8 + (6 * pos) + kern, 100)
	draw(thisLet, statsPage, 14 + (6 * pos) + kern, 116)
	draw(thisLet, movesPage, 8 + (6 * pos) + kern, 100)
	draw(thisLet, movesPage, 14 + (6 * pos) + kern, 116)
	pos = pos + 1

#draw sex/gender
gender = genderFont.crop((0 + (genderDict[char.gender] * 16), 0, 16 + (genderDict[char.gender] * 16), 11))
draw(gender, typePage, 60, 131)
draw(gender, statsPage, 60, 131)
draw(gender, movesPage, 60, 131)

#draw owner
pos = 0
kern = 0
for j in char.owner:
	if j == ' ':
		kern += 3
		continue
	thisLet = letterFont.crop((0 + (alp[j] * 6), 0, 6 + (alp[j] * 6), 12))
	thisLet = repaint(thisLet, (248, 184, 176, 255), (208, 112, 104, 255))
	draw(thisLet, typePage, 106 + (6 * pos) + kern, 36)
	pos = pos + 1
	if j in '.,':
		kern -= 2

if char.hasArt:
	sprite = Image.open(char.art)
	draw(sprite, movesPage, 8, 32)
	draw(sprite, statsPage, 8, 32)
	draw(sprite, typePage, 8, 32)
	
typePage = typePage.resize((720,480), Image.NEAREST)
movesPage2 = movesPage
movesPage = movesPage.resize((720,480), Image.NEAREST)
statsPage = statsPage.resize((720,480), Image.NEAREST)
typePage.save("results/" + char.name + "_1type.png")
movesPage.save("results/" + char.name + "_3moves.png")
statsPage.save("results/" + char.name + "_2stats.png")

#print custom move description page
draw(customMovePage, movesPage2, 0, 0)

for i in range(2):
	pos = 0
	kern = 0
	for j in char.custom[i]:
		if j == ' ':
			kern += 3
			continue
		if j.islower():
			thisLet = minusFont.crop((0 + (alp2[j] * 6), 0, 6 + (alp2[j] * 6), 12))
		else:
			thisLet = letterFont.crop((0 + (alp[j] * 6), 0, 6 + (alp[j] * 6), 12))
		draw(thisLet, movesPage2, 86 + (6 * pos) + kern, 124 + (i * 16))
		pos = pos + 1
		if j in 'il.,':
			kern -= 2
		if j == 'rj':
			kern -= 1

#turn stats into strings
pow = str(char.customPower)
if pow == "0":
	thisLet = letterFont.crop((0 + (alp['-'] * 6), 0, 6 + (alp['-'] * 6), 12))
	draw(thisLet, movesPage2, 67, 124)
	draw(thisLet, movesPage2, 73, 124)
else:
	pos = 0
	for j in pow[::-1]:
		thisNum = numberFont.crop((0 + (int(j) * 6), 0, 6 + (int(j) * 6), 10))
		draw(thisNum, movesPage2, 73 + (6 * pos), 124)
		pos = pos - 1
		
acc = str(char.customAccuracy)
if acc == "0":
	thisLet = letterFont.crop((0 + (alp['-'] * 6), 0, 6 + (alp['-'] * 6), 12))
	draw(thisLet, movesPage2, 67, 140)
	draw(thisLet, movesPage2, 73, 140)
else:
	pos = 0
	for j in acc[::-1]:
		thisNum = numberFont.crop((0+(int(j)*6), 0, 6+(int(j)*6), 10))
		draw(thisNum, movesPage2, 73 + (6*pos), 140)
		pos = pos - 1


movesPage2 = movesPage2.resize((720,480), Image.NEAREST)
movesPage2.save("results/" + char.name + "_4custom.png")
fullPage = Image.new('RGB', (1440, 960))
fullPage.paste(typePage, (0,0))
fullPage.paste(statsPage, (720,0))
fullPage.paste(movesPage, (0,480))
fullPage.paste(movesPage2, (720,480))
fullPage.save("results/" + char.name + "_5all.png")