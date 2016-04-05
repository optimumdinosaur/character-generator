import characterGenerator
import Tkinter
import tkMessageBox
import random
import operator


test = characterGenerator.Character('Test', 20)


class theGUI(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.minsize(width=420, height=635)
		self.initialize()


	def initialize(self):
		self.grid()


		headerString = Tkinter.StringVar()
		self.headerLabel = Tkinter.Label(self, textvariable=headerString)
		self.headerLabel.grid(column=0, row=0, columnspan=3)
		headerString.set('Character Display')

		buildHeaderString = Tkinter.StringVar()
		buildHeaderLabel = Tkinter.Label(self, textvariable=buildHeaderString)
		buildHeaderLabel.grid(column=0, row=4)
		buildHeaderString.set('Build a Character:')

		self.nameString = Tkinter.StringVar()
		self.nameString.set('Name')
		nameEntryBox = Tkinter.Entry(self, textvariable=self.nameString)
		nameEntryBox.grid(column=1, row=4, columnspan=2)

		levelRangeString = Tkinter.StringVar()
		levelRangeString.set('Level Range:')
		levelRangeLabel = Tkinter.Label(self, textvariable=levelRangeString)
		levelRangeLabel.grid(column=0, row=5)
		levelMinString = Tkinter.StringVar()
		levelMinString.set('1')
		self.levelMinBox = Tkinter.Entry(self, width=3, textvariable=levelMinString)
		self.levelMinBox.grid(column=1, row=5, sticky=Tkinter.W)
		levelMaxString = Tkinter.StringVar()
		levelMaxString.set('20')
		self.levelMaxBox = Tkinter.Entry(self, width=3, textvariable=levelMaxString)
		self.levelMaxBox.grid(column=2, row=5, sticky=Tkinter.W)

		raceOptLabelString = Tkinter.StringVar()
		raceOptLabelString.set('Race Options: ')
		raceOptLabel = Tkinter.Label(self, textvariable=raceOptLabelString)
		raceOptLabel.grid(column=0, row=6)
		self.DwarfVar = Tkinter.IntVar()
		DwarfCheck = Tkinter.Checkbutton(self, text='Dwarf', onvalue=1, offvalue=0, variable=self.DwarfVar)
		DwarfCheck.grid(column=0, row=7)
		self.ElfVar = Tkinter.IntVar()
		ElfCheck = Tkinter.Checkbutton(self, text='Elf', onvalue=1, offvalue=0, variable=self.ElfVar)
		ElfCheck.grid(column=0, row=8)
		self.GnomeVar = Tkinter.IntVar()
		GnomeCheck = Tkinter.Checkbutton(self, text='Gnome', onvalue=1, offvalue=0, variable=self.GnomeVar)
		GnomeCheck.grid(column=0, row=9)
		self.HalfOrcVar = Tkinter.IntVar()
		HalfOrcCheck = Tkinter.Checkbutton(self, text='Half-Orc', onvalue=1, offvalue=0, variable=self.HalfOrcVar)
		HalfOrcCheck.grid(column=0, row=10)
		self.HalflingVar = Tkinter.IntVar()
		HalflingCheck = Tkinter.Checkbutton(self, text='Halfling', onvalue=1, offvalue=0, variable=self.HalflingVar)
		HalflingCheck.grid(column=0, row=11)
		self.HumanVar = Tkinter.IntVar()
		HumanCheck = Tkinter.Checkbutton(self, text='Human', onvalue=1, offvalue=0, variable=self.HumanVar)
		HumanCheck.grid(column=0, row=12)
		self.KoboldVar = Tkinter.IntVar()
		KoboldCheck = Tkinter.Checkbutton(self, text='Kobold', onvalue=1, offvalue=0, variable=self.KoboldVar)
		KoboldCheck.grid(column=0, row=13)

		classOptLabelString = Tkinter.StringVar()
		classOptLabelString.set('Class Options: ')
		classOptLabel = Tkinter.Label(self, textvariable=classOptLabelString)
		classOptLabel.grid(column=1, row=6, columnspan=2)
		self.BarbarianVar = Tkinter.IntVar()
		BarbarianCheck = Tkinter.Checkbutton(self, text='Barbarian', onvalue=1, offvalue=0, variable=self.BarbarianVar)
		BarbarianCheck.grid(column=1, row=7)
		self.FighterVar = Tkinter.IntVar()
		FighterCheck = Tkinter.Checkbutton(self, text='Fighter', onvalue=1, offvalue=0, variable=self.FighterVar)
		FighterCheck.grid(column=1, row=8)
		self.PaladinVar = Tkinter.IntVar()
		PaladinCheck = Tkinter.Checkbutton(self, text='Paladin', onvalue=1, offvalue=0, variable=self.PaladinVar)
		PaladinCheck.grid(column=1, row=9)
		self.RangerVar = Tkinter.IntVar()
		RangerCheck = Tkinter.Checkbutton(self, text='Ranger', onvalue=1, offvalue=0, variable=self.RangerVar)
		RangerCheck.grid(column=1, row=10)
		self.RogueVar = Tkinter.IntVar()
		RogueCheck = Tkinter.Checkbutton(self, text='Rogue', onvalue=1, offvalue=0, variable=self.RogueVar)
		RogueCheck.grid(column=1, row=11)
		self.CrusaderVar = Tkinter.IntVar()
		CrusaderCheck = Tkinter.Checkbutton(self, text='Crusader', onvalue=1, offvalue=0, variable=self.CrusaderVar)
		CrusaderCheck.grid(column=1, row=13)
		self.SwordsageVar = Tkinter.IntVar()
		SwordsageCheck = Tkinter.Checkbutton(self, text='Swordsage', onvalue=1, offvalue=0, variable=self.SwordsageVar)
		SwordsageCheck.grid(column=1, row=14)
		self.WarbladeVar = Tkinter.IntVar()
		WarbladeCheck = Tkinter.Checkbutton(self, text='Warblade', onvalue=1, offvalue=0, variable=self.WarbladeVar)
		WarbladeCheck.grid(column=1, row=15)
		self.BardVar = Tkinter.IntVar()
		BardCheck = Tkinter.Checkbutton(self, text='Bard', onvalue=1, offvalue=0, variable=self.BardVar)
		BardCheck.grid(column=2, row=7)
		self.BeguilerVar = Tkinter.IntVar()
		BeguilerCheck = Tkinter.Checkbutton(self, text='Beguiler', onvalue=1, offvalue=0, variable=self.BeguilerVar)
		BeguilerCheck.grid(column=2, row=8)
		self.DreadNecromancerVar = Tkinter.IntVar()
		DreadNecromancerCheck = Tkinter.Checkbutton(self, text='Dread Necromancer', onvalue=1, offvalue=0, variable=self.DreadNecromancerVar)
		DreadNecromancerCheck.grid(column=2, row=9)
		self.DruidVar = Tkinter.IntVar()
		DruidCheck = Tkinter.Checkbutton(self, text='Druid', onvalue=1, offvalue=0, variable=self.DruidVar)
		DruidCheck.grid(column=2, row=10)
		self.WarmageVar = Tkinter.IntVar()
		WarmageCheck = Tkinter.Checkbutton(self, text='Warmage', onvalue=1, offvalue=0, variable=self.WarmageVar)
		WarmageCheck.grid(column=2, row=11)
		self.ArdentVar = Tkinter.IntVar()
		ArdentCheck = Tkinter.Checkbutton(self, text='Ardent', onvalue=1, offvalue=0, variable=self.ArdentVar)
		ArdentCheck.grid(column=2, row=13)
		self.PsionVar = Tkinter.IntVar()
		PsionCheck = Tkinter.Checkbutton(self, text='Psion', onvalue=1, offvalue=0, variable=self.PsionVar)
		PsionCheck.grid(column=2, row=14)
		self.WilderVar = Tkinter.IntVar()
		WilderCheck = Tkinter.Checkbutton(self, text='Wilder', onvalue=1, offvalue=0, variable=self.WilderVar)
		WilderCheck.grid(column=2, row=15)


		self.generateButton = Tkinter.Button(self, text='Generate a Character', command=self.generateCharacter)
		self.generateButton.grid(column=0, row=16, columnspan=3)


		self.grid_columnconfigure(0,weight=1)
		self.resizable(True, True)
		self.update()
		self.geometry(self.geometry())


	# callback function for the generateButton
	# currently randomly selects race and class from all available options
	def generateCharacter(self):

		raceChoices = []
		if self.DwarfVar.get() == 1:
			raceChoices.append('Dwarf')
		if self.ElfVar.get() == 1:
			raceChoices.append('Elf')
		if self.GnomeVar.get() == 1:
			raceChoices.append('Gnome')
		if self.HalfOrcVar.get() == 1:
			raceChoices.append('Half-Orc')
		if self.HalflingVar.get() == 1:
			raceChoices.append('Halfling')
		if self.HumanVar.get() == 1:
			raceChoices.append('Human')
		if self.KoboldVar.get() == 1:
			raceChoices.append('Kobold')

		classChoices = []
		if self.ArdentVar.get() == 1:
			classChoices.append('Ardent')
		if self.BarbarianVar.get() == 1:
			classChoices.append('Barbarian')
		if self.BardVar.get() == 1:
			classChoices.append('Bard')
		if self.BeguilerVar.get() == 1:
			classChoices.append('Beguiler')
		if self.CrusaderVar.get() == 1:
			classChoices.append('Crusader')
		if self.DreadNecromancerVar.get() == 1:
			classChoices.append('Dread Necromancer')
		if self.DruidVar.get() == 1:
			classChoices.append('Druid')
		if self.FighterVar.get() == 1:
			classChoices.append('Fighter')
		if self.PaladinVar.get() == 1:
			classChoices.append('Paladin')
		if self.PsionVar.get() == 1:
			classChoices.append('Psion')
		if self.RangerVar.get() == 1:
			classChoices.append('Ranger')
		if self.RogueVar.get() == 1:
			classChoices.append('Rogue')
		if self.SwordsageVar.get() == 1:
			classChoices.append('Swordsage')
		if self.WarbladeVar.get() == 1:
			classChoices.append('Warblade')
		if self.WarmageVar.get() == 1:
			classChoices.append('Warmage')
		if self.WilderVar.get() == 1:
			classChoices.append('Wilder')

		print 'raceChoices ', raceChoices
		print 'classChoices ', classChoices

		raceChoice = random.choice(raceChoices)
		classChoice = random.choice(classChoices)

		print 'race: ', raceChoice
		print 'class: ', classChoice

		test.name = self.nameString.get()

		test.level = random.randint(int(self.levelMinBox.get()), int(self.levelMaxBox.get()))

		test.buildACharacter(raceChoice, classChoice)

		self.displayCharacter()

	def writeCharacter(self):
		test.writeCharacterToFile('{}.txt'.format(test.name))
		tkMessageBox.showinfo('Character Saved', 'Character successfully saved to {}.txt!'.format(test.name))

	def rollSkill(self):
		roll = random.randint(1,20)
		skillWithBonus = str(self.skillBox.get(Tkinter.ACTIVE))
		skillName = skillWithBonus[:skillWithBonus.index('+')]
		skillBonus = int(skillWithBonus[skillWithBonus.index('+'):])
		finalRoll = roll + skillBonus
		self.skillLabelString.set('Roll {} : {} ({} + {})'.format(skillName, finalRoll, roll, skillBonus))


	# call back function for the Roll button near the basic attack display
	# rolls the appropriate virtual dice and adds the approprite bonuses and then displays the result on a label
	def rollAttack(self):
		natAtkRoll = random.randint(1,20)
		atkResult = natAtkRoll + self.attackBonus
		weaponNumOfDice = int(self.weaponDamage[0])
		weaponDieSize = int(self.weaponDamage[2:])
		damage = 0
		damageRolls = []
		for i in xrange(weaponNumOfDice):
			roll = random.randint(1,weaponDieSize)
			damage += roll
			damageRolls.append(roll)
		
		damage += self.damageBonus
		weapon = characterGenerator.weapons[test.equipment['Main Hand'][3:]]

		if natAtkRoll >= weapon[1]:
			damage = damage * weapon[2]
			crit = True
		else:
			crit = False

		if crit:
			self.atkResultString.set('Attack Roll: {} ({}) : Damage (CRIT!!): {} (({}+{})*{})'.format(atkResult, natAtkRoll, damage, damageRolls, self.damageBonus, weapon[2]))
		else:
			self.atkResultString.set('Attack Roll: {} ({}) : Damage: {} ({}+{})'.format(atkResult, natAtkRoll, damage, damageRolls, self.damageBonus))


	def displayCharacter(self):
		heightSM = 12 # height of skill and move boxes
		widthSM = 35 # width of skill and move boxes

		for widget in self.winfo_children():
			widget.destroy()



		self.nameLabelString = Tkinter.StringVar()
		nameLabel = Tkinter.Label(self, textvariable=self.nameLabelString)
		nameLabel.grid(column=0,row=0,columnspan=4)
		self.nameLabelString.set(test.name)

		self.raceClassLabelString = Tkinter.StringVar()
		raceClassLabel = Tkinter.Label(self, textvariable=self.raceClassLabelString)
		raceClassLabel.grid(column=0,row=1,columnspan=4)
		self.raceClassLabelString.set('Lvl {} {} {}'.format(test.level, test.race, test.clas))

		self.abiScoreLabelString = Tkinter.StringVar()
		abiScoreLabel = Tkinter.Label(self, textvariable=self.abiScoreLabelString)
		abiScoreLabel.grid(column=0,row=3)
		self.abiScoreLabelString.set('Ability Scores')

		self.strScoreLabelString = Tkinter.StringVar()
		strScoreLabel = Tkinter.Label(self, textvariable=self.strScoreLabelString)
		strScoreLabel.grid(column=0,row=4)
		self.strScoreLabelString.set('Str {} ({})'.format(test.strength, test.strMod))

		self.dexScoreLabelString = Tkinter.StringVar()
		dexScoreLabel = Tkinter.Label(self, textvariable=self.dexScoreLabelString)
		dexScoreLabel.grid(column=0,row=5)
		self.dexScoreLabelString.set('Dex {} ({})'.format(test.dexterity, test.dexMod))

		self.conScoreLabelString = Tkinter.StringVar()
		conScoreLabel = Tkinter.Label(self, textvariable=self.conScoreLabelString)
		conScoreLabel.grid(column=0,row=6)
		self.conScoreLabelString.set('Con {} ({})'.format(test.constitution, test.conMod))

		self.intScoreLabelString = Tkinter.StringVar()
		intScoreLabel = Tkinter.Label(self, textvariable=self.intScoreLabelString)
		intScoreLabel.grid(column=0,row=7)
		self.intScoreLabelString.set('Int {} ({})'.format(test.intelligence, test.intMod))

		self.wisScoreLabelString = Tkinter.StringVar()
		wisScoreLabel = Tkinter.Label(self, textvariable=self.wisScoreLabelString)
		wisScoreLabel.grid(column=0,row=8)
		self.wisScoreLabelString.set('Wis {} ({})'.format(test.wisdom, test.wisMod))

		self.chaScoreLabelString = Tkinter.StringVar()
		chaScoreLabel = Tkinter.Label(self, textvariable=self.chaScoreLabelString)
		chaScoreLabel.grid(column=0,row=9)
		self.chaScoreLabelString.set('Cha {} ({})'.format(test.charisma, test.chaMod))



		self.hpLabelString = Tkinter.StringVar()
		hpLabel = Tkinter.Label(self, textvariable=self.hpLabelString)
		hpLabel.grid(column=2,row=3)
		self.hpLabelString.set('Hit Points {}'.format(test.hitPoints))

		self.acLabelString = Tkinter.StringVar()
		acLabel = Tkinter.Label(self, textvariable=self.acLabelString)
		acLabel.grid(column=2,row=4)
		self.acLabelString.set('Armor Class {}'.format(test.armorClass))

		self.touchFFLabelString = Tkinter.StringVar()
		touchFFLabel = Tkinter.Label(self, textvariable=self.touchFFLabelString)
		touchFFLabel.grid(column=2,row=5)
		self.touchFFLabelString.set('Touch {} | Flat-footed {}'.format(test.touchArmorClass, test.flatFootedArmorClass))

		self.fortLabelString = Tkinter.StringVar()
		fortLabel = Tkinter.Label(self, textvariable=self.fortLabelString)
		fortLabel.grid(column=2,row=6)
		self.fortLabelString.set('Fort +{}'.format(test.fortSave))

		self.refLabelString = Tkinter.StringVar()
		refLabel = Tkinter.Label(self, textvariable=self.refLabelString)
		refLabel.grid(column=2,row=7)
		self.refLabelString.set('Ref +{}'.format(test.refSave))

		self.willLabelString = Tkinter.StringVar()
		willLabel = Tkinter.Label(self, textvariable=self.willLabelString)
		willLabel.grid(column=2,row=8)
		self.willLabelString.set('Will +{}'.format(test.willSave))

		self.babLabelString = Tkinter.StringVar()
		babLabel = Tkinter.Label(self, textvariable=self.babLabelString)
		babLabel.grid(column=2,row=9)
		babString = 'BAB +{}'.format(test.BAB)
		for i in xrange((int)(test.BAB-1)/5):
			babString += '/+{}'.format(test.BAB - (5*(i+1)))
		self.babLabelString.set(babString)


		parsedWeapon = test.equipment['Main Hand'][3:]
		weaponBonus = int(test.equipment['Main Hand'][1])
		self.weaponDamage = characterGenerator.weapons[parsedWeapon][0]
		numOfDice = int(self.weaponDamage[0])
		dieSize = int(self.weaponDamage[2:])
		self.attackBonus = weaponBonus + test.BAB
		self.damageBonus = weaponBonus + test.strMod
		if 'Weapon Finesse' in test.featList or 'Ranged Attacker' in test.tags:
			self.attackBonus += test.dexMod
		else:
			self.attackBonus += test.strMod
		if 'Weapon Focus' in test.featList:
			self.attackBonus += 1
		if 'Weapon Specialization' in test.featList:
			self.damageBonus += 2
		if 'Big Weapon' in test.tags:
			self.damageBonus += (int)(0.5 * test.strMod)
		self.atkLabelString = Tkinter.StringVar()
		atkLabel = Tkinter.Label(self, textvariable=self.atkLabelString)
		atkLabel.grid(column=0,row=10,columnspan=3, sticky=Tkinter.W)
		self.atkLabelString.set('Basic Attack: {} +{} ATK {}d{}+{} {}-20/x{}'.format(parsedWeapon, self.attackBonus, numOfDice, dieSize, self.damageBonus, characterGenerator.weapons[parsedWeapon][1], characterGenerator.weapons[parsedWeapon][2]))
		atkButton = Tkinter.Button(self, text='Roll Attack', command=self.rollAttack)
		atkButton.grid(column=2, row=10, sticky=Tkinter.E)

		self.atkResultString = Tkinter.StringVar()
		atkResultLabel = Tkinter.Label(self, textvariable=self.atkResultString)
		atkResultLabel.grid(column=0,row=11,columnspan=3)

		#BEGIN SETUP OF MOVEBOX AND WHATNOT
		if test.clas == 'Fighter': # fighters have their own setup because they have so few class features
			featScroll = Tkinter.Scrollbar(self)
			featBox = Tkinter.Listbox(self, yscrollcommand=featScroll.set)
			featBox.config(height=20, width=widthSM)
			featBox.grid(column=0, row=12, rowspan=3)
			featScroll.config(command=featBox.yview)
			featScroll.grid(column=1, row=12, rowspan=3, sticky=Tkinter.N+Tkinter.S)

			specialScroll = Tkinter.Scrollbar(self)
			specialBox = Tkinter.Listbox(self, yscrollcommand=specialScroll.set)
			specialBox.config(height=10, width=widthSM)
			specialBox.grid(column=2, row=12, rowspan=2)
			specialScroll.config(command=specialBox.yview)
			specialScroll.grid(column=3, row=12, rowspan=2, sticky=Tkinter.N+Tkinter.S)

			skillScroll = Tkinter.Scrollbar(self)
			self.skillBox = Tkinter.Listbox(self, yscrollcommand=skillScroll.set)
			self.skillBox.config(height=10, width=widthSM)
			self.skillBox.grid(column=2, row=14)
			skillScroll.config(command=self.skillBox.yview)
			skillScroll.grid(column=3, row=14, sticky=Tkinter.N+Tkinter.S)	

		else:

			if 'Psionic' in test.tags:
				powerScroll = Tkinter.Scrollbar(self)
				powerBox = Tkinter.Listbox(self, yscrollcommand=powerScroll.set)
				powerBox.config(height=20, width=widthSM)
				powerBox.grid(column=0, row=12, rowspan=3)
				
				powerScroll.config(command=powerBox.yview)
				powerScroll.grid(column=1, row=12, sticky=Tkinter.N+Tkinter.S, rowspan=3)

				powerBox.insert(Tkinter.END, 'PP: {}'.format(test.powerPoints))
				for power in test.powerList:
					powerBox.insert(Tkinter.END, power)

			elif 'Martial Adept' in test.tags:
				manScroll = Tkinter.Scrollbar(self)
				manBox = Tkinter.Listbox(self, yscrollcommand=manScroll.set)
				manBox.config(height=14, width=widthSM)
				manBox.grid(column=0, row=12, rowspan=2)
				manScroll.config(command=manBox.yview)
				manScroll.grid(column=1, row=12, sticky=Tkinter.N+Tkinter.S, rowspan=2)

				manBox.insert(Tkinter.END, 'Maneuvers Known: (**{} Ready**)'.format(test.maneuversReadied))
				if test.clas == 'Crusader':
					grantedManeuverIndices = random.sample(xrange(len(test.maneuverList)), test.maneuversReadied[0])
					readyManeuverIndices = random.sample(grantedManeuverIndices, test.maneuversReadied[1])
					for i in xrange(len(test.maneuverList)):
						if i in grantedManeuverIndices:
							if i in readyManeuverIndices:
								manBox.insert(Tkinter.END, '**{}** (Granted)'.format(test.maneuverList[i]))
							else:
								manBox.insert(Tkinter.END, '{} (Granted)'.format(test.maneuverList[i]))
						else:
							manBox.insert(Tkinter.END, test.maneuverList[i])
				else:
					readyManeuverIndices = random.sample(xrange(len(test.maneuverList)), test.maneuversReadied)
					for i in xrange(len(test.maneuverList)):
						if i in readyManeuverIndices:
							manBox.insert(Tkinter.END, '**{}**'.format(test.maneuverList[i]))
						else:
							manBox.insert(Tkinter.END, test.maneuverList[i])

				stanceScroll = Tkinter.Scrollbar(self)
				stanceBox = Tkinter.Listbox(self, yscrollcommand=stanceScroll.set)
				stanceBox.config(height=6, width=widthSM)
				stanceBox.grid(column=0, row=14)
				stanceScroll.config(command=stanceBox.yview)
				stanceScroll.grid(column=1, row=14, sticky=Tkinter.N+Tkinter.S)

				stanceBox.insert(Tkinter.END, 'Stances Known: (**Active**)')
				activeStanceIndex = random.randint(0, len(test.stanceList)-1)
				for i in xrange(len(test.stanceList)):
					if i == activeStanceIndex:
						stanceBox.insert(Tkinter.END, '**{}**'.format(test.stanceList[i]))
					else:
						stanceBox.insert(Tkinter.END, test.stanceList[i])


			elif 'Spellcaster' in test.tags:
				spellScroll = Tkinter.Scrollbar(self)
				spellBox = Tkinter.Listbox(self, yscrollcommand=spellScroll.set)
				spellBox.config(height=14, width=widthSM)
				spellBox.grid(column=0, row=12, rowspan=2)
				spellScroll.config(command=spellBox.yview)
				spellScroll.grid(column=1, row=12, sticky=Tkinter.N+Tkinter.S, rowspan=2)


				spdScroll = Tkinter.Scrollbar(self) # spd = spells per day
				spdBox = Tkinter.Listbox(self, yscrollcommand=spdScroll.set)
				spdBox.config(height=6, width=widthSM)
				spdBox.grid(column=0, row=14)
				spdScroll.config(command=spdBox.yview)
				spdScroll.grid(column=1, row=14, sticky=Tkinter.N+Tkinter.S)

				if 'Prepared' in test.tags:
					spellBox.insert(Tkinter.END, 'Spells Prepared (Level): ')
					if test.clas == 'Paladin' or test.clas == 'Ranger':
						if test.clas == 'Paladin':
							dcMod = test.chaMod
						else:
							dcMod = test.wisMod
						for i in xrange(len(test.spellsPerDay)):
							spdBox.insert(Tkinter.END, 'Lvl {} : {}/Day DC {}'.format(i+1, test.spellsPerDay[i], i+11+dcMod))
							for spell in test.spellsPrepared[i]:
								spellBox.insert(Tkinter.END, '{} ({})'.format(spell, i+1))
					else:
						if test.clas == 'Druid':
							dcMod = test.wisMod
						for i in xrange(len(test.spellsPerDay)+1):
							if i == 0:
								spdBox.insert(Tkinter.END, 'Lvl 0 : 99/Day DC {}'.format(10+dcMod))
								for spell in test.spellsPrepared[i]:
									spellBox.insert(Tkinter.END, '{} ({})'.format(spell, i))
							else:
								spdBox.insert(Tkinter.END, 'Lvl {} : {}/Day DC {}'.format(i, test.spellsPerDay[i-1], i+10+dcMod))
								for spell in test.spellsPrepared[i-1]:
									spellBox.insert(Tkinter.END, '{} ({})'.format(spell, i))

				elif 'Spontaneous' in test.tags:
					spellBox.insert(Tkinter.END, 'Spells Known (Level): ')
					if test.clas == 'Dread Necromancer':
						for i in xrange(len(test.spellsPerDay)):
							spdBox.insert(Tkinter.END, 'Lvl {} : {}/day DC {}'.format(i+1, test.spellsPerDay[i], i+11+test.chaMod))
							for spell in test.spellList[i]:
								spellBox.insert(Tkinter.END, '{} ({})'.format(spell, i+1))
					else:
						if test.clas == 'Beguiler' or test.clas == 'Warmage':
							dcMod = test.intMod
						elif test.clas == 'Bard':
							dcMod = test.chaMod
						for i in xrange(len(test.spellsPerDay)+1):
							if i == 0:
								spdBox.insert(Tkinter.END, 'Lvl 0 : 99/Day DC {}'.format(10+dcMod))
								for spell in test.spellList[i]:
									spellBox.insert(Tkinter.END, '{} (0)'.format(spell))
							else:
								spdBox.insert(Tkinter.END, 'Lvl {} : {}/Day DC {}'.format(i, test.spellsPerDay[i-1], i+10+dcMod))
								for spell in test.spellList[i-1]:
									spellBox.insert(Tkinter.END, '{} ({})'.format(spell, i))
					

			elif test.clas == 'Barbarian':
				rageScroll = Tkinter.Scrollbar(self)
				rageBox = Tkinter.Listbox(self, yscrollcommand=rageScroll.set)
				rageBox.config(height=20, width=widthSM)
				rageBox.grid(column=0, row=12, rowspan=3)
				rageScroll.config(command=rageBox.yview)
				rageScroll.grid(column=1, row=12, rowspan=3, sticky= Tkinter.N+Tkinter.S)
				rageBox.insert(Tkinter.END, 'Rage Powers: ')
				for item in test.ragePowers:
					rageBox.insert(Tkinter.END, item)

			elif test.clas == 'Rogue':
				rogueTalentScroll = Tkinter.Scrollbar(self)
				rogueTalentBox = Tkinter.Listbox(self, yscrollcommand=rogueTalentScroll.set)
				rogueTalentBox.config(height=20, width=widthSM)
				rogueTalentBox.grid(column=0, row=12, rowspan=3)
				rogueTalentScroll.config(command=rogueTalentBox.yview)
				rogueTalentScroll.grid(column=1, row=12, rowspan=3, sticky= Tkinter.N+Tkinter.S)
				rogueTalentBox.insert(Tkinter.END, 'Rogue Talents: ')
				for item in test.rogueTalents:
					rogueTalentBox.insert(Tkinter.END, item)

			specialScroll = Tkinter.Scrollbar(self)
			specialBox = Tkinter.Listbox(self, yscrollcommand=specialScroll.set)
			specialBox.config(height=8, width=widthSM)
			specialBox.grid(column=2, row=12)
			
			specialScroll.config(command=specialBox.yview)
			specialScroll.grid(column=3, row=12, sticky=Tkinter.N+Tkinter.S)

			featScroll = Tkinter.Scrollbar(self)
			featBox = Tkinter.Listbox(self, yscrollcommand=featScroll.set)
			featBox.config(height=5, width=widthSM)
			featBox.grid(column=2, row=13)
			
			featScroll.config(command=featBox.yview)
			featScroll.grid(column=3, row=13, sticky=Tkinter.N+Tkinter.S)

			skillScroll = Tkinter.Scrollbar(self)
			self.skillBox = Tkinter.Listbox(self, yscrollcommand=skillScroll.set)
			self.skillBox.config(height=7, width=widthSM)
			self.skillBox.grid(column=2, row=14)
			
			skillScroll.config(command=self.skillBox.yview)
			skillScroll.grid(column=3, row=14, sticky=Tkinter.N+Tkinter.S)			



		specialBox.insert(Tkinter.END, 'Special Features: ')
		for item in test.specialList:
			specialBox.insert(Tkinter.END, item)
		featBox.insert(Tkinter.END, 'Feats: ')
		for item in test.featList:
			featBox.insert(Tkinter.END, item)
		self.skillBox.insert(Tkinter.END, 'Skills: ')
		sortedSkills = sorted(test.skillBonus.items(), key=operator.itemgetter(1))
		sortedSkills.reverse()
		for item in sortedSkills:
			self.skillBox.insert(Tkinter.END, '{} +{}'.format(item[0], item[1]))

		skillButton = Tkinter.Button(self, text='Roll Skill', command=self.rollSkill)
		skillButton.grid(column=2, row=15)
		self.skillLabelString = Tkinter.StringVar()
		skillLabel = Tkinter.Label(self, textvariable=self.skillLabelString)
		skillLabel.grid(column=0, row=15)

		writeButton = Tkinter.Button(self, text='Write Character to {}.txt'.format(test.name), command=self.writeCharacter)
		writeButton.grid(column=0, row=16)

		self.grid_columnconfigure(0,weight=1)
		self.resizable(False,False)
		self.update()
		self.geometry(self.geometry())

	# END displayCharacter


if __name__ == "__main__":
	app = theGUI(None)
	app.title('Character Generator & Display')
	app.mainloop()
