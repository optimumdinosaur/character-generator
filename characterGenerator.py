import random
import math
import operator


# LISTS CONTAINING ALL SPELLS, POWERS, & MANEUEVERS
# THE SUBLIME WAY
desertWind = ['Blistering Flourish', 'Burning Blade', "Flame's Blessing", 'Wind Stride', 'Burning Brand', 'Fire Riposte', 'Flashing Sun', "Hatchling's Flame", 'Death Mark', 'Fan the Flames', 'Holocaust Cloak', 'Zephyr Dance', 'Firesnake', 'Searing Blade', 'Searing Charge', "Dragon's Flame", 'Leaping Flame', 'Lingering Inferno', 'Desert Tempest', 'Fiery Assault', 'Ring of Fire', 'Inferno Blade', 'Salamander Charge', 'Rising Phoenix', "Wyrm's Flame", 'Inferno Blast']
devotedSpirit = ["Crusader's Strike", "Iron Guard's Glare", 'Martial Spirit', 'Vanguard Strike', 'Foehammer', 'Shield Block', 'Defensive Rebuke', 'Revitalizing Strike', 'Thicket of Blades', 'Divine Surge', 'Entangling Blade', 'Daunting Strike', 'Doom Charge', 'Law Bearer', 'Radiant Charge', 'Tide of Chaos', 'Aura of Chaos', 'Aura of Perfect Order', 'Order of Triumph' 'Order of Tyranny', 'Rallying Strike', 'Castigating Strike', 'Shield Counter', 'Greater Divine Surge', 'Immortal Fortitude', 'Surge of Righteous Vitality']
diamondMind = ['Moment of Perfect Clarity', 'Sapphire Nightmare Blade', 'Stance of Clarity', 'Action Before Thought', 'Emerald Razor', 'Insightful Strike', 'Mind Over Body', 'Pearl of Black Doubt', 'Boudning Assault', 'Mind Strike', 'Ruby Nightmare Blade', 'Disrupting Blow', 'Hearing the Air', 'Rapid Counter', 'Greater Insightful Strike', 'Moment of Alacrity', 'Avalanche of Blades', 'Quicksilver Motion', 'Diamond Defense', 'Diamond Nightmare Blade', 'Stance of Alacrity', 'Time Stands Still']
ironHeart = ['Punishing Stance', 'Steel Wind', 'Steely Strike', 'Disarming Strike', 'Wall of Blades', 'Absolute Steel Stance', 'Exorcism of Steel', 'Iron Heart Surge', 'Lightning Recovery', 'Mithral Tornado', 'Dancing Blade Form', 'Dashing Strike', 'Iron Heart Focus', 'Iron Heart Endurance', 'Manticore Parry', 'Finishing Move', 'Scything Blade', 'Adamantine Hurricane', 'Lightning Throw', 'Supreme Blade Parry','Strike of Perfect Clarity']
settingSun = ['Counter Charge', 'Mighty Throw', 'Step of the Wind', 'Baffling Defense', 'Clever Positioning', 'Comet Throw', 'Strike of the Broken Shield', 'Mirrored Pursuit', 'Shifting Defense', 'Soaring Throw', 'Stalking Shadow', 'Ballista Throw', 'Scorpion Parry', 'Hydra Slaying Strike', "Fool's Strike", 'Ghostly Defense', 'Tornado Throw']
shadowHand = ['Child of Shadow', 'Shadow Blade Technique', 'Clinging Shadow Strike', 'Island of Blades', 'Cloak of Deception', 'Drain Vitality', 'Shadow Jaunt', "Assassin's Stance", 'Dance of the Spider', 'Shadow Garrote', 'Strength Draining Strike', 'Hand of Death', 'Obscuring Shadow Veil', 'Bloodletting Strike', 'Shadow Stride', 'Step of the Dancing Moth', 'Ghost Blade', 'Shadow Noose', 'Stalker in the Night', 'Death in the Dark', 'Shadow Blink', 'Balance on the Sky', 'Enervating Shadow Strike', 'One With Shadow', 'Five-Shadow Creeping Ice Enervation Strike']
stoneDragon = ['Charging Minotaur', 'Stone Bones', 'Stonefoot Stance', 'Mountain Hammer', 'Stone Vise', 'Bonecrusher', 'Crushing Weight of the Mountain', 'Roots of the Mountain', "Stone Dragon's Fury", 'Bonesplitting Strike', 'Boulder Roll', 'Overwhelming Mountain Strike', 'Elder Mountain Hammer', "Giant's Stance", 'Mountain Avalanche', 'Crushing Vise', 'Iron Bones', 'Irresistable Mountain Strike', 'Ancient Mountain Hammer', 'Colossus Strike', 'Adamantine Bones', 'Earthstrike Quake', 'Strength of Stone', 'Mountain Tombstone Strike']
tigerClaw = ['Blood in the Water', "Hunter's Sense", 'Sudden Leap', 'Wolf Fang Strike', 'Claw at the Moon', 'Rabid Wolf Strike', 'Flesh Ripper', 'Leaping Dragon Stance', 'Soaring Raptor Strike', 'Wolverine Stance', 'Death From Above', 'Fountain of Blood', 'Dancing Mongoose', 'Pouncing Charge', 'Rabid Bear Strike', 'Wolf Climbs the Mountain', 'Hamstring Attack', 'Prey on the Weak', 'Swooping Dragon Strike', 'Girallon Windmill Flesh Rip', 'Raging Mongoose', 'Wolf Pack Tactics', 'Feral Death Blow']
whiteRaven = ['Bolstering Voice', 'Douse the Flames', 'Leading the Attack', 'Leading the Charge', "Battle Leader's Charge", 'Tacical Strike', "Lion's Roar", 'Tactics of the Wolf', 'White Raven Tactics', 'Covering Strike', 'White Raven Strike', 'Flanking Maneuver', 'Press the Advantage', 'Order Forged from Chaos', "War Leader's Charge", 'Clarion Call', 'Swarming Assault', 'Swarm Tactics', 'White Raven Hammer', "War Maser's Charge"]
# BARD SPELLS organized as such: [[Cantrips], [1st level spells], [2nd level spells], ...]
bardSpells = [['Dancing Lights', 'Daze', 'Detect Magic', 'Flare', 'Ghoust Sound', 'Haunted Fey Aspect', 'Know Direction', 'Light', 'Lullaby', 'Mage Hand', 'Mending', 'Message', 'Open/Close', 'Prestidigitation', 'Read Magic', 'Resistance', 'Sift', 'Spark', 'Summon Instrument', 'Unwitting Ally'], ['Abundant Ammunition', 'Adjuring Step', 'Adoration', 'Alarm', 'Alter Musical Instrument', 'Animate Rope', 'Anticipate Peril', 'Abstemiousness', 'Aspect of the Nightingale', 'Beguiling Gift', 'Blurred Movement', 'Borrow Skill', 'Call Weapon', 'Cause Fear', 'Charm Person', 'Chord of Shards', 'Clarion Call', 'Compel Hostility', 'Comprehend Languages', 'Cultural Adaptation', 'Lesser Confusion', 'Cure Light Wounds', 'Dancing Lantern', 'Darting Duplicate', 'Dazzling Blade', "Deadeye's Lore", 'Delusional Pride', 'Detect Charm', 'Detect Metal', 'Detect Secret Doors', 'Discern Next of Kin', 'Disguise Weapon', 'Disguise Self', 'Ear-Piercing Scream', 'Enhance Water', 'Erase', 'Expeditious Retreat', 'Feather Fall', 'Feater Step', 'Flare Burst', 'Forced Quiet', 'Fumbletongue', 'Glue Seal', 'Grease', 'Haze of Dreams', 'Heightened Awareness', "Tasha's Hideous Laughter", ' Horn of Pursuit', 'Hypnotism', 'Identify', 'Innocence', 'Invigorate', 'Invisibility Alarm', 'Jitterbugs', 'Jury-Rig', 'Ki Arrow', 'Lighten Object', 'Liberating Command', 'Lock Gaze', 'Memorize Page', 'Moment of Greatness', 'Magic Mouth', 'Memory Lapse', 'Magic Aura', "Nature's Paths", 'Negative Reaction', 'Obscure Object', 'Play Instrument', 'Poisoned Egg', 'Read Weather', 'Recharge Innate Magic', 'Remove Fear', 'Restful Sleep', 'Saving Finale', 'See Alignment', 'Share Lanaguage', 'Silent Image', 'Sleep', 'Solid Note', 'Summon Minor Monster', 'Summon Monster I', 'Swaller Your Fear', 'Tap Inner Beauty', 'Technomancy', 'Timely Inspiration', 'Toilsome Chant', 'Touch of Gracelessness', 'Transfer Tattoo', 'Twisted Fortunes', 'Unbreakable Heart', 'Undetectable Alignment', 'Unnatural Lust', 'Unprepared Combatant', 'Unseen Servant', 'Vanish', 'Ventriloquism', 'Vocal Alteration', 'Weaponwand', 'Youthful Appearance'], ['Acute Senses', 'Air Step', 'Allegro', 'Alter Self', 'Alter Summoned Monster', 'Ancestral Communion', 'Animal Messenger', 'Animal Purpose Training', 'Animal Trance', 'Anonymous Interaction', 'Arcane Disruption', 'Bestow Insight', 'Bladed Dash', 'Blindness/Deafness', 'Blistering Incetive', 'Blood Biography', 'Boiling Blood', 'Book Ward', 'Blur', 'Bullet Ward', 'Buoyancy', 'Cacophonous Call', 'Callback', 'Calm Emotions', "Cat's Grace", 'Charitable Impulse', 'Codespeak', 'Commune with Birds', 'Compassionate Ally', 'Create Treasure Map', 'Cure Moderate Wounds', 'Darkness', 'Daze Monster', 'Delay Pain', 'Delay Poison', 'Detect Thoughts', 'Determine Depth', 'Discovery Torch', 'Disguise Other', 'Distracting Cacophony', 'Distressing Tone', 'Dream Shield', 'Dust of Twilight', "Eagle's Splendor", 'Empower Holy Water', 'Enshroud Thoughts', 'Enter Image', 'Enthrall', 'Escaping Ward', 'Focused Scrutiny', "Fox's Cunning", 'Gallant Inspiration', 'Ghostbane Dirge', 'Ghostly Disguise', 'Glitterdust', 'Haunting Mists', 'Heightened Reflexes', 'Heroic Fortune', 'Heroism', 'Hidden Speech', 'Hold Person', 'Honeyed Tongue', 'Hydrophobia', 'Hypnotic Pattern', 'Instant Weapon', 'Investigate Mind', 'Invisibility', 'Jealous Rage', 'Locate Object', 'Mad Hallucination', 'Marching Chant', 'Masterwork Transformation', 'Mindlocked Messenger', 'Minor Image', 'Mirror Image', 'Misdirection', 'Miserable Pity', 'Muffle Sound', 'Oppressive Boredom', 'Path of Glory', 'Piercing Shriek', 'Pilfering Hand', "Pugwampi's Grace", 'Pyrotechnics', 'Qualm', 'Rage', 'Reckless Infatuation', 'Resounding Clang', 'Restrieve Item', 'Returning Weapon', 'Scare', "Seducer's Eyes", 'Shadow Anchor', 'Communal Share Language', 'Share Memory', 'Shatter', 'Silence', 'Silent Table', 'Silk to Steel', 'Snapdragon Fireworks', 'Sonic Scream', 'Sound Burst', 'Spell Gauge', 'Steal Voice', 'Suggestion', 'Summon Monster II', 'Summon Swarm', 'Tactical Acumen', 'Tattoo Potion', 'Thunder Fire', 'Tongues', 'Touch of Mercy', 'Track Ship', 'Trail of the Rose', 'Umbral Weapon', 'Unadulterated Loathing', 'Versatile Weapon', 'Wartrain Mount', 'Whip of Spiders', 'Whispering Wind'], ['Accept Affliction', 'Adjustable Disguise', 'Arcane Concordance', 'Aura of the Unremarkable', 'Blink', 'Blot', 'Campfire Wall', 'Channel the Gift', 'Charm Monster', 'Clairvoyance/Clairvoyance', 'Confusion', 'Contingent Action', 'Control Summoned Creature', 'Coordinated Effort', 'Crushing Despair', 'Cure Serious Wounds', 'Curse of Disgust', 'Daylight', 'Death from Below', 'Communal Delay Poison', 'Deep Slumber', 'Discern Value', 'Dispel Magic', 'Displacemnet', 'Disrupt Link', 'Elemental Speech', 'Exquisite Accompaniment', 'False Alibi', 'Fear', 'Fearsome Duplicate', 'Mass Feather Step', 'Flexible Fury', 'Fractions of Heal and Harm', 'Gaseous Form', 'Lesser Geas', 'Glibess', 'Good Hope', 'Harrowing', 'Haste', 'Haunting Choir', 'Illusory Script', 'Mass Invigorate', 'Invisibility Sphere', 'Isolate', "Jester's Jaunt", "Lover's Vengenace", 'Mad Monkeys', 'Major Image', 'Malicious Spite', 'Martial Marionette', 'Minor Dream', 'Overwhelming Grief', 'Phantom Diver', 'Phantom Steed', 'Pierce Disguise', 'Prehensile Pilfer', 'Purging Finale', 'Raging Rubble', 'Rain of Frogs', "Raven's Flight", 'Remvoe Curse', 'Communal Returning Weapon', 'Reviving Finale', 'Scrying', 'Sculpt Sound', 'Secret Page', 'See Invisibility', 'Seek Thoughts', 'Sepia Snake Sigil', 'Slow', 'Smug Narcissism', 'Speak with Animals', 'Summon Monster III', 'Terrible Remorse', 'Thunderous Drums', 'Tiny Hut', 'Communal Tongues', 'Triggered Suggestion', 'Vision of Hell', 'Wall of Nausea', 'Witness'], ['Adjustable Polymorph', 'Ancestral Gift', 'Antithetical Constraint', 'Apparent Master', 'Break Enchantment', 'Contingent Scroll', 'Conversing Wind', 'Cure Critical Wounds', 'Dance of a Hundred Cuts', 'Mass Daze', 'Denounce', 'Detect Scrying', 'Dimension Door', 'Discordant Blast', 'Dominate Person', 'Echolocation', 'Envious Urge', 'Feast on Fear', 'Forgetful Slumber', 'Mass Ghostbane Dirge', 'Freedom of Movement', 'Hallucinatory Terrain', 'Heroic Finale', 'Mass Heroic Fortune', 'Hold Monster', 'Greater Invisibility', 'Legend Lore', 'Locate Creature', 'Kiss of the First World', 'Modify Memory', 'Neutralize Poison', "Nixie's Lure", 'Greater Path of Glory', 'Communal Phantom Steed', 'Primal Scream', 'Rainbow Pattern', 'Repel Vermin', 'Secure Shelter', 'Serenity', 'Shadow Conjuration', 'Shadow Step', 'Shield of the Dawnflower', 'Shocking Image', 'Shout', 'Song of Healing', 'Sonic Thrust', 'Speak with Plants', 'Summon Accuser', 'Summon Monster IV', 'Treasure Stitching', 'Unseen Crew', 'Utter Contempt', 'Virtuoso Performance', 'Wall of Blindness/Deafness', 'Wall of Sound', 'Wandering Star Motes', 'Zone of Silence'], ["Archon's Trumpet", "Bard's Escape", 'Greater Bladed Dash', 'Mass Cacophonous Call', 'Greater Callback', 'Cloak of Dreams', 'Covetous Aurea', 'Mass Cure Light Wounds', 'Deafening Song Bolt', 'Death Pact', 'Greater Dispel Magic', 'Dream', 'False Vision', 'Foe to Friend', 'Frozen Note', 'Greater Heroism', 'Hymn of Mercy', 'Joyful Rapture', 'Ki Shout', 'Mind Fog', 'Mirage Arcana', 'Mislead', 'Music of the Spheres', 'Nightmare', 'Persistent Image', 'Phantasmal Web', 'Resonating Word', 'Sabotage Construct', 'Seeming', 'Shadow Evocation', 'Shadow Walk', 'Shadowbard', 'Song of Discord', 'Soulswitch', 'Stunning Finale', 'Mass Suggestion', 'Summon Infernal Host', 'Summon Monster V', 'Unwilling Shield', 'Vengeful Outrage', 'Whip of Centipedes'], ['Analyze Dweomer', 'Animate Objects', 'Brilliant Inspiration', "Mass Cat's Grace", 'Mass Charm Monster', 'Mass Cure Moderate Wounds', 'Dance of a Thousand Cuts', 'Deadly Finale', 'Dirge of the Victorious Knights', "Mass Eagle's Splendor", 'Euphoric Tranquility', 'Eyebite', 'Find the Path', "Fool's Forbiddance", "Mass Fox's Cunning", 'Geas/Quest', 'Getaway', "Heroes' Feast", 'Hymn of Peace', 'Irresistable Dance', 'Magnifying Chime', 'Overwhelming Presence', 'Permanent Image', 'Pied Piping', 'Programmed Image', 'Project Image', 'Greater Scrying', 'Greater Shout', 'Sonic Form', 'Subjective Reality', 'Summon Monster VI', 'Sympathetic Vibration', 'Unconscious Agenda', 'Veil', 'Waves of Ecstasy', 'Whip of Ants']]
# DRUID SPELLS (sans Summon Nature's Ally just so it won't be pointlessly prepared)
druidSpells = [['Create Water', 'Detect Magic', 'Detect Poison', 'Enhanced Diplomacy', 'Flare', 'Guidance', 'Know Direction', 'Light', 'Mending', 'Purify Food and Drink', 'Read Magic', 'Resistance', 'Read Magic', 'Resistance', 'Spark', 'Stabilize', 'Virtue'], ['Clam Animals', 'Charm Animal', 'Cure Light Wounds', 'Detect Animasls or Plants', 'Detect Snares and Pits', 'Endure Elements', 'Entangle', 'Faerie Fire', 'Goodberry', 'Hide from Animals', 'Jump', 'Keen Senses', 'Longstrider', 'Magic Fang', 'Magic Stone', 'Obscuring Mist', 'Pass without Trace', 'Produce Flame', 'Shiellelagh', 'Speak with Animals'], ['Animal Messenger', 'Animal Trance', 'Barkskin', "Bear's Endurance", "Bull's Strength", "Cat's Grace", 'Chill Metal', 'Delay Poison', 'Fire Trap', 'Flame Blade', 'Flaming Sphere', 'Fog Cloud', 'Gust of Wind', 'Heat Metal', 'Hold Animal', "Owl's Wisdom", 'Reduce Animal', 'Resist Energy', 'Lesser Restoration', 'Soften Earth and Stone', 'Spider Climb', 'Summon Swarm', 'Tree Shape', 'Warp Wood', 'Wood Shape'], ['Call Lightning', 'Contagion', 'Cure Moderate Wounds', 'Daylight', 'Diminish Plants', 'Dominate Animal', 'Greater Magic Fang', 'Meld into Stone', 'Neutralize Poison', 'Plant Growth', 'Poison', 'Protection from Energy', 'Quench', 'Remove Disease', 'Sleet Storm', 'Snare', 'Speak with Plants', 'Spike Growth', 'Stone Shape', 'Water Breathing', 'Wind Wall'], ['Absorb Toxicity', 'Lesser Age Resistance', 'Air Walk', 'Antiplant Shell', 'Arboreal Hammer', 'Aspect of the Stag', 'Atavism', 'Ball Lightning', 'Blight', 'Bloody Claws', 'Cape of Wasps', 'Command Plants', 'Control Water', 'Cure Serious Wounds', 'Dispel Magic', 'Echolocation', 'Flame Strike', 'Freedom of Movement', 'Geyser', 'Giant Vermin', 'Grove of Respite', 'Ice Storm', 'Life Bubble', 'Moonstruck', 'Obsidian Flow', 'Plague Carrier', 'Communal Protection from Energy', 'Reincarnate', 'Repel Vermin', 'Ride the Waves', 'River of Wind', 'Rusting Grasp', 'Scrying', 'Spike Stones', 'Strong Jaw', 'Thorn Body', 'Touch of Slime', 'True Form', 'Vermin Shape II', 'Volcanic Storm'], ['Communal Air Walk', 'Animal Growth', 'Aspect of the Wolf', 'Atonement', 'Awaken', 'Baleful Polymorph', 'Blessing of the Salamander', 'Call Lightning Storm', 'Commune with Nature', 'Greater Contagion', 'Control Winds', 'Cure Critcal Wounds', 'Death Ward', 'Fickle Winds', 'Fire Snake', 'Hallow', 'Inspect Plague', 'Raise Animal Companion', 'Reprobation', 'Rest Eternal', 'Snake Staff', 'Stoneskin', 'Threefold Aspect', 'Transmute Mud to Rock', 'Transmute Rock to Mud', 'Tree Stride', 'Unhallow', 'Wall of Fire', 'Wall of Thorns', 'Greater Thunderfist', 'Wall of Disease'], ['Age Resistance', 'Antilife Shell', "Mass Bear's Endurance", "Mass Bull's Strength", "Mass Cat's Grace", 'Mass Cure Light Wounds', 'Greater Dispel Magic', 'Dust Form', 'Eagle Aerie', 'Epidemic', 'Find the Path', 'Fire Seeds', 'Ironwood', 'Liveoak', 'Move Earth', "Mass Owl's Wisdom", 'Plague Storm', 'Repel Wood', 'Sirocco', 'Spellstaff', 'Communal Stoneskin', 'Stone Tell', 'Swarm Skin', 'Tar Pool', 'Transport via Plants', 'Wall of Stone', 'Dragonbane', 'Fires of Renewal', 'Tidal Wave'], ['Greater Age Resistance', 'Animate Plants', 'Changestaff', 'Control Weather', 'Creeping Doom', 'Mass Cure Moderate Wounds', 'Fire Storm', 'Heal', 'Rampart', 'Scouring Winds', 'Greater Scrying', 'Siege of Trees', 'Sunbeam', 'Transmute Metal to Wood', 'True Seeing', 'Vortex', 'Wind Walk', 'Pestilence', 'Summon Siren', 'True Form'], ['Animal Shapes', 'Mass Atavism', 'Blood Mist', 'Control Plants', 'Mass Cure Serious Wounds', 'Earthquake', 'Euphoric Tranquility', 'Finger of Death', 'Frightful Aspect', 'Repel Metal or Stone', 'Reverse Gravity', 'Seamantle', 'Stormbolts', 'Sunburst', 'Wall of Lava', 'Whirlwind', 'Word of Recall', 'Cyclone Barrier', 'Greater Ice Mirror', 'Peace Aura'], ['Antipathy', 'Clashing Rocks', 'Mass Cure Critical Wounds', 'Elemental Swarm', 'Foresight', 'Polar Midnight', 'Regenerate', 'Shambler', 'Shapechange', 'Greater Siege of Trees', 'Storm of Vengeance', 'Summon Elder Worm', 'Summon Froghemoth', 'Sympathy', 'Tsunami', 'Winds of Vengeance', 'World Wave', 'Avalanche', 'Glacier', 'Typhoon']]
# PALADIN SPELLS - [[1st], [2nd], [3rd], [4th]]
paladinSpells = [['Animal Purpose Training', 'Aspect of the Nightingale', 'Bed of Iron', 'Bless', 'Blessed Fist', 'Blessing of the Watch', 'Bless Water', 'Bless Weapon', 'Bowstaff', 'Challenge Evil', 'Compel Hostility', 'Create Water', 'Cure Light Wounds', "Deadeye's Water", 'Detect Charm', 'Detect Poison', 'Detect the Faithful', 'Detect Undead', 'Diagnose Disease', 'Divine Favor', 'Emblazon Crest', 'Empower Holy Water', 'Endure Elements', 'Enhance Water', 'Firebelly', 'Ghostbane Dirge', 'Grace', 'Haze of Dreams', "Hero's Defiance", 'Honeyed Tongue', 'Horn of Pursuit', 'Ironbeard', 'Keep Watch', "Knight's Calling", 'Know the Enemy', 'Liberating Command', 'Linebreaker', 'Litany of Sloth', 'Longshot', 'Magic Weapon', 'Protection from Chaos/Evil', 'Rally Point', 'Read Magic', 'Resistance', 'Lesser Restoration', 'Sanctify Corpse', 'Shield of Fortification', 'Stunning Barrier', 'Swift Girding', 'Sun Metal', 'Tactical Acumen', 'Touch of Truthtelling', 'Tracking Mark', 'Unbreakable Heart', 'Veil of Positive Energy', 'Virtue', 'Wartrain Mount', 'Weapons Against Evil', 'Word of Resolve'], ['Abeyance', 'Lesser Angelic Aspect', 'Arrow of Law', 'Aura of Greater Courage', 'Bestow Grace', 'Bestow Weapon Proficiency', 'Blade Tutors Spirit', 'Blessing of Courage and Life', 'Blessings of Luck and Resolve', 'Blinding Ray', 'Bullet Ward', 'Bulls Strength', 'Carry Companion', 'Corruption Resistance', 'Delay Disease', 'Delay Poison', 'Divine Arrow', 'Divine Illumination', 'Eagles Splendor', 'Effortless Armor', 'Communal Endure Elements', 'Fairness', 'Fire of Entanglement', 'Holy Shield', 'Instant Armor', 'Ironskin', 'Life Shield', 'Light Lance', 'Litany of Defense', 'Litany of Eloquence', 'Litany of Entanglement', 'Litany of Righteousness', 'Litany of Warding', 'Magic Siege Engine', 'Martyrs Bargain', 'Owls Wisdom', 'Paladins Sacrifice', 'Communal Protection from Chaos', 'Communal Protection from Evil', 'Remove Paralysis', 'Righteous Vigor', 'Resist Energy', 'Sacred Bond', 'Sacred Space', 'Saddle Surge', 'Shield Companion', 'Shield Other', 'Soothing Word', 'Undetectable Alignment', 'Vestment of the Champion', 'Wake of Light', 'Weapon of Awe', 'Widen Auras', 'Zone of Truth'], ['Accept Affliction', 'Angelic Aspect', "Archon's Aura", 'Aura of Inviolate Ownership', 'Bestow Auras', 'Blade of Bright Victory', 'Blessing of the Mole', 'Burst of Speed', 'Cure Moderate Wounds', 'Daybreak Arrow', 'Daylight', 'Deadly Juggernaut', 'Communal Delay Poison', 'Discern Lies', 'Dispel Magic', 'Divine Transfer', 'Fire of Judgement', 'Mass Ghostbane Dirge', 'Heal Mount', 'Heroic Fortune', 'Holy Whisper', 'Litany of Escape', 'Litany of Sight', 'Magic Circle Against Chaos/Evil', 'Greater Magic Weapon', 'Mantle of Calm', 'Marks of Forbiddance', 'Prayer', 'Remove Blindness/Deafness', 'Remove Curse', 'Resilient Reservoir', 'Communal Resist Energy', 'Sanctify Armor', 'Sanctify Weapons', 'Greater Shield of Fortification', 'Greater Stunning Barrier', 'Wrathful Mantle'], ['Greater Angelic Aspect', "Archon's Trumpet", 'Bestow Grace of the Champion', 'Blaze of Glory', 'Mass Blessings of Luck and Resolve', 'Break Enchantment', 'Bloodsworn Retribution', 'Burst of Glory', 'Chains of Light', "Crusader's Edge", 'Cure Serious Wounds', 'Death Ward', 'Dimensional Blade', 'Disepl Chaos', 'Dispel Evil', 'Eaglesoul', 'Fire of Vengeance', 'Forced Repentance', 'Forceful Strike', 'Guardian of Faith', 'Holy Sword', "King's Castle", 'Litany of Thunder', 'Litany of Vengeance', 'Greater Magic Siege Engine', 'Mark of Justice', 'Neutralize Poison', 'Oath of Peace', 'Paragon Surge', "Planeslayer's Call", 'Raise Animal Companion', 'Reprobation', 'Sacrificial Oath', 'Shield of Dawn', 'Stay the Hand', 'Symbol of Healing']]
# RANGER SPELLS
rangerSpells = [['Ant Haul', 'Aspect of the Falcon', 'Call Animal', 'Cloak of Shade', 'Dancing Lanter', 'Detect Aberration', 'Feather Step', 'Glide', 'Gravity Bow', "Hunter's Howl", 'Keen Senses', 'Lead Blades', 'Negate Aroma', 'Residual Tracking', 'Tireless Pursuit', 'Alarm', 'Animal Messenger', 'Calm Animals', 'Charm Animal', 'Delay Poison', 'Detect Animals or Plants', 'Detect Poison', 'Detect Snares and Pits', 'Endure Elements', 'Entangle', 'Hide from Animals', 'Jump', 'Longstrider', 'Magic Fang', 'Pass without Trace', 'Read Magic', 'Resist Energy', 'Speak with Animals', "Summon Nature's Ally I"], ['Barkskin', "Bear's Endurance", "Cat's Grace", 'Cure Light Wounds', 'Hold Animal', "Owl's Wisdom", 'Protection from Energy', 'Snare', 'Speak with Plants', 'Spike Growth', "Summon Nature's Ally II", 'Wind Wall', 'Accelerate Poison', 'Allflood', 'Arrow Eruption', 'Aspect of the Bear', 'Bloodhound', 'Campfire Wall', 'Chameleon Stride', 'Create Treasure Map', 'Eagle Eye', 'Guiding Star', 'Hide Campsite', "Hunter's Eye", 'Lockjaw', 'Perceive Cues', 'Protective Spirit', 'Slipstream', 'Stone Call', 'Versatile Weapon'], ['Aspect of the Stag', 'Bloody Claws', 'Cloak of Winds', 'Mass Feather Step', 'Instant Enemy', 'Life Bubble', 'Strong Jaw', 'Tireless Pursuers', 'Venomous Bolt', 'Command Plants', 'Cure Moderate Wounds', 'Darkvision', 'Diminish Plants', 'Greater Magic Fang', 'Neutralize Poison', 'Plant Growth', 'Reduce Animal', 'Remove Disease', 'Repel Vermin', "Summon Nature's Ally III", 'Tree Shape', 'Water Walk'], ['Animal Growth', 'Commune with Nature', 'Cure Serious Wounds', 'Freedom of Movement', 'Nondetection', "Summon Nature's Ally IV", 'Tree Stride', 'Aspect of the Wolf', 'Blessing of the Salamander', 'Bow Spirit', 'Grove of Respite']]
# BEGUILER SPELLS
beguilerSpells = [['Dancing Lights', 'Daze', 'Detect Magic', 'Ghost Sound', 'Message', 'Open/Close', 'Read Magic'], ['Charm Person', 'Color Spray', 'Comprehend Languages', 'Detect Secret Doors', 'Disguise Self', 'Expeditious Retreat', 'Hypnotism', 'Mage Armor', 'Obscuring Mist', 'Rouse', 'Silent Image', 'Sleep', 'Undetectable Alignment', 'Whelm'], ['Blinding Color Surge', 'Blur', 'Daze Monster', 'Detect Thoughts', 'Fog Cloud', 'Glitterdust', 'Hypnotic Pattern', 'Invisibility', 'Knock', 'Minor Image', 'Mirror Image', 'Misdirection', 'See Invisibility', 'Silence', 'Spider Climb', 'Stay the Hand', 'Touch of Idiocy', 'Vertigo', 'Whelming Blast'], ['Arcane Sight', 'Clairaudience/Clairvoyance', 'Crown of Veils', 'Deep Slumber', 'Dispel Magic', 'Displacement', 'Glibess', 'Halt', 'Haste', 'Hesitate', 'Hold Person', 'Inevitable Defeat', 'Invisibility Sphere', 'Legion of Sentinels', 'Major Image', 'Nondetection', 'Slow', 'Suggestion', 'Vertigo Field', 'Zone of Silence'], ['Charm Monster', 'Confusion', 'Crushing Despair', 'Freedom of Movement', 'Greater Invisibility', 'Locate Creature', 'Greater Mirror Image', 'Phantom Battle', 'Rainbow Pattern', 'Solid Fog', 'Mass Whelm'], ['Break Enchantment', 'Dominate Person', 'Swift Etherealness', 'Feeblemind', 'Friend to Foe', 'Hold Monster', 'Incite Riot', 'Mind Fog', "Rary's Telepathic Bond", 'Seeming', 'Sending'], ['Greater Dispel Magic', 'Mislead', 'Overwhelm', 'Repulsion', 'Shadow Walk', 'Mass Suggestion', 'True Seeing', 'Veil'], ['Greater Arcane Sight', 'Ethereal Jaunt', 'Mass Hold Person', 'Mass Invisibility', 'Phase Door', 'Power Word: Blind', 'Project Image', 'Spell Turning'], ['Demand', 'Discern Location', 'Mind Blank', 'Moment of Prescience', 'Power Word: Stun', 'Scintillating Pattern', 'Screen'], ['Dominate Monster', 'Etherealness', 'Foresight', 'Mass Hold Monster', 'Power Word: Kill', 'Time Stop']]
beguilerADSpells = {1 : ['Bungle','Delusional Pride', 'Vanish', 'Ventriloquism'], 3 : ['Vision of Hell', 'False Pain', 'Secret Speech', 'Weapon of Nightmares', 'Curse of Truth', 'Euphoria', 'Glossolalia', 'Surge'], 5 : ['Dream', 'False Vision', 'Shadow Evocation'], 7 : ['Insanity', 'Waves of Ecstasy', 'Greater Shadow Conjuration'], 9 : ['Shades', 'Weird', 'Heroic Invocation']}
# DREAD NERCROMANCER SPELLS
dreadNecroSpells = [['Bane', 'Bestow Wound', 'Cause Fear', 'Chill Touch', 'Detect Magic', 'Detect Undead', 'Doom', 'Hide From Undead', 'Inflict Light Wounds', 'Ray of Enfeeblement', 'Summon Undead I', 'Undetectable Alignment'], ['Blindness/Deafness', 'Command Undead', 'Darkness', 'Death Knell', 'False Life', 'Gentle Repose', 'Ghoul Touch', 'Inflict Moderate Wounds', 'Scare', 'Spectral Hand', 'Summon Swarm', 'Summon Undead II'], ['Crushing Depspair', 'Halt Undead', 'Inflict Serious Wounds', 'Ray of Exhaustion', 'Speak With Dead', 'Summon Undead III', 'Vampiric Touch'], ['Animate Dead', 'Bestow Curse', 'Contagion', 'Death Ward', 'Dispel Magic', 'Enervation', "Evard's Black Tentacles", 'Fear', 'Giant Vermin', 'Inflict Critical Wounds', 'Phantasmal Killer', 'Poison', 'Summon Undead IV'], ['Blight', 'Cloudkill', 'Greater Dispel Magic', 'Fire In The Blood', 'Mass Inflict Light Wounds', 'Insect Plague', 'Magic Jar', 'Nightmare', 'Oath of Blood', 'Lesser Planar Binding', 'Slay Living', 'Summon Undead V', 'Undeath to Death', 'Unhallow', 'Waves of Fatigue'], ['Acid Fog', 'Circle of Death', 'Create Undead', 'Eyebite', 'Geas/Quest', 'Harm', 'Mass Inflict Moderate Wounds', 'Planar Binding', 'Waves of Exhaustion'], ['Control Undead', 'Destruction', 'Finger of Death', 'Greater Harm', 'Mass Inflict Serious Wounds', 'Song of Discord', 'Vile Death'], ['Create Greater Undead', 'Horrid Wilting', 'Mass Inflict Critical Wounds', 'Symbol of Death'], ['Energy Drain', 'Mass Harm', 'Imprison Soul', 'Plague of Undead', 'Wail of the Banshee']]
dreadNecroADSpells = {2 : ['Languor', 'Mute', 'Angry Wound'], 4: ['Boneshatter', 'Shadow Projection'], 6 : ['Eyebite', 'Greater Contagion'], 8 : ['Orb of the Void'], 9 : ['Astral Projection', 'Canopic Conversion', 'Mass Suffocation']}
# WARMAGE SPELLS
warmageSpells = [['Acid Splash', 'Disrupt Undead', 'Light', 'Ray of Frost'], ['Accuracy', 'Lesser Acid Orb', 'Burning Hands', 'Chill Touch', 'Lesser Cold Orb', 'Lesser Electric Orb', 'Lesser Fire Orb', 'Fist of Stone', 'Hail of Stone', 'Magic Missile', 'Shocking Grasp', 'Lesser Sonic Orb', 'True Strike'], ['Blades of Fire', 'Continual Flame', 'Fire Trap', 'Fireburst', 'Flaming Sphere', 'Ice Knife', "Melf's Acid Arrow", 'Pyrotechnics', 'Scorching Ray', 'Shater', 'Whirling Blade'], ['Fire Shield', 'Fireball', 'Flame Arrow', 'Gust of Wind', 'Ice Storm', 'Lightning Bolt', 'Poison', 'Ring of Blades', 'Sleet Storm', 'Stinking Cloud'], ['Blast of Flame', 'Contagion', "Evard's Black Tentacles", 'Orb of Acid', 'Orb of Cold', 'Orb of Electricity', 'Orb of Fire', 'Orb of Force', 'Orb of Sound', 'Phantasmal Killer', 'Shout', 'Wall of Fire'], ['Arc of Lightning', 'Cloudkill', 'Cone of Cold', 'Mass Fire Shield', 'Greater Fireburst', 'Flame Strike', 'Prismatic Ray'], ['Acid Fog', 'Blade Barrier', 'Chain Lightning', 'Circle of Death', 'Disentigrate', 'Fire Seeds', "Otiluke's Freezing Shphere", "Tenser's Transformation"], ['Delayed Blast Fireball', 'Earthquake', 'Finger of Death', 'Fire Storm', "Mordenkainen's Sword", 'Prismatic Spray', 'Sunbeam', 'Waves of Exhaustion'], ['Horrid Wilting', 'Incendiary Cloud', 'Polar Ray', 'Prismatic Wall', 'Scintillating Pattern', 'Greater Shout', 'Sunburst'], ['Elemental Swarm', 'Implosion', 'Meteor Swarm', 'Prismatic Sphere', 'Wail of the Banshee', 'Weird']]
warmageADSpells = {1 : ['Floating Disk', 'Hydraulic Push', 'Airblast', 'Caustic Cloud', 'Wind Tunnel'], 3 : ['Battering Blast', 'Diamond Spray', 'Force Punch', 'Hydraulic Torrent', 'Object Grenade', 'Wall of Water'], 5 : ['Fire Snake', 'Icy Prison', 'Mass Pain Strike', 'Tempest Hammer'], 8 : ['Clenched Fist', 'Telekinetic Sphere', 'Vortex']}
# DOMAIN SPELLS
domainSpells = {'Air Domain' : ['Obscuring Mist', 'Wind Wall', 'Gaseous Form', 'Air Walk', 'Control Winds', 'Chain Lightning', 'Elemental Body IV', 'Whirlwind', 'Elemental Swarm'], 'Animal Domain' : ['Calm Animals', 'Hold Animal', 'Dominate Animal', "Summon Nature's Ally IV", 'Beast Shape III', 'Antilife Shell', 'Animal Shapes', "Summon Nature's Ally VIII", 'Shapechange'], 'Earth Domain' : ['Magic Stone', 'Soften Earth and Stone', 'Stone Shape', 'Spike Stones', 'Wall of Stone', 'Stoneskin', 'Elemental Body IV', 'Earthquake', 'Elemental Swarm'], 'Fire Domain' : ['Burning Hands', 'Produce Flame', 'Fireball', 'Wall of Fire', 'Fire Shield', 'Fire Seeds', 'Elemental Body IV', 'Incendiary Cloud', 'Elemental Swarm'], 'Plant Domain' : ['Entangle', 'Barkskin', 'Plant Growth', 'Command Plants', 'Wall of Thorns', 'Repel Wood', 'Animate Plants', 'Control Plants', 'Shambler'], 'Water Domain' : ['Obscuring Mist', 'Fog Cloud', 'Water Breathing', 'Control Water', 'Ice Storm', 'Cone of Cold', 'Elemental Body IV', 'Horrid Wilting', 'Elemental Swarm'], 'Weather Domain' : ['Obscuring Mist', 'Fog Cloud', 'Call Lightning', 'Sleet Storm', 'Ice Storm', 'Control Winds', 'Control Weather', 'Whirlwind', 'Storm of Vengeance']}
chaosMantle = [['Destiny Dissonance (1)', 'Matter Agitation (1)'], ['Distracting Shout (3)'], [], ['Personality Parasite (7)'], ['Catapsi (9)'], ['Inconstant Location (11)'], [], ['Chaos Fissure (15)'], []]
communicationMantle = [['Attration (1)', 'Psionic Charm (1)', 'Missive (1)', 'Telempathic Projection (1)'], ['Mass Missive (3)', 'Psionic Suggestion (3)', 'Psionic Tongues (3)'], [], ['Correspond (7)'], ['Metaconcert (9)'], [], [], [], ['Metafaculty (17)']]
conflictMantle = [['Metaphysical Weapon (1)', 'Offensive Prescience (1)'], ["Psionic Lion's Charge (3)"], ['Dimension Slide (5)'], ['Immovability (7)'], ['Psychic Crush (9)', 'Graft Weapon (9)'], [], [], ['Spirit of War (15)'], []]
consumptionMantle = [['Hungry Touch (1)'], ['Feat Leech (3)'], [], ['Power Leech (7)'], [], [], ['Power Thief (13)', 'Decebreate (13)'], [], ['Apopsi (17)']]
corruptionAndMadnessMantle = [['Psionic Daze (1)', 'Primal Fear (1)'], ['Brain Lock (3)'], ['Mental Turmoil (5)'], ['Mindwipe (7)'], [], [], ['Decebreate (13)', 'Insanity (13)'], [], ['Microcosm (17)']]
creationMantle = [['Astral Construct (1)', 'Psionic Minor Creation (1)'], [], [], ['Psionic Fabricate (7)'], ['Psionic Major Creation (9)'], ['Greater Psionic Fabricate (11)'], [], [], ['True Creation (17)']]
deathMantle = [['Stygian Discernment (1)'], ['Stygian Ray (3)'], ['Psionic Speak with Dead (5)'], ['Death Urge (7)'], ['Stygian Dominion (9)'], [], ['Crisis of Life (13)'], ['Recall Death (15)', 'Stygian Veil (15)'], []]
deceptionMantle = [['Psionic Charm (1)'], ['Cloud Mind (3)', 'Concealing Amorpha (3)'], ['False Sensory Input (5)', 'Escape Detection (5)'], [], [], ['Mass Cloud Mind (11)'], [], ['Bend Reality (15)'], []]
destructionMantle = [['Dissipating Touch (1)'], ['Dissolving Touch (3)', 'Dissolving Weapon (3)'], ['Dispel Psionics (5)'], [], [], ['Psionic Disintegrate (11)'], ['Ultrablast (13)'], [], ['Intellect Bomb (17)']]
elementsMantle = [['Control Flames (1)', 'Elemental Steward (1)'], ['Control Air (3)', 'Earth Walk (3)'], ['Breathless (5)'], [], ['Adapt Body (9)'], ['Blackstone Hammer (11)'], [], [], ['Tornado Blast (17)']]
energyMantle = [['Energy Ray (1)'], ['Energy Push (3)'], ['Energy Bolt (5)', 'Energy Burst (5)', 'Energy Wall (5)'], [], ['Energy Manipulation (9)'], [], ['Energy Wave (13)'], [], []]
evilMantle = [['Psionic Protection from Good (1)'], ['Psionic Death Knell (3)'], [], ['Planar Apotheosis (7)'], ['Fiendish Conduit (9)'], ['Planar Embrace (11)'], [], ['Dark Despair (15)'], []]
fateMantle = [['Defensive Precognition (1)', 'Offensive Precognition (1)'], ['Clairvoyant Sense (3)'], [], ['Remote Viewing (7)'], [], ['Greater Precognition (11)'], ['Fate of One (13)'], [], ['Metafaculty (17)']]
forceMantle = [['Force Screen (1)', 'Deflection Field (1)'], ['Concussion Blast (3)'], ['Telekinetic Force (5)', 'Ethereal Volley (5)'], ['Telekinetic Maneuever (7)'], [], ['Concussive Detonation (11)'], [], ['Psionic Telekinetic Sphere (15)'], []]
freedomMantle = [['Dimension Hop (1)'], ['Hustle (3)'], [], ['Psionic Fly (7)'], ['Psionic Freedom of Movement (9)', 'Psionic Teleport (9)'], ['Evade Burst\t (11)'], [], ['Psionic Greater Teleport (15)'], []]
goodMantle = [['Psionic Protection from Evil (1)'], ['Empathic Transfer (3)'], [], ['Planar Apotheosis (7)'], ['Celestial Conduit (9)'], ['Planar Embrace (11)'], [], ['Greater Glory (15)'], []]
guardianMantle = [['Deaden Blow (1)', 'Thicken Skin (1)'], ['Damp Power (3)'], ['Dispel Psionics (5)'], ['Wall of Ectoplasm (7)'], ['Protection from Psionics (9)'], ['Mind over Energy (11)'], [], ['Psionic Iron Body (15)'], []]
justiceMantle = [['Call Weaponry (1)'], ['Call Armor (3)', 'Incite Bravery (3)', 'Psionic Zone of Truth (3)'], [], ['Aura of Sight (7)', 'Psionic Discern Lies (7)'], ['Psionic True Seeing (9)'], ['Perfect Riposte (11)'], ['Reddopsi (13)'], [], []]
knowledgeMantle = [['Call to Mind (1)', 'Detect Psionics (1)', 'Detect Teleportation (1)', 'Know Direction and Location (1)'], ['Detect Hostile Intent (3)', 'Psionic Identify (3)', 'Object Reading (3)'], ['Touchsight (5)'], ['Detect Remote Viewing (7)', 'Trace Teleport (7)'], [], ['Psychometry (11)'], [], [], []]
lawMantle = [['Grip of Iron (1)', 'Hammer (1)'], ['Psionic Lock (3)'], ['Heavy Earth (5)'], ['Immovability (7)', 'Steadfast Perception (7)'], ['Tower of Iron Will (9)'], [], [], ['Psionic Iron Body (15)'], ['Timeless Body (17)']]
lifeMantle = [['Touch of Health (1)'], ['From the Brink (3)'], ['Body Purification (5)'], ['Stygian Ward (7)'], ['Psionic Revivify (9)'], ['Mend Wounds (11)', 'Psionic Restoration (11)'], [], ['True Metabolism (15)'], []]
lightAndDarknessMantle = [['Control Light (1)', 'Elfsight (1)', 'My Light (1)'], ['Claws of Darkness (3)'], [], ['Light Beam (7)'], ['Psionic Shadow Walk (9)'], [], [], ['Light Burst (15)'], []]
magicMantle = [['Metaphysical Weapon (1)'], [], ['Dispel Psionics (5)'], [], ['Power Resistance (9)'], ['Psionic Analyze Dweomer (11)', 'Null Psionics Field (11)'], [], ['Psionic Protection from Spells (15)'], []]
mentalPowerMantle = [['Mind Thrust (1)'], ['Id Insinuation (3)', 'Mental Disruption (3)'], ['Mind Trap (5)'], ['Intellect Fortress (7)'], ['Psychic Crush (9)'], ['Cranial Deluge (11)'], [], ['Hypercognition (15)'], []]
naturalWorldMantle = [['Chameleon (1)', 'Metaphysical Claw (1)', 'Stone Mind (1)'], ['Animal Affinity (3)', 'Psionic Scent (3)'], [], ['Metamorphosis (7)'], ['Oak Body (9)'], [], ['Psionic Animate Plants (13)'], [], ['Psionic Earthquake (17)']]
painAndSufferingMantle = [['Disable (1)'], ['Inflict Pain (3)', 'Recall Agony (3)'], ['Hostile Empathic Transfer (5)', 'Forced Share Pain (5)'], ['Empathic Feedback (7)'], ['Psychotic Break (9)'], ['Fuse Flesh (11)'], [], [], ['Pain Affinity Field (17)']]
physicalPowerMantle = [['Adrenaline Boost (1)', 'Vigor (1)'], ['Animal Affinity (3)'], ['Graft Weapon (5)'], [], ['Psychofeedback (9)'], [], ['Oak Body (13)'], ['True Metabolism (15)'], []]
thePlanesMantle = [['Astral Traveler (1)'], [], ['Astral Caravan (5)'], ['Psionic Dimensional Anchor (7)', 'Psionic Dismissal (7)'], ['Psionic Plane Shift (9)'], ['Planar Champion (11)'], ['Psionic Ethereal Jaunt (13)'], [], ['Psionic Etherealness (17)']]
reposeMantle = [['Empty Mind (1)'], ['Serenity (3)', 'Empathic Transfer (3)'], ['Solicit Psicrystal (5)'], ['Steadfast Perception (7)'], [], ['Suspend Life (11)'], ['Personal Mind Blank (13)'], [], []]
timeMantle = [['Deceleration (1)'], ['Sustenance (3)'], ['Time Hop (5)'], [], ['Anticipatory Strike (9)'], ['Temporal Acceleration (11)'], [], ['Mass Time Hop (15)'], ['Time Regression (17)']]
pwPowers = [['Astral Traveler (1)', 'Attraction (1)', 'Bolt (1)', 'Call to Mind (1)', 'Catfall (1)', 'Conceal Thoughts (1)', 'Control Flames (1)', 'Control Light (1)', 'Create Sound (1)', 'Crystal Shard (1)', 'Psionic Daze (1)', 'Deceleration (1)', 'Deja Vu (1)', 'Demoralize (1)', 'Detect Psionics (1)', 'Disable (1)', 'Dissipating Touch (1)', 'Distract (1)', 'Echo Protection (1)', 'Empathy (1)', 'Empty Mind (1)', 'Energy Ray (1)', 'Entangling Ectoplasm (1)', 'Far Hand (1)', 'Float (1)', 'Force Screen (1)', 'Psionic Grease (1)', 'Hammer (1)', 'Inertial Armor (1)', 'Know Direction and Location (1)', 'Matter Agitation (1)', 'Mind Thrust (1)', 'Missive (1)', 'My Light (1)', 'Defensive Precognition (1)', 'Offensive Precognition (1)', 'Offensive Prescience (1)', 'Sense Link (1)', 'Skate (1)', 'Synesthete (1)', 'Telempathic Projection (1)', 'Vigor (1)'], ['Bestow Power (3)', 'Biofeedback (3)', 'Body Equilibrium (3)', 'Cloud Mind (3)', 'Concealing Amorpha (3)', 'Concussion Blast (3)', 'Control Sound (3)', 'Detect Hostile Intent (3)', 'Ego Whip (3)', 'Elfsight (3)', 'Specified Energy Adaptation (3)', 'Energy Push (3)', 'Energy Stun (3)', 'Feat Leech (3)', 'Id Insinuation (3)', 'Psionic Identify (3)', 'Inflict Pain (3)', 'Psionic Knock (3)', 'Psionic Levitate (3)', 'Mental Disruption (3)', 'Mass Missive (3)', 'Psionic Lock (3)', 'Recall Agony (3)', 'Forced Sense Link (3)', 'Share Pain (3)', 'Sustenance (3)', 'Swarm of Crystals (3)', 'Thought Shield (3)', 'Psionic Tongues (3)'], ['Body Adjustment (5)', 'Body Purification (5)', 'Danger Sense (5)', 'Psionic Darkvision (5)', 'Dismiss Ectoplasm (5)', 'Dispel Psionics (5)', 'Energy Bolt (5)', 'Energy Burst (5)', 'Energy Retort (5)', 'Energy Wall (5)', 'Eradicate Invisibility (5)', 'Psionic Keen Edge (5)', 'Mental Barrier (5)', 'Mind Trap (5)', 'Psionic Blast (5)', 'Forced Share Pain (5)', 'Solicit Psicrystal (5)', 'Telekinetic Force (5)', 'Telekinetic Thrust (5)', 'Time Hop (5)', 'Touchsight (5)', 'Ubiquitous Vision (5)'], ['Aura Sight (7)', 'Correspond (7)', 'Death Urge (7)', 'Detect Remote Viewing (7)', 'Psionic Dimension Door (7)', 'Psionic Divination (7)', 'Empathic Feedback (7)', 'Energy Adaptation (7)', 'Psionic Freedom of Movement (7)', 'Intellect Fortress (7)', 'Mindwipe (7)', 'Personality Parasite (7)', 'Power Leech (7)', 'Psychic Reformation (7)', 'Telekinetic Maneuever (7)', 'Trace Teleport (7)', 'Wall of Ectoplasm (7)'], ['Adapt Body (9)', 'Catapsi (9)', 'Ectoplasmic Shambler (9)', 'Incarnate (9)', 'Leech Field (9)', 'Psionic Major Creation (9)', 'Psionic Plane Shift (9)', 'Power Resistance (9)', 'Psychic Crush (9)', 'Shatter Mind Blank (9)', 'Tower of Iron Will (9)', 'Psionic True Seeing (9)'], ['Aura Alteration (11)', 'Breath of the Black Dragon (11)', 'Mass Cloud Mind (11)', 'Psionic Contingency (11)', 'Co-opt Concentration (11)', 'Psionic Disintegrate (11)', 'Fuse Flesh (11)', 'Psionic Overland Flight (11)', 'Remote View Trap (11)', 'Retrieve (11)', 'Suspend Life (11)', 'Temporal Acceleration (11)'], ['Decebreate (13)', 'Divert Teleport (13)', 'Energy Conversion (13)', 'Energy Wave (13)', 'Evade Burst (13)', 'Insanity (13)', 'Personal Mind Blank (13)', 'Psionic Moment of Prescience (13)', 'Oak Body (13)', 'Psionic Phase Door (13)', 'Psionic Sequester (13)', 'Ultrablast (13)'], ['Bend Reality (15)', 'Psionic Iron Body (15)', 'Matter Manipulation (15)', 'Psionic Mind Blank (15)', 'Recall Death (15)', 'Shadow Body (15)', 'Psionic Greater Teleport (15)', 'True Metabolism (15)'], ['Affinity Field (17)', 'Apopsi (17)', 'Assimilate (17)', 'Psionic Etherealness (17)', 'Microcosm (17)', 'Reality Revision (17)', 'Timeless Body (17)']]
egoistPowers = [['Thicken Skin (1)'], ['Animal Affinity (3)', 'Chameleon (3)', 'Empathic Transfer (3)'], ['Ectoplasmic Form (5)', 'Hustle (5)'], ['Metamorphosis (7)', 'Psychic Vampire (7)'], ['Psionic Revivify (9)', 'Psychofeedback (9)', 'Restore Extremity (9)'], ['Psionic Restoration (11)'], ['Fission (13)'], ['Fusion (15)'], ['Greater Metamorphosis (17)']]
kineticistPowers = [['Control Object (1)'], ['Control Air (3)', 'Energy Missile (3)'], ['Energy Cone (5)'], ['Control Body (7)', 'Energy Ball (7)', 'Inertial Barrier (7)'], ['Energy Current (9)', 'Fiery Discorporation (9)'], ['Dispelling Buffer (11)', 'Null Psionics Field (11)'], ['Reddopsi (13)'], ['Psionic Telekinetic Sphere (15)'], ['Tornado Blast (17)']]
nomadPowers = [['Burst (1)', 'Detect Teleportation (1)'], ['Dimension Swap (3)', 'Psionic Levitate (3)'], ['Astral Caravan (5)'], ['Psionic Dimensional Anchor (7)', 'Psionic Dismissal (7)', 'Psionic Fly (7)'], ['Baleful Teleport (9)', 'Psionic Teleport (9)', 'Teleport Trigger (9)'], ['Psionic Banishment (11)'], ['Dream Travel (13)', 'Psionic Ethereal Jaunt (13)'], ['Mass Time Hop (15)'], ['Psionic Teleportation Circle (17)', 'Time Regression (17)']]
seerPowers = [['Destiny Dissonance (1)', 'Precognition (1)'], ['Clairvoyant Sense (3)', 'Object Reading (3)', 'Sensitivity to Psychic Impressions (3)'], ['Escape Detection (5)', 'Fate Link (5)'], ['Anchored Navigation (7)', 'Remote Viewing (7)'], ['Clairtangent Hand (9)', 'Second Chance (9)'], ['Greater Precognition (11)'], ['Fate of One (13)'], ['Hypercognition (15)'], ['Metafaculty (17)']]
shaperPowers = [['Astral Construct (1)', 'Psionic Minor Creation (1)'], ['Psionic Repair Damage (3)'], ['Greater Concealing Amorpha (5)', 'Ectoplasmic Cocoon (5)'], ['Psiconic Fabricate (7)', 'Quintessence (7)'], ['Hail of Crystals (9)'], ['Crystallize (11)', 'Greater Psionic Fabricate (11)'], ['Mass Ectoplasmic Cocoon (13)'], ['Astral Seed (15)'], ['Genesis (17)', 'True Creation (17)']]
telepathPowers = [['Psionic Charm (1)', 'Mindlink (1)'], ['Aversion (3)', 'Brain Lock (3)', 'Read Thoughts (3)', 'Psionic Suggestion (3)'], ['Crisis of Breath (5)', 'Hostile Empathic Transfer (5)', 'False Sensory Input (5)'], ['Psionic Dominate (7)', 'Thieving Mindlink (7)', 'Psionic Modify Memory (7)', 'Shcism (7)'], ['Metaconcert (9)', 'Mind Probe (9)'], ['Mind Switch (11)'], ['Crisis of Life (13)'], ['Mind Seed (15)'], ['True Mind Switch (17)', 'Psychic Chirurgery (17)']]

#WEAPONS
weapons = {'Hand' : ['1d3',20,2], 'Greataxe' : ['1d12',20,3], 'Handaxe' : ['1d6',20,3], 'Battleaxe' : ['1d8',20,3], 'Waraxe' : ['1d10',20,3], 'Greatsword' : ['2d6',19,2], 'Longsword' : ['1d8',19,2], 'Katana' : ['1d10',19,2], 'Dagger' : ['1d4',19,2], 'Shortsword' : ['1d6',19,2], 'Kukri' : ['1d4',18,2], 'Rapier' : ['1d6',18,2], 'Composite Shortbow' : ['1d6',20,3], 'Composite Longbow' : ['1d8',20,3], 'Cestus' : ['1d4',19,2], 'Punching Dagger' : ['1d4',20,3], 'Double Crossbow' : ['1d8',19,2], 'Handcrossbow' : ['1d4',19,2], 'Heavy Repeating Crossbow' : ['1d8',19,2], 'Dire Flail' : ['1d8',20,2], 'Kusarigama' : ['1d6',20,2], 'Two-Bladed Sword' : ['1d8',19,2], 'Pistols' : ['1d8',20,4], 'Blunderbuss' : ['1d8',20,2], 'Musket' : ['1d12',20,4], 'Light Hammer' : ['1d6',20,3], 'Warhammer' : ['1d8',20,3], 'Greathammer' : ['1d12',20,3], 'Nunchaku' : ['1d6',20,2], 'Guisarme' : ['2d4',20,3], 'Halberd' : ['1d10',20,3], 'Javelins' : ['1d6',20,2], 'Harpoon' : ['1d8',20,3], 'Lance' : ['1d8',20,3], 'Spear' : ['1d8',20,3], 'Sling' : ['1d6',20,2], 'Shurikens' : ['1d2',20,2], 'Throwing Knives' : ['1d4',19,2], 'Falchion' : ['2d4',18,2], 'Scythe' : ['1d4',20,4], 'Spiked Iron Light Shield' : ['1d4',20,2]}

##########################################
# This is the class to store, manage, and generate a character
##########################################
class Character(object):
	# sets up some dummy values and whatnot. 
	def __init__(self,name,level):
		self.name = name
		self.level = level
		self.clas = ''
		self.race = ''
		self.hitPoints = 0
		self.finalRolls = [0,0,0,0,0,0]
		self.strength = 0
		self.dexterity = 0
		self.constitution = 0
		self.intelligence = 0
		self.wisdom = 0
		self.charisma = 0
		self.strMod = 0
		self.dexMod = 0
		self.conMod = 0
		self.intMod = 0
		self.wisMod = 0
		self.chaMod = 0
		self.fortSave = 0
		self.refSave = 0
		self.willSave = 0
		self.specialList = []
		self.featList = []
		self.skillsAtMax = 0
		self.skillBonus = {}
		self.classSkills = []

		# self.powerList = []
		# self.powerPoints = 0
		# self.spellsPerDay = []

		self.BAB = 0
		self.languagesKnown = []
		self.armorClass = 10
		self.touchArmorClass = 10
		self.flatFootedArmorClass = 10
		self.equipment = {'Armor' : '', 'Main Hand' : '+0 Hand', 'Off Hand' : '+0 Hand'}
		self.tags = set()

		
	# function to roll ability scores in the traditional way
	# 4d6 drop lowest for each stat. If an individual roll is less than 7 we throw it out
	# If the sum of the rolled ability score modifiers is less than 1 all six scores are
	# rolled again. 
	def rollStats(self):
		rolls = [0, 0, 0, 0]
		mods = [0, 0, 0, 0, 0, 0]
		for i in xrange(6):
			while self.finalRolls[i] < 6: # stat totals less than 6 are thrown out and we roll again
				for j in xrange(4): # roll 4d6
					rolls[j] = random.randint(1,6)
					
				self.finalRolls[i] = sum(rolls) - min(rolls) # drop the lowest die roll and add the rest together
				mods[i] = self.calcMod(self.finalRolls[i])

		return self.finalRolls

	# function to assignAbilityScoresByClass. also increases the character's most important stat once for every 4 levels
	# for use if the class has been chosen by some means other than the chooseclass() algorithm as that 
	# function determines class based on ability scores. 
	# this one looks at the character's class before choosing where to put its rolls
	# i tried to just give the character the essentials for their class and usually also
	# constitution, but after that leave it up to the virtual dice.
	def assignAbilityScoresByClass(self,rolls):
		print 'Assigning ability scores...'
		print 'Rolls: {}'.format(rolls)
		if self.clas == 'Ardent':
			self.wisdom = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.dexterity = rolls[1]
			self.intelligence = rolls[2]
			self.charisma = rolls[3]

		elif self.clas == 'Barbarian':
			self.strength = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.constitution = rolls.pop(rolls.index(max(rolls)))
			self.dexterity = rolls.pop(rolls.index(max(rolls)))

			self.intelligence = rolls[0]
			self.wisdom = rolls[1]
			self.charisma = rolls[2]

		elif self.clas == 'Bard':
			self.charisma = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.dexterity = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.intelligence = rolls[1]
			self.wisdom = rolls[2]

		elif self.clas == 'Beguiler':
			self.intelligence = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.charisma = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))
			
			self.strength = rolls[0]
			self.dexterity = rolls[1]
			self.wisdom = rolls[2]

		elif self.clas == 'Crusader':
			self.constitution = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.charisma = rolls.pop(rolls.index(max(rolls)))
			self.strength = rolls.pop(rolls.index(max(rolls)))

			self.dexterity = rolls[0]
			self.intelligence = rolls[1]
			self.wisdom = rolls[2]

		elif self.clas == 'Dread Necromancer':
			self.charisma = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.dexterity = rolls[1]
			self.intelligence = rolls[2]
			self.wisdom = rolls[3]

		elif self.clas == 'Druid':
			self.wisdom = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.dexterity = rolls[1]
			self.intelligence = rolls[2]
			self.charisma = rolls[3]

		elif self.clas == 'Fighter':
			self.strength = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.dexterity = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.intelligence = rolls[0]
			self.wisdom = rolls[1]
			self.charisma = rolls[2]

		elif self.clas == 'Paladin':
			self.constitution = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.charisma = rolls.pop(rolls.index(max(rolls)))
			self.strength = rolls.pop(rolls.index(max(rolls)))

			self.dexterity = rolls[0]
			self.intelligence = rolls[1]
			self.wisdom = rolls[2]

		elif self.clas == 'Psion':
			self.intelligence = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.dexterity = rolls[1]
			self.wisdom = rolls[2]
			self.charisma = rolls[3]

		elif self.clas == 'Ranger':
			self.dexterity = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.strength = rolls.pop(rolls.index(max(rolls)))
			self.wisdom = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.intelligence = rolls[0]
			self.charisma = rolls[1]

		elif self.clas == 'Rogue':
			self.dexterity = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.intelligence = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.wisdom = rolls[1]
			self.charisma = rolls[2]

		elif self.clas == 'Swordsage':
			self.dexterity = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.wisdom = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.intelligence = rolls[1]
			self.charisma = rolls[2]

		elif self.clas == 'Warblade':
			self.strength = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.intelligence = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))
			self.dexterity = rolls.pop(rolls.index(max(rolls)))

			self.wisdom = rolls[0]
			self.charisma= rolls[1]

		elif self.clas == 'Warmage':
			self.intelligence = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.charisma = rolls.pop(rolls.index(max(rolls)))
			self.dexterity = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.wisdom = rolls[1]

		elif self.clas == 'Wilder':
			self.charisma = rolls.pop(rolls.index(max(rolls))) + int(self.level / 4)
			self.dexterity = rolls.pop(rolls.index(max(rolls)))
			self.constitution = rolls.pop(rolls.index(max(rolls)))

			self.strength = rolls[0]
			self.intelligence = rolls[1]
			self.wisdom = rolls[2]
		print 'Ability scores assigned!'
		self.reassignAllMods()
		# imma try putting this skill thing here. see if it works out. i figure we should establish this as soon as possible, meaning right after we get the character's modifiers
		self.skillBonus = {'Acrobatics' : self.dexMod, 'Appraise' : self.intMod, 'Autohypnosis' : self.wisMod, 'Bluff' : self.chaMod, 'Climb' : self.strMod, 'Craft' : self.intMod, 'Diplomacy' : self.chaMod, 'Disable Device' : self.dexMod, 'Disguise' : self.chaMod, 'Escape Artist' : self.dexMod, 'Fly' : self.dexMod, 'Handle Animal' : self.chaMod, 'Heal' : self.wisMod, 'Intimidate' : self.chaMod, 'Knowledge(Arcana)' : self.intMod, 'Knowledge(Dungeoneering)' : self.intMod, 'Knowledge(Engineering)' : self.intMod, 'Knowledge(Geography)' : self.intMod, 'Knowledge(History)' : self.intMod, 'Knowledge(Local)' : self.intMod, 'Knowledge(Nature)' : self.intMod, 'Knowledge(Nobility)' : self.intMod, 'Knowledge(Planar)' : self.intMod, 'Knowledge(Psionics)' : self.intMod, 'Knowledge(Religion)' : self.intMod, 'Linguistics' : self.intMod, 'Martial Lore' : self.intMod, 'Perception' : self.wisMod, 'Perform' : self.chaMod, 'Profession' : self.wisMod, 'Psicraft' : self.intMod, 'Ride' : self.dexMod, 'Sense Motive' : self.wisMod, 'Sleight of Hand' : self.dexMod, 'Spellcraft' : self.intMod, 'Stealth' : self.dexMod, 'Survival' : self.wisMod, 'Swim' : self.strMod, 'Use Magic Device' : self.chaMod, 'Use Psionic Device' : self.chaMod}
		print 'Skill bonuses initialized!'


	# assignAbilityScores is a function intended to take in the list of rolls and put them in place. This version simply places them in order. The function also assigns each Ability Score's Modifier, which is used in most calculations in place of the score itself.
	def assignAbilityScores(self,rolls):
		print 'In the assignAbilityScores() method...'
		for i in xrange(int(self.level / 4)):
			rolls[random.randint(0,5)] += 1
		print 'Ability scores increases from level have been added!'

		self.strength = rolls[0]
		self.strMod = self.calcMod(self.strength)
		print 'Strength set to {} ({})'.format(self.strength, self.strMod)
		
		self.dexterity = rolls[1]
		self.dexMod = self.calcMod(self.dexterity)
		print 'Dexterity set to {} ({})'.format(self.dexterity, self.dexMod)

		self.constitution = rolls[2]
		self.conMod = self.calcMod(self.constitution)
		print 'Constitution set to {} ({})'.format(self.constitution, self.conMod)
		
		self.intelligence = rolls[3]
		self.intMod = self.calcMod(self.intelligence)
		print 'Intelligence set to {} ({})'.format(self.intelligence, self.intMod)

		self.wisdom = rolls[4]
		self.wisMod = self.calcMod(self.wisdom)
		print 'Wisdom set to {} ({})'.format(self.wisdom, self.wisMod)
		
		self.charisma = rolls[5]
		self.chaMod = self.calcMod(self.charisma)
		print 'Charisma set to {} ({})'.format(self.charisma, self.chaMod)

		print 'Ability scores set!'

		self.skillBonus = {'Acrobatics' : self.dexMod, 'Appraise' : self.intMod, 'Autohypnosis' : self.wisMod, 'Bluff' : self.chaMod, 'Climb' : self.strMod, 'Craft' : self.intMod, 'Diplomacy' : self.chaMod, 'Disable Device' : self.dexMod, 'Disguise' : self.chaMod, 'Escape Artist' : self.dexMod, 'Fly' : self.dexMod, 'Handle Animal' : self.chaMod, 'Heal' : self.wisMod, 'Intimidate' : self.chaMod, 'Knowledge(Arcana)' : self.intMod, 'Knowledge(Dungeoneering)' : self.intMod, 'Knowledge(Engineering)' : self.intMod, 'Knowledge(Geography)' : self.intMod, 'Knowledge(History)' : self.intMod, 'Knowledge(Local)' : self.intMod, 'Knowledge(Nature)' : self.intMod, 'Knowledge(Nobility)' : self.intMod, 'Knowledge(Planar)' : self.intMod, 'Knowledge(Psionics)' : self.intMod, 'Knowledge(Religion)' : self.intMod, 'Linguistics' : self.intMod, 'Martial Lore' : self.intMod, 'Perception' : self.wisMod, 'Perform' : self.chaMod, 'Profession' : self.wisMod, 'Psionic' : self.intMod, 'Ride' : self.dexMod, 'Sense Motive' : self.wisMod, 'Sleight of Hand' : self.dexMod, 'Spellcraft' : self.intMod, 'Stealth' : self.dexMod, 'Survival' : self.wisMod, 'Swim' : self.strMod, 'Use Magic Device' : self.chaMod, 'Use Psionic Device' :  self.chaMod}
		print 'Skill bonuses initialized!'


	# function to calculate the ability score modifier given the score
	def calcMod(self,score):
		if score % 2 == 0: # if the score is even
			return (score - 10) / 2
		else: # if the score is odd
			return (score - 11) / 2

	# function to change the character's ability score modifier once
	# it has already been set. 
	def reassignMod(self,mod):
		if mod == self.strMod:
			self.strMod = self.calcMod(self.strength)
		elif mod == self.dexMod:
			self.dexMod = self.calcMod(self.dexterity)
		elif mod == self.conMod:
			self.conMod = self.calcMod(self.constitution)
		elif mod == self.intMod:
			self.intMod = self.calcMod(self.intelligence)
		elif mod == self.wisMod:
			self.wisMod = self.calcMod(self.wisdom)
		elif mod == self.chaMod:
			self.chaMod = self.calcMod(self.charisma)

	# function to reassign all ability score modifiers
	def reassignAllMods(self):
		self.strMod = self.calcMod(self.strength)
		self.dexMod = self.calcMod(self.dexterity)
		self.conMod = self.calcMod(self.constitution)
		self.intMod = self.calcMod(self.intelligence)
		self.wisMod = self.calcMod(self.wisdom)
		self.chaMod = self.calcMod(self.charisma)

	# function to calculate armor class
	def calcArmorClass(self):
		self.armorClass = 10 + self.dexMod - self.size
		self.touchArmorClass = 10 + self.dexMod - self.size
		self.flatFootedArmorClass = 10 - self.size

	# function to print all ability scores and their modifiers in this neat table
	def printAbilityScores(self):
		print "Ability | Score | Modifier"
		print "Str     |  {}   |    {}".format(self.strength, self.strMod)
		print "Dex     |  {}   |    {}".format(self.dexterity, self.dexMod)
		print "Con     |  {}   |    {}".format(self.constitution, self.conMod)
		print "Int     |  {}   |    {}".format(self.intelligence, self.intMod)
		print "Wis     |  {}   |    {}".format(self.wisdom, self.wisMod)
		print "Cha     |  {}   |    {}".format(self.charisma, self.chaMod)

	# function to set class
	def setClass(self, newClass):
		self.clas = newClass
		return self.clas

	# function to determine an approprite class for the character
	# looks at which ability scores the character has that are good and uses those to choose
	def chooseClass(self):
		goodStats = [0,0,0,0,0,0]
		if self.strMod >= 2: goodStats[0] = 1
		if self.dexMod >= 2: goodStats[1] = 1
		if self.conMod >= 2: goodStats[2] = 1
		if self.intMod >= 2: goodStats[3] = 1
		if self.wisMod >= 2: goodStats[4] = 1
		if self.chaMod >= 2: goodStats[5] = 1

		# print 'Good Stats: {}'.format(goodStats)
		# print 'Sum of goodStats : {}'.format(sum(goodStats))

		if sum(goodStats) >= 3:
			# print 'At least 3 good stats!'
			if goodStats[1] == goodStats[2] == goodStats[4] == 1: # good Dex, Con, and Wis
				self.clas = 'Monk'
				return self.clas
			elif goodStats[1] == goodStats[3] == goodStats[5] == 1: # good Dex, Int, and Cha
				self.clas = 'Bard'
				return self.clas
			elif goodStats[0] == goodStats[2] == goodStats[5] == 1: # good Str, Con, and Cha
				self.clas = 'Paladin'
				return self.clas
			elif goodStats[0] == goodStats[1] == goodStats[4] == 1: # good Str, Dex, and Wis
				self.clas = 'Ranger'
				return self.clas
			# else:
			# 	print 'Not monk, bard, or paladin material.'

		if sum(goodStats) >= 2:
			#print 'Two good stats!'
			if goodStats[0] == goodStats[3] == 1: # good Strength, and Intellect
				self.clas = 'Warblade'
				return self.clas
			elif goodStats[1] == goodStats[4] == 1: # Dex, Wis
				self.clas = 'Swordsage'
				return self.clas
			elif goodStats[2] == goodStats[5] == 1: # Con, Cha
				self.clas = 'Crusader'
				return self.clas
			elif goodStats[3] == goodStats[5] == 1: # Int, Cha
				self.clas = 'Warmage'
				return self.clas
			elif goodStats[1] == goodStats[3] == 1: # Dex, Int
				self.clas = 'Beguiler'
				return self.clas
			elif goodStats[1] == goodStats[5] == 1: # Dex, Cha
				self.clas = 'Dread Necromancer'
				return self.clas
			elif goodStats[2] == goodStats[4] == 1: # Con, Wis
				self.clas = 'Druid'
				return self.clas
			# else:
				#print 'No matches here...'
			
		if sum(goodStats) >= 1:
			#print 'Checking the single stat dependent classes...'
			if goodStats[0] == 1:
				self.clas = 'Barbarian'
				#print 'Class: {}'.format(self.clas)
				return self.clas
			elif goodStats[1] == 1:
				self.clas = 'Rogue'
				#print 'Class: {}'.format(self.clas)
				return self.clas
			elif goodStats[2] == 1:
				self.clas = 'Fighter'
				#print 'Class: {}'.format(self.clas)
				return self.clas
			elif goodStats[3] == 1:
				self.clas = 'Psion'
				#print 'Class: {}'.format(self.clas)
				return self.clas
			elif goodStats[4] == 1:
				self.clas = 'Ardent'
				#print 'Class: {}'.format(self.clas)
				return self.clas
			elif goodStats[5] == 1:
				self.clas = 'Wilder'
				#print 'Class: {}'.format(self.clas)
				return self.clas
			else:
				print 'Well this is weird.'

		# # a character generated using the stat roller here should never have stats this low, but just in case
		# if sum(goodStats) == 0:
		# 	self.clas == 'Commoner'
		# 	return self.clas

	def assignRace(self):
		raceChoices = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Kobold', 'Half-Orc']
		self.race = random.choice(raceChoices)
		self.getRacialTraits()
		return self.race

	# function to get the character their race's features including size, speed, stat adjustments, etc.
	def getRacialTraits(self):
		if self.race == 'Human':
			# SET SIZE AND SPEED
			self.size = 0
			self.landSpeed = 30

			# STAT ADJUSTMENT
			# if the character's constitution is low it will use the human +2 to any stat
			# to boost their constitution
			if self.constitution > 10:
				self.constitution += 2
			# otherwise the program increases a randomly chosen abiity score
			else:
				whichStat = random.randint(1,6)
				if whichStat == 1:
					self.strength += 2
				elif whichStat == 2:
					self.dexterity += 2
				elif whichStat == 3:
					self.constitution += 2
				elif whichStat == 4:
					self.intelligence += 2
				elif whichStat == 5:
					self.wisdom += 2
				elif whichStat == 6:
					self.charisma += 2
			self.reassignAllMods()

			# SPECIAL RACIAL ABILITIES
			self.getFeat()
		
			# LANGUAGES
			self.languagesKnown.append('Common')
			if self.intMod > 0:
				langChoices = ['Aboleth', 'Abyssal', 'Aklo', 'Aquan', 'Auran', 'Boggard', 'Celestial', 'Cyclops', 'Dark Folk', 'Draconic', 'Drow Sign Language', 'Dwarven', 'Elven', 'Giant', 'Gnoll', 'Gnome', 'Goblin', 'Grippli', 'Halfling', 'Ignan', 'Infernal', 'Necril', 'Orc', 'Sylvan', 'Tengu', 'Terran', 'Treant', 'Undercommon']
				for i in xrange(self.intMod):
					self.languagesKnown.append(langChoices.pop(random.randint(0,len(langChoices)-1)))

		elif self.race == 'Dwarf':
			# SET SIZE AND SPEED
			self.size = 0
			self.landSpeed = 20

			# STAT ADJUSTMENT
			self.constitution += 2
			self.wisdom += 2
			self.charisma -= 2
			self.reassignAllMods()

			# SPECIAL RACIAL ABILITIES
			self.specialList.append('Defensive Training')
			self.specialList.append('Hardy')
			self.specialList.append('Stability')
			self.specialList.append('Greed')
			self.specialList.append('Stonecunning')
			self.specialList.append('Darkvision 60')
			self.specialList.append('Hatred')
			self.specialList.append('Dwarven Weapon Familiarity')

			# LANGUAGES
			self.languagesKnown.extend(['Common', 'Dwarven'])
			if self.intMod > 0:
				langChoices = ['Giant', 'Gnome', 'Goblin', 'Orc', 'Terran', 'Undercommon']
				for i in xrange(self.intMod):
					self.languagesKnown.append(langChoices.pop(random.randint(0,len(langChoices)-1)))

		elif self.race == 'Elf':
			# SET SIZE AND SPEED
			self.size = 0
			self.landSpeed = 30

			# STAT ADJUSTMENT
			self.dexterity += 2
			self.intelligence += 2
			self.constitution -= 2
			self.reassignAllMods()

			# SPECIAL RACIAL ABILITIES
			self.specialList.append('Elven Immunities')
			self.skillBonus['Perception'] += 2
			self.specialList.append('Elven Magic')
			self.specialList.append('Low-Light Vision')

			# LANGUAGES
			self.languagesKnown.extend(['Common', 'Elven'])
			if self.intMod > 0:
				langChoices = ['Celestial', 'Draconic', 'Gnoll', 'Gnome', 'Goblin', 'Orc', 'Sylvan']
				for i in xrange(self.intMod):
					self.languagesKnown.append(langChoices.pop(random.randint(0,len(langChoices)-1)))


		elif self.race == 'Gnome':
			# SET SIZE AND SPEED
			self.size = -1
			self.landSpeed = 20

			# STAT ADJUSTMENT
			self.constitution += 2
			self.charisma += 2
			self.strength -= 2
			self.reassignAllMods()

			# SPECIAL RACIAL ABILITIES
			self.specialList.append('Defensive Training')
			self.specialList.append('Illusion Resistance')
			self.specialList.append('Keen Senses')
			self.skillBonus['Perception'] += 2
			self.specialList.append('Obsessed') # +2 bonus on a Craft or Profession of player's choice
			choices = ['Alchemy', 'Armor', 'Bows', 'Weapons', 'Trapmaking', 'Carpentry', 'Mechanical']
			self.skillBonus['Craft({})'.format(random.choice(choices))] = self.intMod + 2
			self.specialList.append('Gnome Magic')
			self.specialList.append('Hatred')
			self.specialList.append('Gnome Weapon Familiarity')
			self.specialList.append('Low-Light Vision')

			# LANGUAGES
			self.languagesKnown.extend(['Common', 'Gnome'])
			if self.intMod > 0:
				langChoices = ['Draconic', 'Dwarven', 'Elven', 'Giant', 'Goblin', 'Orc']
				for i in xrange(self.intMod):
					self.languagesKnown.append(langChoices.pop(random.randint(0,len(langChoices)-1)))


		elif self.race == 'Halfling':
			# SET SIZE AND SPEED
			self.size = -1
			self.landSpeed = 20

			# STAT ADJUSTMENT
			self.dexterity += 2
			self.charisma += 2
			self.strength -= 2
			self.reassignAllMods()

			# SPECIAL RACIAL ABILITIES
			self.specialList.append('Fearless')
			self.specialList.append('Halfling Luck') # Halfling Luck: +1 to all saving throws
			self.specialList.append('Sure-Footed') # Sure-Footed: +2 to Acrobatics and Climb
			self.skillBonus['Acrobatics'] += 2
			self.skillBonus['Climb'] += 2
			self.specialList.append('Halfling Weapon Familiarity')
			self.specialList.append('Keen Senses')
			self.skillBonus['Perception'] += 2

			# LANGUAGES
			self.languagesKnown.extend(['Common', 'Halfling'])
			if self.intMod > 0:
				langChoices = ['Dwarven', 'Elven', 'Gnome', 'Goblin', 'Sylvan', 'Undercommon', 'Auran']
				for i in xrange(self.intMod):
					self.languagesKnown.append(langChoices.pop(random.randint(0,len(langChoices)-1)))


		elif self.race == 'Half-Orc':
			# SET SIZE AND SPEED
			self.size = 0
			self.landSpeed = 30

			# STAT ADJUSTMENT
			if self.strength > 10:
				self.strength += 2
			# otherwise the program increases a randomly chosen ability score
			else:
				whichStat = random.randint(1,6)
				if whichStat == 1:
					self.strength += 2
				elif whichStat == 2:
					self.dexterity += 2
				elif whichStat == 3:
					self.constitution += 2
				elif whichStat == 4:
					self.intelligence += 2
				elif whichStat == 5:
					self.wisdom += 2
				elif whichStat == 6:
					self.charisma += 2
			self.reassignAllMods()

			# SPECIAL RACIAL ABILITIES
			self.skillBonus['Intimidate'] += 2
			self.specialList.append('Orc Ferocity')
			self.specialList.append('Darkvision 60')
			self.specialList.append('Orc Blood')

			# LANGUAGES
			self.languagesKnown.extend(['Common', 'Orc'])
			if self.intMod > 0:
				langChoices = ['Abyssal', 'Draconic', 'Giant', 'Gnoll', 'Goblin', 'Ignan', 'Terran', 'Undercommon']
				for i in xrange(self.intMod):
					self.languagesKnown.append(langChoices.pop(random.randint(0,len(langChoices)-1)))


		elif self.race == 'Kobold':
			# SET SIZE AND SPEED
			self.size = -1
			self.landSpeed = 30

			# STAT ADJUSTMENT
			self.strength -= 4
			self.dexterity += 2
			self.constitution -= 2
			self.reassignAllMods()

			# SPECIAL RACIAL ABILITIES
			self.specialList.append('Scaly Skin') # +1 natural armor
			self.armorClass += 1
			self.flatFootedArmorClass += 1
			self.specialList.append('Crafty') # +2 to Craft(Trapmaking), Perception, and Profession(Miner).
			self.skillBonus['Craft(Trapmaking)'] = self.intMod + 2
			self.skillBonus['Perception'] += 2
			self.skillBonus['Profession(Miner)'] = self.wisMod + 2
			self.classSkills.extend(['Craft(Trapmaking)', 'Stealth'])
			self.specialList.append('Darkvision 60 feet')
			self.specialList.append('Light Sensitivity')

			# LANGUAGES
			self.languagesKnown.extend(['Draconic'])
			if self.intMod > 0:
				langChoices = ['Common', 'Dwarven', 'Gnome', 'Undercommon', 'Ignan', 'Infernal', 'Celestial', 'Aquan', 'Auran', 'Terran']
				for i in xrange(self.intMod):
					self.languagesKnown.append(langChoices.pop(random.randint(0,len(langChoices)-1)))
						

	# calculates the character's total number of hit points based on a given hit die, and their level
	def calcHitPoints(self, hitDie):
		hp = hitDie + self.conMod # max roll for hp at level 1
		for i in xrange(self.level - 1):
			hp += random.randint(1, hitDie) + self.conMod
		return hp

	# this function looks at the character's class and then semi-randomly decides which skills to maximize
	# the number of skills the character may have at max ranks is calculated at the time as class features
	def calcSkills(self):
		for i in xrange(self.skillsAtMax):
			self.skillBonus[self.classSkills.pop(random.randint(0,len(self.classSkills)-1))] += self.level + 3

	# function to get feats at the appropriate levels
	def getFeats(self):
		numOfFeats = int(math.ceil(self.level / 2)) + 1
		for i in xrange(numOfFeats):
			self.getFeat()

	# getFeat will look through a list of feats and choose a suitable one
	# for the character. It also gives the character that feat and returns
	# the name of it. 
	def getFeat(self):
		priorityPool = set() # a pool of feats that are a higher tier of priority than others for the character
		featPool = {'Fleet', 'Toughness', 'Improved Initiative', 'Quick Draw'} # a pool of lower priority feats, begin with some old favorites that are good for everyone
		
		if self.dexMod - 2 >= self.strMod and 'Melee' in self.tags:
			priorityPool.add('Weapon Finesse')

		if 'Shield' in self.tags:
			priorityPool.update({'Improved Shield Bash', 'Shield Focus(Spiked Iron Light Shield)'})

		if 'Ranged Attacker' in self.tags:
			priorityPool.add('Point Blank Shot')

		if 'Power Attack' in self.featList:
			featPool.update(['Cleave', 'Improved Bull Rush', 'Improved Overrun'])

		if 'Combat Expertise' in self.featList:
			featPool.update(['Imrpoved Feint', 'Improved Disarm'])

		if 'Dodge' in self.featList:
			featPool.add('Mobility')

		if 'Improved Unarmed Strike' in self.featList:
			featPool.add('Scorpion Style')
			if self.dexterity >= 13:
				featPool.add('Improved Grapple')
				featPool.add('Deflect Arrows')

		if 'Point Blank Shot' in self.featList:
			priorityPool.add('Precise Shot')
			featPool.add('Far Shot')

		if 'Two-Weapon Fighting' in self.featList:
			featPool.add('Double Slice')

		if 'Weapon Focus' in self.featList:
			featPool.add('Dazzing Display')

		if self.BAB >= 4:
			if 'Cleave' in self.featList:
				featPool.add('Great Cleave')
			if 'Weapon Focus' in self.featList:
				featPool.add('Weapon Specialization')
			if 'Mobility' in self.featList:
				featPool.add('Spring Attack')
				if 'Point Blank Shot' in self.featList and self.dexterity >= 13:
					featPool.add('Shot on the Run')
		if self.BAB >= 6:
			featPool.update(['Disruptive', 'Vital Strike', 'Lunge'])
			if 'Improved Bull Rush' in self.featList:
				featPool.add('Greater Bull Rush')
			if 'Improved Overrun' in self.featList:
				featPool.add('Greater Overrun')
			if 'Improved Feint' in self.featList:
				featPool.add('Greater Feint')
			if 'Dazzing Display' in self.featList:
				featPool.add('Shatter Defenses')
			if 'Dodge' in self.featList:
				featPool.add('Wind Stance')
			if self.dexterity >= 17:
				if 'Two-Weapon Fighting' in self.featList:
					featPool.add('Improved Two-Weapon Fighting')
				if 'Rapid Shot' in self.featList:
					featPool.add('Manyshot')
			if 'Scorpion Style' in self.featList:
				featPool.add("Gorgon's Fist")
			if 'Improved Grapple' in self.featList:
				featPool.add('Greater Grapple')
		if self.BAB >= 8:
			featPool.add('Improved Critical')
			if 'Weapon Focus' in self.featList:
				featPool.add('Greater Weapon Focus')
			if 'Shield Focus' in self.featList:
				featPool.add('Greater Shield Focus')
			if 'Catch Off-Guard' or 'Throw Anything' in self.featList:
				featPool.add('Improvised Weapon Mastery')
		if self.BAB >= 9 and 'Melee' in self.tags or 'Ranged Attacker' in self.tags:
			featPool.add('Critical Focus')
		if self.BAB >= 10:
			if 'Disruptive' in self.featList:
				featPool.add('Spellbreaker')
		if self.BAB >= 11:
			featPool.add('Strike Back')
			if 'Critical Focus' in self.featList:
				featPool.add('Bleeding Critical')
				featPool.add('Sickening Critical')
			if "Gorgon's Fist" in self.featList:
				featPool.add("Medusa's Wrath")
			if 'Shield Slam' in self.featList:
				featPool.add('Shield Master')
			if 'Vital Strike' in self.featList:
				featPool.add('Improved Vital Strike')
			if 'Improved Two-Weapon Fighting' in self.featList:
				if 'Double Slice' in self.featList:
					featPool.add('Two-Weapon Rend')
				if self.dexterity >= 19:
					featPool.add('Greater Two-Weapon Fighting')
			if 'Precise Shot' in self.featList and self.dexterity >= 19:
				featPool.add('Improved Precise Shot')
			if 'Wind Stance' in self.featList and self.dexterity >= 17:
				featPool.add('Lightning Stance')
			if 'Greater Weapon Focus' in self.featList and 'Shatter Defneses' in self.featList:
				featPool.add('Deadly Stroke')
		if self.BAB >= 12:
			if 'Weapon Focus' in self.featList:
				featPool.add('Penetrating Strike')
			if 'Weapon Specialization' in self.featList:
				featPool.add('Greater Weapon Specialization')
		if self.BAB >= 13:
			if 'Critical Focus' in self.featList:
				featPool.add('Crippling Critical')
				featPool.add('Deafening Critical')
				featPool.add('Staggering Critical')
				featPool.add('Tiring Critical')
		if self.BAB >= 15:
			if 'Critical Focus' in self.featList:
				featPool.add('Blinding Critical')
				featPool.add('Exhausting Critical')
		if self.BAB >= 16:
			if 'Improved Vital Strike' in self.featList:
				featPool.add('Greater Vital Strike')
			if 'Improved Precise Shot' in self.featList:
				featPool.add('Pinpoint Targeting')
			if 'Penetrating Strike' in self.featList:
				featPool.add('Greater Penetrating Strike')

		if self.strength >= 13 and 'Melee' in self.tags:
			featPool.add('Power Attack')

		if self.dexterity >= 13 and 'Ranged Attacker' in self.tags:
			featPool.add('Deadly Aim')

		if self.dexterity >= 15:
			if 'Melee' in self.tags:
				featPool.add('Two-Weapon Fighting')
			if 'Deflect Arrows' in self.featList:
				featPool.add('Snatch Arrows')

		if self.intelligence >= 13 and 'Melee' in self.tags:
			featPool.add('Combat Expertise')

		if 'Lay on Hands' in self.specialList:
			featPool.add('Extra Lay on Hands')
		if 'Bardic Performance' in self.specialList:
			featPool.add('Extra Performance')
		if 'Rage' in self.specialList:
			featPool.add('Extra Rage')

		if 'Psionic' in self.tags:
			featPool.update(['Psicrystal Affinity', 'Overchannel', 'Power Penetration', 'Chain Power', 'Empower Power', 'Update Power', 'Maximize Power', 'Quicken Power'])
			if self.level >= 4:
				featPool.update(['Power Specialization'])
		if self.clas == 'Wilder':
			featPool.update(['Enervation Endurance'])
			if self.level >= 4:
				featPool.add('Euphoric Reduction')
		if self.clas == 'Ardent':
			featPool.update(['Tap Mantle', 'Mantle Focus'])
			if 'Tap Mantle' in self.featList:
				featPool.add('Don Mantle')


		# here i've got to choose a feat out of the priority pool first
		for i in xrange(len(priorityPool)):
			whichFeat = random.choice(tuple(priorityPool))
			if whichFeat not in self.featList:
				self.featList.append(whichFeat)
				self.getTagsFromFeats(whichFeat)
				return whichFeat
			else:
				priorityPool.remove(whichFeat)

		# if the character already has all the feats in the priority pool or if it's empty then we go to featPool
		for i in xrange(len(featPool)):
			whichFeat = random.choice(tuple(featPool))
			if whichFeat not in self.featList:
				self.featList.append(whichFeat)
				self.getTagsFromFeats(whichFeat)
				return whichFeat
			else:
				featPool.remove(whichFeat)

		return 0

	# funtion to get tags from appropriate feats for the character
	# its only parameter, whichFeat is the feat just added
	def getTagsFromFeats(self, whichFeat):
		if whichFeat == 'Two-Weapon Fighting':
			self.tags.add('Two Weapons')
		elif whichFeat == 'Power Attack':
			self.tags.add('Big Weapon')


	def getClassFeatures(self):
		# Do each Class Seperately here
		print 'Getting class features...'
		# BARBARIAN
		if self.clas == 'Barbarian':
			self.tags.update(['Medium Armor', 'Strong', 'Melee', 'Tough', 'Big Weapon'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(12)
			self.BAB = self.level
			self.fortSave = int(2 + (self.level / 2)) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(self.level /3) + self.wisMod
			self.skillsAtMax = 4 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.classSkills = ['Acrobatics', 'Climb', 'Craft', 'Handle Animal', 'Intimidate', 'Knowledge(Nature)', 'Perception', 'Ride', 'Survival', 'Swim']
			self.calcSkills()

			# CLASS ABILITIES
			self.ragePowers = []
			self.rageRounds = 4 + self.conMod + (2 * (self.level - 1))
			trapSense = self.level / 3			
			if self.level >= 19:
				damageReduction = 5
			elif self.level >= 16:
				damageReduction = 4
			elif self.level >= 13:
				damageReduction = 3
			elif self.level >= 10:
				damageReduction = 2
			elif self.level >= 7:
				damageReduction = 1

			if self.level >= 1:
				self.specialList.append('Fast Movement')
				self.landSpeed += 10
				self.specialList.append('Rage')
			if self.level >= 2:
				self.getRagePower(2) 
				self.specialList.append('Uncanny Dodge')
			if self.level >= 4:
				self.getRagePower(4)
			if self.level >= 5:
				self.specialList.append('Improved Uncanny Dodge')
			if self.level >= 6:
				self.getRagePower(6)
			if self.level >= 8:
				self.getRagePower(8)
			if self.level >= 10:
				self.getRagePower(10)
			if self.level >= 11:
				self.specialList.append('Greater Rage')
			if self.level >= 12:
				self.getRagePower(12)
			if self.level >= 14:
				self.specialList.append('Indomitable Will')
				self.getRagePower(14)
			if self.level >= 16:
				self.getRagePower(16)
			if self.level >= 17:
				self.specialList.append('Tireless Rage')
			if self.level >= 18:
				self.getRagePower(18)
			if self.level >= 20:
				self.specialList.append('Mighty Rage')
				self.getRagePower(20)
			if trapSense > 0:
				self.specialList.append('Trap Sense +{}'.format(trapSense))
			if self.level >= 7:
				self.specialList.append('Damage Reduction {}/-'.format(damageReduction))

		# FIGHTER
		elif self.clas == 'Fighter':
			self.tags.update('Heavy Armor')
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(10)
			self.BAB = self.level
			self.fortSave = int(2 + self.level / 2) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(self.level / 3) + self.wisMod
			self.skillsAtMax = 2 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.classSkills = ['Climb', 'Craft', 'Handle Animal', 'Intimidate', 'Knowledge(Dungeoneering)', 'Knowledge(Engineering)', 'Profession', 'Ride', 'Survival', 'Swim']
			self.calcSkills()

			# BRAVERY
			bravery = 0
			if self.level >= 18:
				bravery = 5
			elif self.level >= 14:
				bravery = 4
			elif self.level >= 10:
				bravery = 3
			elif self.level >= 6:
				bravery = 2
			elif self.level >= 2:
				bravery = 1
			if bravery > 0:
				self.specialList.append('Bravery +{}'.format(bravery))

			# ARMOR TRAINING
			if self.level >= 15:
				armorTraining = 4
			elif self.level >= 11:
				armorTraining = 3
			elif self.level >= 7:
				armorTraining = 2
			elif self.level >= 3:
				armorTraining = 1
			else:
				armorTraining = 0
			if armorTraining > 0:
				self.specialList.append('Armor Training -{}'.format(armorTraining))

			# WEAPON TRAINING
			weaponGroupList =['Axes','Heavy Blades','Light Blades','Bows','Close','Crossbows','Double','Firearms','Hammers','Monk','Natural','Polearms','Spears','Thrown']
			weaponTrainingBonus = int((self.level - 1) / 4)
			for i in xrange(weaponTrainingBonus):
				whichWeapon = weaponGroupList.pop(random.randint(0,len(weaponGroupList)-1))
				self.specialList.append('Weapon Training +{} ({})'.format(i+1, whichWeapon))
				if whichWeapon == 'Bows' or whichWeapon == 'Crossbows' or whichWeapon == 'Firearms' or whichWeapon == 'Thrown':
					self.tags.update('Ranged Attacker')
				else:
					self.tags.update('Melee')

			# OTHER SPECIAL ABILITIES
			if self.level >= 1:
				self.getFighterFeat(1)
			if self.level >= 2:
				self.getFighterFeat(2)
			if self.level >= 4:
				self.getFighterFeat(4)
			if self.level >= 6:
				self.getFighterFeat(6)
			if self.level >= 8:
				self.getFighterFeat(8)
			if self.level >= 10:
				self.getFighterFeat(10)
			if self.level >= 12:
				self.getFighterFeat(12)
			if self.level >= 14:
				self.getFighterFeat(14)
			if self.level >= 16:
				self.getFighterFeat(16)
			if self.level >= 18:
				self.getFighterFeat(18)
			if self.level >= 19:
				self.specialList.append('Armor Mastery')
			if self.level >= 20:
				self.getFighterFeat(20)
				self.specialList.append('Weapon Mastery')

		# MONK
		elif self.clas == 'Monk':
			self.tags.update('Unarmored', 'Melee')
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(8)
			self.BAB = int(0.75 * self.level)
			self.fortSave = int(0.5 * self.level) + 2 + self.conMod
			self.refSave = int(0.5 * self.level) + 2 + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.skillsAtMax = 4 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.classSkills = ['Acrobatics', 'Climb', 'Craft', 'Escape Artist', 'Intimidate', 'Knowledge(History)', 'Knowledge(Religion)', 'Perception', 'Perform', 'Profession', 'Ride', 'Sense Motive', 'Stealth', 'Swim']
			self.calcSkills()

			# FLURRY OF BLOWS
			if self.level >= 16:
				self.flurryOfBlows = [self.level - 2, self.level - 2, self.level - 7, self.level - 7, self.level - 12, self.level - 12, self.level - 17]
			elif self.level == 15: # 15th level Monks are the only monks with a Six-Attack Flurry so they get their own hard-coded elif clause
				self.flurryOfBlows = [13, 13, 8, 8, 3, 3]
			elif self.level >= 11:
				self.flurryOfBlows = [self.level - 2, self.level - 2,self.level - 7, self.level - 7, self.level - 12]
			elif self.level >= 8:
				self.flurryOfBlows = [self.level - 2, self.level - 2,self.level - 7, self.level - 7]
			elif self.level >= 6:
				self.flurryOfBlows = [self.level - 2, self.level -2, self.level - 7]
			else:
				self.flurryOfBlows = [self.level - 2, self.level -2]

			# UNARMED DAMAGE & AC BONUS
			if self.level >= 20:
				self.acBonus = 5
				if self.size == 0: # medium
					self.unarmedDamage = '2d10'
				elif self.size == -1: # small
					self.unarmedDamage = '2d8'
				elif self.size == 1: # large
					self.unarmedDamage = '4d8'
			elif self.level >= 16:
				self.acBonus = 4
				if self.size == 0:
					self.unarmedDamage = '2d8'
				elif self.size == -1:
					self.unarmedDamage = '2d6'
				elif self.size == 1:
					self.unarmedDamage = '3d8'
			elif self.level >= 12:
				self.acBonus = 3
				if self.size == 0:
					self.unarmedDamage = '2d6'
				elif self.size == -1:
					self.unarmedDamage = '1d10'
				elif self.size == 1:
					self.unarmedDamage = '3d6'
			elif self.level >= 8:
				self.acBonus = 2
				if self.size == 0:
					self.unarmedDamage = '1d10'
				elif self.size == -1:
					self.unarmedDamage = '1d8'
				elif self.size == 1:
					self.unarmedDamage = '2d8'
			elif self.level >= 4:
				self.acBonus = 1
				if self.size == 0:
					self.unarmedDamage = '1d8'
				elif self.size == -1:
					self.unarmedDamage = '1d6'
				elif self.size == 1:
					self.unarmedDamage = '2d6'
			else:
				self.acBonus = 0
				if self.size == 0:
					self.unarmedDamage = '1d6'
				elif self.size == -1:
					self.unarmedDamage = '1d4'
				elif self.size == 1:
					self.unarmedDamage = '1d8'
			self.armorClass += self.acBonus + self.wisMod
			self.touchArmorClass += self.acBonus + self.wisMod
			self.flatFootedArmorClass += self.acBonus + self.wisMod

			# FAST MOVEMENT
			fastMovement = int(self.level / 3) * 10

			# SLOW FALL
			if self.level >= 4 :
				slowFall = int(self.level / 2) * 10


			# OTHER SPECIAL ABILITIES
			bonusFeatList = []
			if self.level >= 1:
				self.specialList.append('Stunning Fist')
				self.specialList.append('Flurry of Blows: {}'.format(self.flurryOfBlows))
				self.specialList.append('Unarmed Strike: {}'.format(self.unarmedDamage))
				bonusFeatList.extend(['Catch Off-Guard', 'Combat Reflexes', 'Deflect Arrows', 'Dodge', 'Improved Grapple', 'Scorpion Style', 'Throw Anything'])
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
			if self.level >= 2:
				self.specialList.append('Evasion')
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
			if self.level >= 3:
				self.specialList.append('Fast Movement: +{}'.format(fastMovement))
				self.specialList.append('Maneuver Training')
				self.specialList.append('Still Mind')
			if self.level >= 4:
				self.kiPool = (self.level / 2) + self.wisMod
				self.specialList.append('Ki Pool: {}'.format(self.kiPool))
				self.specialList.append('Ki Pool(Magic)')
			if self.level >= 5:
				self.specialList.append('High Jump')
				self.specialList.append('Purity of Body')
			if self.level >= 6:
				bonusFeatList.extend(["Gorgon's Fist", 'Improved Bull Rush', 'Improved Disarm', 'Improved Feint', 'Improved Trip', 'Mobility'])
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
			if self.level >= 7:
				self.specialList.append('Ki Pool(Cold Iron/Silver')
				self.specialList.append('Wholeness of Body')
			if self.level >= 9:
				self.specialList.append('Improved Evasion')
			if self.level >= 10:
				bonusFeatList.extend(['Improved Critical', "Medusa's Wrath", 'Snatch Arrows', 'Spring Attack'])
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
				self.specialList.append('Ki Pool(Lawful)')
			if self.level >= 11:
				self.specialList.append('Diamond Body')
			if self.level >= 12:
				self.specialList.append('Abundant Step')
			if self.level >= 13:
				self.specialList.append('Diamond Soul')
			if self.level >= 14:
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
			if self.level >= 15:
				self.specialList.append('Quivering Palm')
			if self.level >= 16:
				self.specialList.append('Ki Pool(Adamantine')
			if self.level >= 17:
				self.specialList.append('Timeless Body')
				self.specialList.append('Tongue of Sun and Moon')
			if self.level >= 18:
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
			if self.level >= 19:
				self.specialList.append('Empty Body')
			if self.level >= 20:
				self.specialList.append('Perfect Self')
				self.specialList.append('Slow Fall Any Distance')

		# ROGUE
		elif self.clas == 'Rogue':
			self.tags.update(['Light Armor', 'Sneaky', 'Melee', 'Two-Weapon'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(8)
			self.BAB = int(0.75 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = 2 + int(self.level / 2) + self.dexMod
			self.willSave = int(self.level / 3) + self.wisMod
			self.classSkills = ['Acrobatics', 'Appraise', 'Bluff', 'Climb', 'Craft', 'Diplomacy', 'Disable Device', 'Disguise', 'Escape Artist', 'Intimidate', 'Knowledge(Dungeoneering)', 'Knowledge(Local)', 'Linguistics', 'Perception', 'Perform', 'Profession', 'Sense Motive', 'Sleight of Hand', 'Stealth', 'Swim', 'Use Magic Device']
			self.skillsAtMax = 8 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# SNEAK ATTACK
			sneakAttack = ((self.level + 1) / 2)

			# TRAP SENSE
			trapSense = int(self.level / 3)

			# OTHER SPECIAL ABILITIES
			self.rogueTalents = []
			if self.level >= 1:
				self.specialList.append('Sneak Attack +{}d6'.format(sneakAttack))
				self.specialList.append('Trapfinding')
			if self.level >= 2:
				self.specialList.append('Evasion')
				self.getRogueTalent(2)
			if self.level >= 3:
				self.specialList.append('Trap Sense +{}'.format(trapSense))
			if self.level >= 4:
				self.specialList.append('Uncanny Dodge')
				self.getRogueTalent(4)
			if self.level >= 6:
				self.getRogueTalent(6)
			if self.level >= 8:
				self.specialList.append('Improved Uncanny Dodge')
				self.getRogueTalent(8)
			if self.level >= 10:
				self.specialList.append('Advanced Talents')
				self.getRogueTalent(10)
			if self.level >= 12:
				self.getRogueTalent(12)
			if self.level >= 14:
				self.getRogueTalent(14)
			if self.level >= 16:
				self.getRogueTalent(16)
			if self.level >= 18:
				self.getRogueTalent(18)
			if self.level >= 20:
				self.specialList.append('Master Strike')
				self.getRogueTalent(20)

		# PALADIN
		elif self.clas == 'Paladin':
			self.tags.update(['Heavy Armor', 'Spellcaster', 'Divine', 'Melee', 'Prepared'])
			self.tags.update(random.choice(['Two-Handed', 'Shield']))
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(10)
			self.BAB = self.level
			self.fortSave = 2 + int(self.level / 2) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = 2 + int(self.level / 2) + self.wisMod
			self.classSkills = ['Craft', 'Diplomacy', 'Handle Animal', 'Heal', 'Knowledge(Nobility)', 'Knowledge(Religion)', 'Ride', 'Sense Motive', 'Spellcraft']
			self.skillsAtMax = 2 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# SMITES
			smitesPerDay = (self.level + 2) / 3

			# OTHER SPECIAL ABILITIES
			mercies = []
			self.spellsPerDay = []
			if self.level >= 1:
				self.specialList.append('Smite Evil {}/day'.format(smitesPerDay))
				self.specialList.append('Aura of Good')
				self.specialList.append('Detect Evil')
			if self.level >= 2:
				self.specialList.append('Divine Grace')
				self.fortSave += self.chaMod
				self.refSave += self.chaMod
				self.willSave += self.chaMod
				self.specialList.append('Lay on Hands')
			if self.level >= 3:
				self.specialList.append('Aura of Courage')
				self.specialList.append('Divine Health')
				mercies.append('Fatigued')
				mercies.append('Shaken')
				mercies.append('Sickened')
				whichMercy = mercies[random.randint(0,len(mercies)-1)]
				mercies.remove(whichMercy)
				self.specialList.append('Mercy({})'.format(whichMercy))
			if self.level >= 4:
				self.specialList.append('Channel Positive Energy')
				self.spellsPerDay.append(0)
			if self.level >= 5:
				self.specialList.append('Divine Bond')
				self.spellsPerDay[0] += 1
			if self.level >= 6:
				mercies.append('Dazed')
				mercies.append('Diseased')
				mercies.append('Staggered')
				whichMercy = mercies[random.randint(0,len(mercies)-1)]
				mercies.remove(whichMercy)
				self.specialList.append('Mercy({})'.format(whichMercy))
			if self.level >= 7:
				self.spellsPerDay.append(0)
			if self.level >= 8:
				self.specialList.append('Aura of Resolve')
				self.spellsPerDay[1] += 1
			if self.level >= 9:
				mercies.append('Cursed')
				mercies.append('Exhausted')
				mercies.append('Frightened')
				mercies.append('Nauseated')
				mercies.append('Poisoned')
				whichMercy = mercies[random.randint(0,len(mercies)-1)]
				mercies.remove(whichMercy)
				self.specialList.append('Mercy({})'.format(whichMercy))
				self.spellsPerDay[0] += 1
			if self.level >= 10:
				self.spellsPerDay.append(0)
			if self.level >= 11:
				self.specialList.append('Aura of Justice')
				self.spellsPerDay[2] += 1
			if self.level >= 12:
				mercies.append('Blinded')
				mercies.append('Deafened')
				mercies.append('Paralyzed')
				mercies.append('Stunned')
				whichMercy = mercies[random.randint(0,len(mercies)-1)]
				mercies.remove(whichMercy)
				self.specialList.append('Mercy({})'.format(whichMercy))
				self.spellsPerDay[1] += 1
			if self.level >= 13:
				self.spellsPerDay[0] += 1
				self.spellsPerDay.append(0)
			if self.level >= 14:
				self.specialList.append('Aura of Faith')
				self.spellsPerDay[3] += 1
			if self.level >= 15:
				whichMercy = mercies[random.randint(0,len(mercies)-1)]
				mercies.remove(whichMercy)
				self.specialList.append('Mercy({})'.format(whichMercy))
				self.spellsPerDay[2] += 1
			if self.level >= 16:
				self.spellsPerDay[1] += 1
			if self.level >= 17:
				self.specialList.append('Aura of Righteousness')
				self.spellsPerDay[0] += 1
			if self.level >= 18:
				whichMercy = mercies[random.randint(0,len(mercies)-1)]
				mercies.remove(whichMercy)
				self.specialList.append('Mercy({})'.format(whichMercy))
				self.spellsPerDay[3] += 1
			if self.level >= 19:
				self.spellsPerDay[2] += 1
			if self.level >= 20:
				self.specialList.append('Holy Champion')
				self.spellsPerDay[1] += 1
				self.spellsPerDay[3] += 1

			self.calcBonusSpells(self.chaMod)
			self.prepareSpells()

		# CRUSADER
		elif self.clas == 'Crusader':
			self.tags.update(['Heavy Armor', 'Martial Adept', 'Tough', 'Melee', 'Shield'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(10)
			self.BAB = self.level
			self.fortSave = int(2 + self.level / 2) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(self.level / 3) + self.wisMod
			self.classSkills = ['Acrobatics', 'Craft', 'Diplomacy', 'Intimidate', 'Knowledge(History)', 'Knowledge(Religion)', 'Martial Lore', 'Ride']
			self.skillsAtMax = 4 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# STEELY RESOLVE
			steelyResolve = 5
			steelyResolve += (5 * (self.level / 4))

			# SMITES
			if self.level >= 18:
				smitesPerDay = 2
			elif self.level >= 6:
				smitesPerDay = 1

			# THE SUBLIME WAY & OTHER SPECIAL ABILITIES
			self.maneuversKnown = 5
			self.maneuversReadied = [5,2]
			self.stancesKnown = 1
			self.availableDiscplines = ['Devoted Spirit', 'Stone Dragon', 'White Raven']
			self.maneuverList = []
			self.stanceList = []
			self.desertWindCount = 0
			self.devotedSpiritCount = 0
			self.diamondMindCount = 0
			self.ironHeartCount = 0
			self.settingSunCount = 0
			self.shadowHandCount = 0
			self.stoneDragonCount = 0
			self.tigerClawCount = 0
			self.whiteRavenCount = 0
			if self.level >= 1:
				self.specialList.append('Furious Counterstrike')
				self.specialList.append('Steely Resolve {}'.format(steelyResolve))
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnStance(1)
			if self.level >= 2:
				self.specialList.append('Indomitable Soul')
				self.learnStance(2)
			if self.level >= 3:
				self.specialList.append('Zealous Surge')
				self.learnManeuver(3)
			if self.level >= 5:
				self.learnManeuver(5)
			if self.level >= 6:
				self.specialList.append('Smite {}/day'.format(smitesPerDay))
			if self.level >= 7:
				self.learnManeuver(7)
			if self.level >= 8:
				self.learnStance(8)
			if self.level >= 9:
				self.learnManeuver(9)
			if self.level >= 10:
				self.featList.append('Die Hard')
				self.maneuversReadied = [6,3]
			if self.level >= 11:
				self.learnManeuver(11)
			if self.level >= 13:
				self.specialList.append('Mettle')
				self.learnManeuver(13)
			if self.level >= 14:
				self.learnStance(14)
			if self.level >= 15:
				self.learnManeuver(15)
			if self.level >= 17:
				self.learnManeuver(17)
			if self.level >= 19:
				self.learnManeuver(19)
			if self.level >= 20:
				self.maneuversReadied = [7,4]

		# SWORDSAGE
		elif self.clas == 'Swordsage':
			self.tags.update(['Light Armor', 'Martial Adept', 'Sneaky', 'Melee', 'Two-Weapon'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(8)
			self.BAB = int(0.75 * self.level)
			self.fortSave = int(0.5 * self.level) + 2 + self.conMod
			self.refSave = int(0.5 * self.level) + 2 + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.classSkills = ['Acrobatics', 'Autohypnosis', 'Climb', 'Craft', 'Heal', 'Intimidate', 'Knowledge(History)', 'Knowledge(Local)', 'Knowledge(Nature)', 'Knowledge(Nobility)', 'Martial Lore', 'Perception', 'Ride', 'Sense Motive', 'Stealth', 'Swim']
			self.skillsAtMax = 6 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# QUICK TO ACT
			quickToAct = 1 + (self.level / 5)

			# THE SUBLIME WAY & OTHER SPECIAL ABILITIES
			self.maneuversKnown = 6
			self.maneuversReadied = 4
			self.stancesKnown = 1
			self.availableDiscplines = ['Desert Wind', 'Diamond Mind', 'Setting Sun', 'Shadow Hand', 'Stone Dragon', 'Tiger Claw']
			self.maneuverList = []
			self.stanceList = []
			self.desertWindCount = 0
			self.devotedSpiritCount = 0
			self.diamondMindCount = 0
			self.ironHeartCount = 0
			self.settingSunCount = 0
			self.shadowHandCount = 0
			self.stoneDragonCount = 0
			self.tigerClawCount = 0
			self.whiteRavenCount = 0
			focusDisc = self.availableDiscplines[random.randint(0,len(self.availableDiscplines)-1)]
			focusDisc2 = focusDisc # this gets changed before it's used; it will never be the same as the first
			
			if self.level >= 1:
				self.specialList.append('Quick to Act +{}'.format(quickToAct))
				self.specialList.append('Weapon Focus({})'.format(focusDisc))
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnStance(1)
			
			if self.level >= 2:
				self.specialList.append('AC Bonus')
				self.armorClass += self.wisMod
				self.touchArmorClass += self.wisMod
				self.flatFootedArmorClass += self.wisMod
				self.learnManeuver(2)
				self.learnStance(2)
			
			if self.level >= 3:
				self.learnManeuver(3)
				self.maneuversReadied += 1
			
			if self.level >= 4:
				self.specialList.append('Insightful Strike({})'.format(focusDisc))
				self.learnManeuver(4)
			
			if self.level >= 5:
				self.learnManeuver(5)
				self.maneuversReadied += 1
				self.learnStance(5)
			
			if self.level >= 6:
				self.learnManeuver(6)
			
			if self.level >= 7:
				self.learnManeuver(7)
				self.specialList.append('Sense Magic')
			
			if self.level >= 8:
				self.learnManeuver(8)
				self.maneuversReadied += 1
				self.specialList.append('Defensive Stance({})'.format(focusDisc))
			
			if self.level >= 9:
				self.learnManeuver(9)
				self.learnStance(9)
				self.specialList.append('Evasion')
			
			if self.level >= 10:
				self.learnManeuver(10)
				self.maneuversReadied += 1
			
			if self.level >= 11:
				self.learnManeuver(11)
			
			if self.level >= 12:
				self.learnManeuver(12)
				
				# determine the character's second discipline to focus0
				while  focusDisc2 == focusDisc:
					focusDisc2 = self.availableDiscplines[random.randint(0,len(self.availableDiscplines)-1)]
					self.specialList.append('Insightful Strike({})'.format(focusDisc2))

			if self.level >= 13:
				self.learnManeuver(13)
				self.maneuversReadied += 1
			
			if self.level >= 14:
				self.learnManeuver(14)
				self.learnStance(14)
			
			if self.level >= 15:
				self.learnManeuver(15)
				self.maneuversReadied += 1
			
			if self.level >= 16:
				self.learnManeuver(16)
				self.specialList.append('Defensive Stance({})'.format(focusDisc2))
			
			if self.level >= 17:
				self.learnManeuver(17)
				self.specialList.append('Improved Evasion')
			
			if self.level >= 18:
				self.learnManeuver(18)
				self.maneuversReadied += 1
			
			if self.level >= 19:
				self.learnManeuver(19)
			
			if self.level >= 20:
				self.learnManeuver(20)
				self.maneuversReadied += 1
				self.learnStance(20)

		# WARBLADE
		elif self.clas == 'Warblade':
			self.tags.update(['Medium Armor', 'Martial Adept', 'Strong', 'Melee'])
			self.tags.update(random.choice(['Big Weapon', 'Two-Weapon']))
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(12)
			self.BAB = self.level
			self.fortSave = int(2 + (self.level / 2)) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(self.level /3) + self.wisMod
			self.classSkills = ['Acrobatics', 'Autohypnosis', 'Climb', 'Craft', 'Diplomacy', 'Intimidate', 'Knowledge(History)', 'Knowledge(Local)', 'Martial Lore', 'Swim']
			self.skillsAtMax = 4 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# THE SUBLIME WAY & OTHER SPECIAL ABILITIES
			self.maneuversKnown = 3
			self.maneuversReadied = 3
			self.stancesKnown = 1
			self.availableDiscplines = ['Diamond Mind', 'Iron Heart', 'Stone Dragon', 'Tiger Claw', 'White Raven']
			self.maneuverList = []
			self.stanceList = []
			self.desertWindCount = 0
			self.devotedSpiritCount = 0
			self.diamondMindCount = 0
			self.ironHeartCount = 0
			self.settingSunCount = 0
			self.shadowHandCount = 0
			self.stoneDragonCount = 0
			self.tigerClawCount = 0
			self.whiteRavenCount = 0

			bonusFeatList = ['Acrobatic', 'Agile', 'Athletic', 'Blade Meditation', 'Blind-Fight', 'Combat Reflexes', 'Diehard', 'Endurance', 'Great Fortitude', 'Improved Initiative', 'Iron Will', 'Ironheart', 'Lightning Reflexes', 'Quick Draw', 'Run', 'Stone Power', 'Tiger Blooded', 'Unnerving Calm', 'White Raven Defense']

			if self.level >= 1:
				self.specialList.append('Battle Clarity(Reflex Saves)')
				self.refSave += self.intMod
				self.specialList.append('Weapon Aptitude')
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnManeuver(1)
				self.learnStance(1)
			if self.level >= 2:
				self.specialList.append('Uncanny Dodge')
				self.learnManeuver(2)
			if self.level >= 3:
				self.specialList.append('Battle Ardor(Critical Confirmation)')
				self.learnManeuver(3)
			if self.level >= 4:
				self.maneuversReadied += 1
				self.learnStance(4)
			if self.level >= 5:
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
				self.learnManeuver(5)
			if self.level >= 6:
				self.specialList.append('Improved Uncanny Dodge')
			if self.level >= 7:
				self.specialList.append('Battle Cunning(Damage)')
				self.learnManeuver(7)
			if self.level >= 9:
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
				self.learnManeuver(9)
			if self.level >= 10:
				self.maneuversReadied += 1
				self.learnStance(10)
			if self.level >= 11:
				self.specialList.append('Battle Skill(Opposed Checks)')
				self.learnManeuver(11)
			if self.level >= 13:
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
				self.learnManeuver(13)
			if self.level >= 15:
				self.specialList.append('Battle Mastery(Attacks of Opportunity)')
				self.learnManeuver(15)
				self.maneuversReadied += 1
			if self.level >= 16:
				self.learnStance(16)
			if self.level >= 17:
				self.featList.append(bonusFeatList.pop(random.randint(0,len(bonusFeatList)-1)))
				self.learnManeuver(17)
			if self.level >= 19:
				self.learnManeuver(19)
			if self.level >= 20:
				self.specialList.append('Stance Mastery')
				self.maneuversReadied += 1

		# BARD
		elif self.clas == 'Bard':
			self.tags.update(['Light Armor', 'Spellcaster', 'Arcane', 'Sneaky', 'Spontaneous'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(8)
			self.BAB = int(0.75 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = int(0.5 * self.level) + 2 + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.classSkills = ['Acrobatics', 'Appraise', 'Bluff', 'Climb', 'Craft', 'Diplomacy', 'Disguise', 'Escape Artist', 'Intimidate', 'Knowledge(Arcana)', 'Knowledge(Dungeoneering)', 'Knowledge(Engineering)', 'Knowledge(Geography)', 'Knowledge(History)', 'Knowledge(Local)', 'Knowledge(Nature)', 'Knowledge(Nobility)', 'Knowledge(Planar)', 'Knowledge(Religion)', 'Linguistics', 'Perception', 'Perform', 'Profession', 'Sense Motive', 'Sleight of Hand', 'Spellcraft', 'Stealth', 'Use Magic Device']
			self.skillsAtMax = 6 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# INSPIRE COMPETENCE
			inspireCompetence = 2 + ((self.level - 3) / 4)

			# INSPIRE COURAGE & LORE MASTER
			if self.level >= 17:
				inspireCourage = 4
				loreMaster = 3
			elif self.level >= 11:
				inspireCourage = 3
				loreMaster = 2
			elif self.level >= 5:
				inspireCourage = 2
				loreMaster = 1
			elif self.level >= 1:
				inspireCourage = 1

			self.spellsPerDay = [] # list containing the bard's number of spells per day aranged by level from 1st to 6th. 
			self.spellsKnown = [] # list containg the number of spells known by level from 0 to 6th

			# OTHER SPECIAL ABILITIES
			self.performanceRounds = 4 + self.chaMod + (2 * (self.level - 1))

			if self.level >= 1:
				self.specialList.append('Bardic Knowledge')
				self.specialList.append('Bardic Performance')
				self.specialList.append('Cantrips')
				self.specialList.append('Countersong')
				self.specialList.append('Distraction')
				self.specialList.append('Fascinate')
				self.specialList.append('Inspire Courage +{}'.format(inspireCourage))
				self.spellsPerDay.append(1)
				self.spellsKnown.append(4)
				self.spellsKnown.append(2)
			if self.level >= 2:
				self.specialList.append('Versatile Performance')
				self.specialList.append('Well-Versed')
				self.spellsPerDay[0] = 2
				self.spellsKnown[0] = 5
				self.spellsKnown[1] = 3
			if self.level >= 3:
				self.specialList.append('Inspire Competence +{}'.format(inspireCompetence))
				self.spellsPerDay[0] = 3
				self.spellsKnown[0] = 6
				self.spellsKnown[1] = 4
			if self.level >= 4:
				self.spellsPerDay.append(1)
				self.spellsKnown.append(2)
			if self.level >= 5:
				self.specialList.append('Lore Master {}/day'.format(loreMaster))
				self.spellsPerDay[0] = 4
				self.spellsPerDay[1] = 2
				self.spellsKnown[2] = 3
			if self.level >= 6:
				self.specialList.append('Suggestion')
				self.specialList.append('Versatile Performance')
				self.spellsPerDay[1] = 3
				self.spellsKnown[2] = 4
			if self.level >= 7:
				self.spellsPerDay.append(1)
				self.spellsKnown[1] = 5
				self.spellsKnown.append(2)
			if self.level >= 8:
				self.specialList.append('Dirge of Doom')
				self.spellsPerDay[1] = 4 
				self.spellsPerDay[2] = 2
				self.spellsKnown[3] = 3
			if self.level >= 9:
				self.specialList.append('Inspire Greatness')
				self.spellsPerDay[0] = 5
				self.spellsPerDay[2] = 3
				self.spellsKnown[3] = 4
			if self.level >= 10:
				self.specialList.append('Jack-of-All-Trades')
				self.specialList.append('Versatile Performance')
				self.spellsPerDay.append(1)
				self.spellsKnown.append(2)
			if self.level >= 11:
				self.spellsPerDay[2] = 4
				self.spellsPerDay[3] = 2
				self.spellsKnown[1] = 6
				self.spellsKnown[4] = 3
			if self.level >= 12:
				self.specialList.append('Soothing Performance')
				self.spellsPerDay[1] = 5
				self.spellsPerDay[3] = 3
				self.spellsKnown[4] = 4
			if self.level >= 13:
				self.spellsPerDay.append(1)
				self.spellsKnown.append(2)
			if self.level >= 14:
				self.specialList.append('Frightening Tune')
				self.specialList.append('Versatile Performance')
				self.spellsPerDay[3] = 4
				self.spellsPerDay[4] = 2
				self.spellsKnown[2] = 6
				self.spellsKnown[5] = 3
			if self.level >= 15:
				self.specialList.append('Inspire Heroics')
				self.spellsPerDay[2] = 5
				self.spellsPerDay[4] = 3
				self.spellsKnown[5] = 4
			if self.level >= 16:
				self.spellsPerDay.append(1)
				self.spellsKnown[4] = 5
				self.spellsKnown.append(2)
			if self.level >= 17:
				self.spellsPerDay[4] = 4
				self.spellsPerDay[5] = 2
				self.spellsKnown[3] = 6
				self.spellsKnown[6] = 3
			if self.level >= 18:
				self.specialList.append('Mass Suggestion')
				self.specialList.append('Versatile Performance')
				self.spellsPerDay[3] = 5
				self.spellsPerDay[5] = 3
				self.spellsKnown[6] = 4
			if self.level >= 19:
				self.spellsPerDay[4] = 5
				self.spellsPerDay[5] = 4
				self.spellsKnown[5] = 5
			if self.level >= 20:
				self.specialList.append('Deadly Performance')
				self.spellsPerDay[5] = 5
				self.spellsKnown[4] = 6
				self.spellsKnown[6] = 5

			self.learnSpells()
			self.calcBonusSpells(self.chaMod)

		# WARMAGE
		elif self.clas == 'Warmage':
			self.tags.update(['Spellcaster', 'Spontaneous', 'Arcane', 'Ranged Attacker'])
			if self.level >= 8:
				self.tags.update('Medium Armor')
			else:
				self.tags.update('Light Armor')
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(6)
			self.BAB = int(0.5 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.classSkills = ['Acrobatics', 'Craft', 'Intimidate', 'Knowledge(Arcana)', 'Knowledge(History)', 'Perception', 'Profession', 'Spellcraft']
			self.skillsAtMax = 2 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# SPELLCASTING & OTHER SPECIAL ABILITIES
			self.spellsPerDay = []
			self.spellList = []
			if self.level >= 1:
				self.specialList.append('Armored Mage(Light)')
				self.specialList.append('Warmage Edge')
				self.specialList.append('Cantrips')
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[0])
				self.spellList.append(warmageSpells[1])
			if self.level >= 2:
				self.spellsPerDay[0] = 4
			if self.level >= 3:
				self.advancedLearning(1)
				self.spellsPerDay[0] = 5
			if self.level >= 4:
				self.spellsPerDay[0] = 6
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[2])
			if self.level >= 5:
				self.spellsPerDay[1] = 4
			if self.level >= 6:
				self.spellsPerDay[1] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[3])
				self.advancedLearning(3)
			if self.level >= 7:
				self.featList.append('Sudden Empower')
				self.spellsPerDay[1] = 6
				self.spellsPerDay[2] = 4
			if self.level >= 8:
				self.specialList.append('Armored Mage(Medium)')
				self.spellsPerDay[2] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[4])
			if self.level >= 9:
				self.spellsPerDay[2] = 6
				self.spellsPerDay[3] = 4
			if self.level >= 10:
				self.featList.append('Sudden Enlarge')
				self.spellsPerDay[3] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[5])
			if self.level >= 11:
				self.advancedLearning(5)
				self.spellsPerDay[3] = 6
				self.spellsPerDay[4] = 4
			if self.level >= 12:
				self.spellsPerDay[4] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[6])
			if self.level >= 13:
				self.spellsPerDay[4] = 6
				self.spellsPerDay[5] = 4
			if self.level >= 14:
				self.spellsPerDay[5] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[7])
			if self.level >= 15:
				self.featList.append('Sudden Widen')
				self.spellsPerDay[5] = 6
				self.spellsPerDay[6] = 4
			if self.level >= 16:
				
				self.spellsPerDay[6] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[8])
				self.advancedLearning(8)
			if self.level >= 17:
				self.spellsPerDay[6] = 6
				self.spellsPerDay[7] = 4
			if self.level >= 18:
				self.spellsPerDay[7] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(warmageSpells[9])
			if self.level >= 19:
				self.spellsPerDay[7] = 6
				self.spellsPerDay[8] = 4
			if self.level >= 20:
				self.featList.append('Sudden Maximize')
				self.spellsPerDay[8] = 5
				
			self.calcBonusSpells(self.chaMod)

		# BEGUILER
		elif self.clas == 'Beguiler':
			self.tags.update(['Light Armor', 'Spellcaster', 'Arcane', 'Sneaky', 'Spontaneous'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(6)
			self.BAB = int(0.5 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.classSkills = ['Acrobatics', 'Appraise', 'Bluff', 'Climb', 'Diplomacy', 'Disable Device', 'Disguise', 'Escape Artist', 'Knowledge(Arcana)', 'Knowledge(Local)', 'Perception', 'Profession', 'Sleight of Hand', 'Stealth', 'Spellcraft', 'Swim', 'Use Magic Device']
			self.skillsAtMax = 6 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# SPELLCASTING & OTHER SPECIAL ABILITIES
			if self.level >= 14:
				cloakedCastingDC = 2
			elif self.level >= 2:
				cloakedCastingDC = 1

			self.spellsPerDay = []
			self.spellList = []
			if self.level >= 1:
				self.specialList.append('Armored Mage(Light)')
				self.specialList.append('Trapfinding')
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[0])
				self.spellList.append(beguilerSpells[1])
			if self.level >= 2:
				self.specialList.append('Cloaked Casting(+{} DC)'.format(cloakedCastingDC))
				self.specialList.append('Surprise Casting')
				self.spellsPerDay[0] = 4
			if self.level >= 3:
				self.advancedLearning(1)
				self.spellsPerDay[0] = 5
			if self.level >= 4:
				self.spellsPerDay[0] = 6
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[2])
			if self.level >= 5:
				self.featList.append('Silent Spell')
				self.spellsPerDay[1] = 4
			if self.level >= 6:
				self.specialList.append('Surprise Casting(Move Action)')
				self.spellsPerDay[1] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[3])
			if self.level >= 7:
				self.advancedLearning(3)
				self.spellsPerDay[1] = 6
				self.spellsPerDay[2] = 4
			if self.level >= 8:
				self.specialList.append('Cloaked Casting(+2 to Overcome SR')
				self.spellsPerDay[2] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[4])
			if self.level >= 9:
				self.spellsPerDay[2] = 6
				self.spellsPerDay[3] = 4
			if self.level >= 10:
				self.featList.append('Still Spell')
				self.spellsPerDay[3] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[5])
			if self.level >= 11:
				self.advancedLearning(5)
				self.spellsPerDay[3] = 6
				self.spellsPerDay[4] = 4
			if self.level >= 12:
				self.spellsPerDay[4] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[6])
			if self.level >= 13:
				self.spellsPerDay[4] = 6
				self.spellsPerDay[5] = 4
			if self.level >= 14:
				self.spellsPerDay[5] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[7])
			if self.level >= 15:
				self.advancedLearning(7)
				self.spellsPerDay[5] = 6
				self.spellsPerDay[6] = 4
			if self.level >= 16:
				self.spellsPerDay[6] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[8])
			if self.level >= 17:
				self.spellsPerDay[6] = 6
				self.spellsPerDay[7] = 4
			if self.level >= 18:
				self.spellsPerDay[7] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(beguilerSpells[9])
			if self.level >= 19:
				self.advancedLearning(9)
				self.spellsPerDay[7] = 6
				self.spellsPerDay[8] = 4
			if self.level >= 20:
				self.specialList.append('Cloaked Casting(Overcomes SR)')
				self.spellsPerDay[8] = 5
		
			self.calcBonusSpells(self.intMod)

		# DREAD NECROMANCER
		elif self.clas == 'Dread Necromancer':
			self.tags.update(['Light Armor', 'Spellcaster', 'Arcane', 'Spontaneous'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(6)
			self.BAB = int(0.5 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.classSkills = ['Bluff', 'Craft', 'Disguise', 'Intimidate', 'Knowledge(Arcana)', 'Knowledge(Religion)', 'Profession', 'Spellcraft', 'Stealth']
			self.skillsAtMax = 2 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# SPELLCASTING & OTHER SPECIAL ABILITIES
			# LICH BODY
			if self.level >= 15:
				lichBody = 8
			elif self.level >= 11:
				lichBody = 6
			elif self.level >= 7:
				lichBody = 4
			elif self.level >= 2:
				lichBody = 2
			# NEGATIVE ENERGY BURST
			negativeEnergyBurst = ((self.level - 3) / 5) + 1
			# MENTAL BASTION
			if self.level >= 14:
				mentalBastion = 4
			if self.level >= 4:
				mentalBastion = 2
			# SCABROUS TOUCH
			scabrousTouch = (self.level - 1) / 5
			# LIGHT FORTIFICATION
			if self.level >= 17:
				lightFortification = 50
			elif self.level >= 10:
				lightFortification = 25
			# ENERVATING TOUCH
			if self.level >= 12:
				enervatingTouch = int(self.level / 2)
			elif self.level >= 17:
				enervatingTouch = self.level

			self.spellsPerDay = []
			self.spellList = []
			if self.level >= 1:
				self.specialList.append('Charnel Touch')
				self.specialList.append('Rebuke Undead')
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[0])
			if self.level >= 2:
				self.specialList.append('Lich Body DR {}'.format(lichBody))
				self.spellsPerDay[0] = 4
			if self.level >= 3:
				self.specialList.append('Negative Energy Burst {}/day'.format(negativeEnergyBurst))
				self.spellsPerDay[0] = 5
			if self.level >= 4:
				self.specialList.append('Mental Bastion +{}'.format(mentalBastion))
				self.spellsPerDay[0] = 6
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[1])
				self.advancedLearning(2)
			if self.level >= 5:
				self.specialList.append('Fear Aura')
				self.spellsPerDay[1] = 4
			if self.level >= 6:
				self.specialList.append('Scabrous Touch {}/day'.format(scabrousTouch))
				self.spellsPerDay[1] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[2])
			if self.level >= 7:
				self.specialList.append('Summon Familiar')
				self.spellsPerDay[1] = 6
				self.spellsPerDay[2] = 4
			if self.level >= 8:		
				self.specialList.append('Undead Mastery')
				self.spellsPerDay[2] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[3])
				self.advancedLearning(4)
			if self.level >= 9:
				self.specialList.append('Negative Energy Resistance')
				self.spellsPerDay[2] = 6
				self.spellsPerDay[3] = 4
			if self.level >= 10:
				self.specialList.append('Light Fortification {}%'.format(lightFortification))
				self.spellsPerDay[3] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[4])
			if self.level >= 11:
				self.spellsPerDay[3] = 6
				self.spellsPerDay[4] = 4
			if self.level >= 12:
				self.specialList.append('Enervating Touch {} Negative Levels / Day'.format(enervatingTouch))
				self.spellsPerDay[4] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[5])
				self.advancedLearning(6)
			if self.level >= 13:
				self.spellsPerDay[4] = 6
				self.spellsPerDay[5] = 4
			if self.level >= 14:
				self.spellsPerDay[5] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[6])
			if self.level >= 15:
				self.spellsPerDay[5] = 6
				self.spellsPerDay[6] = 4
			if self.level >= 16:
				self.spellsPerDay[6] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[7])
				self.advancedLearning(8)
			if self.level >= 17:
				self.spellsPerDay[6] = 6
				self.spellsPerDay[7] = 4
			if self.level >= 18:
				self.spellsPerDay[7] = 5
				self.spellsPerDay.append(3)
				self.spellList.append(dreadNecroSpells[8])
			if self.level >= 19:
				self.featList.append('Craft Wondrous Item')
				self.spellsPerDay[7] = 6
				self.spellsPerDay[8] = 4
			if self.level >= 20:
				self.advancedLearning(9)
				self.specialList.append('Lich Transformation')
				self.spellsPerDay[8] = 5

			self.calcBonusSpells(self.chaMod)


		# ARDENT
		elif self.clas == 'Ardent':
			self.tags.update(['Heavy Armor', 'Psionic'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(6)
			self.powerPoints = 0 # this is calculated later
			self.BAB = int(0.5 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.classSkills = ['Autohypnosis', 'Craft', 'Diplomacy', 'Heal', 'Knowledge(Arcana)', 'Knowledge(Engineering)', 'Knowledge(Dungeoneering)', 'Knowledge(Geography)', 'Knowledge(History)', 'Knowledge(Local)', 'Knowledge(Nature)', 'Knowledge(Nobility)', 'Knowledge(Psionics)', 'Knowledge(Planar)', 'Knowledge(Religion)', 'Profession', 'Psicraft']
			self.skillsAtMax = 2 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# PSIONICS & OTHER SPECIAL ABILITIES
			self.powerList = []
			self.mantleList = []
			if self.level >= 1:
				self.powerPoints = 2
				self.assumePsionicMantle()
				self.assumePsionicMantle()
				self.learnPower(1)
				self.learnPower(1)

			if self.level >= 2:
				self.powerPoints = 6
				self.assumePsionicMantle()
				self.learnPower(1)

			if self.level >= 3:
				self.powerPoints = 11
				self.learnPower(2)

			if self.level >= 4:
				self.powerPoints = 17
				self.learnPower(2)

			if self.level >= 5:
				self.powerPoints = 25
				self.assumePsionicMantle()
				self.learnPower(3)

			if self.level >= 6:
				self.powerPoints = 35
				self.learnPower(3)

			if self.level >= 7:
				self.powerPoints = 46
				self.learnPower(4)

			if self.level >= 8:
				self.powerPoints = 58
				self.learnPower(4)

			if self.level >= 9:
				self.powerPoints = 72
				self.learnPower(5)

			if self.level >= 10:
				self.powerPoints = 88
				self.assumePsionicMantle()
				self.learnPower(5)

			if self.level >= 11:
				self.powerPoints = 106
				self.learnPower(6)

			if self.level >= 12:
				self.powerPoints = 126
				self.learnPower(6)

			if self.level >= 13:
				self.powerPoints = 147
				self.learnPower(7)

			if self.level >= 14:
				self.powerPoints = 170
				self.learnPower(7)

			if self.level >= 15:
				self.powerPoints = 195
				self.assumePsionicMantle()
				self.learnPower(8)

			if self.level >= 16:
				self.powerPoints = 221
				self.learnPower(8)

			if self.level >= 17:
				self.powerPoints = 250
				self.learnPower(9)

			if self.level >= 18:
				self.powerPoints = 280
				self.learnPower(9)

			if self.level >= 19:
				self.powerPoints = 311
				self.learnPower(9)

			if self.level >= 20:
				self.powerPoints = 343
				self.learnPower(9)

			# CALCULATE BONUS POWER POINTS
			self.powerPoints += int((self. level * self.wisMod) / 2)

		#PSION
		elif self.clas == 'Psion':
			self.tags.update(['Unarmored', 'Psionic'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(6)
			self.powerPoints = 0 # this is calculated later
			self.BAB = int(0.5 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.classSkills = ['Craft', 'Knowledge(Arcana)', 'Knowledge(Engineering)', 'Knowledge(Dungeoneering)', 'Knowledge(Geography)', 'Knowledge(History)', 'Knowledge(Local)', 'Knowledge(Nature)', 'Knowledge(Nobility)', 'Knowledge(Psionics)', 'Knowledge(Planar)', 'Knowledge(Religion)', 'Profession', 'Psicraft']
			self.skillsAtMax = 2 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			

			# PSIONICS & OTHER SPECIAL ABILITIES
			# DETERMINE DISCIPLINE
			psionDisciplines = ['Seer(Clairsentience)', 'Shaper(Metacreativity)', 'Kineticist(Psychokinesis)', 'Egoist(Psychometabolism)', 'Nomad(Psychoportation)', 'Telepath(Telepathy)']
			self.specialList.append(psionDisciplines[random.randint(0,5)])
			if 'Seer(Clairsentience)' in self.specialList:
				self.classSkills.extend(['Sense Motive', 'Perception'])
			elif 'Shaper(Metacreativity)' in self.specialList:
				self.classSkills.extend(['Bluff', 'Disguise', 'Use Psionic Device'])
			elif 'Kineticist(Psychokinesis)' in self.specialList:
				self.classSkills.extend(['Autohypnosis', 'Disable Device', 'Intimidate'])
			elif 'Egoist(Psychometabolism)' in self.specialList:
				self.classSkills.extend(['Acrobatics', 'Autohypnosis', 'Heal'])
			elif 'Nomad(Psychoportation)' in self.specialList:
				self.classSkills.extend(['Acrobatics', 'Climb', 'Ride', 'Survival', 'Swim'])
			elif 'Telepath(Telepathy)' in self.specialList:
				self.classSkills.extend(['Bluff', 'Diplomacy', 'Sense Motive'])

			self.calcSkills()

			self.powerList = []
			if self.level >= 1:
				self.getPsionBonusFeat(1)
				self.powerPoints = 2
				self.learnPower(1)
				self.learnPower(1)
				self.learnPower(1)

			if self.level >= 2:
				self.powerPoints = 6
				self.learnPower(1)
				self.learnPower(1)

			if self.level >= 3:
				self.powerPoints = 11
				self.learnPower(2)
				self.learnPower(2)

			if self.level >= 4:
				self.powerPoints = 17
				self.learnPower(2)
				self.learnPower(2)

			if self.level >= 5:
				self.getPsionBonusFeat(5)
				self.powerPoints = 25
				self.learnPower(3)
				self.learnPower(3)

			if self.level >= 6:
				self.powerPoints = 35
				self.learnPower(3)
				self.learnPower(3)

			if self.level >= 7:
				self.powerPoints = 46
				self.learnPower(4)
				self.learnPower(4)

			if self.level >= 8:
				self.powerPoints = 58
				self.learnPower(4)
				self.learnPower(4)

			if self.level >= 9:
				self.powerPoints = 72
				self.learnPower(5)
				self.learnPower(5)

			if self.level >= 10:
				self.getPsionBonusFeat(10)
				self.powerPoints = 88
				self.learnPower(5)
				self.learnPower(5)

			if self.level >= 11:
				self.powerPoints = 106
				self.learnPower(6)

			if self.level >= 12:
				self.powerPoints = 126
				self.learnPower(6)
				self.learnPower(6)

			if self.level >= 13:
				self.powerPoints = 147
				self.learnPower(7)

			if self.level >= 14:
				self.powerPoints = 170
				self.learnPower(7)
				self.learnPower(7)

			if self.level >= 15:
				self.getPsionBonusFeat(15)
				self.powerPoints = 195
				self.learnPower(8)

			if self.level >= 16:
				self.powerPoints = 221
				self.learnPower(8)
				self.learnPower(8)

			if self.level >= 17:
				self.powerPoints = 250
				self.learnPower(9)

			if self.level >= 18:
				self.powerPoints = 280
				self.learnPower(9)
				self.learnPower(9)

			if self.level >= 19:
				self.powerPoints = 311
				self.learnPower(9)

			if self.level >= 20:
				self.getPsionBonusFeat(20)
				self.powerPoints = 343
				self.learnPower(9)
				self.learnPower(9)

			# CALCULATE BONUS POWER POINTS
			self.powerPoints += int((self. level * self.intMod) / 2)

		# WILDER
		elif self.clas == 'Wilder':
			self.tags.update(['Light Armor', 'Psionic'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(6)
			self.powerPoints = 0 # this is calculated later
			self.BAB = int(0.5 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(0.5 * self.level) + 2 + self.wisMod
			self.classSkills = ['Acrobatics', 'Autohypnosis', 'Bluff', 'Climb', 'Craft', 'Escape Artist', 'Intimidate', 'Knowledge(Psionics)', 'Perception', 'Profession', 'Psicraft', 'Sense Motive', 'Swim']
			self.skillsAtMax = 2 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# PSIONICS & OTHER SPECIAL ABILITIES
			wildSurge = ((self.level + 1) / 4) + 1
			surgingEuphoria = ((self.level +4) / 8)
			self.powerList = []
			if self.level >= 1:
				self.powerPoints = 2
				self.specialList.append('Wild Surge +{}'.format(wildSurge))
				self.specialList.append('Psychic Enervation')
				self.learnPower(1)
			if self.level >= 2:
				self.powerPoints = 6
				self.specialList.append('Elude Touch')
				self.touchArmorClass += self.chaMod
				if self.touchArmorClass > self.armorClass:
					self.touchArmorClass = self.armorClass
				self.learnPower(1)
			if self.level >= 3:
				self.powerPoints = 11
			if self.level >= 4:
				self.powerPoints = 17
				self.specialList.append('Surging Euphoria +{}'.format(surgingEuphoria))
				self.learnPower(2)
			if self.level >= 5:
				self.powerPoints = 25
				self.specialList.append('Expanded Knowledge')
			if self.level >= 6:
				self.powerPoints = 35
				self.learnPower(3)
			if self.level >= 7:
				self.powerPoints = 46
			if self.level >= 8:
				self.powerPoints = 58
				self.learnPower(4)
			if self.level >= 9:
				self.powerPoints = 72
				self.specialList.append('Expanded Knowledge')
			if self.level >= 10:
				self.powerPoints = 88
				self.learnPower(5)
			if self.level >= 11:
				self.powerPoints = 106
			if self.level >= 12:
				self.powerPoints = 126
				self.learnPower(6)
			if self.level >= 13:
				self.powerPoints = 147
				self.specialList.append('Expanded Knowledge')
			if self.level >= 14:
				self.powerPoints = 170
				self.learnPower(7)
			if self.level >= 15:
				self.powerPoints = 195
			if self.level >= 16:
				self.powerPoints = 221
				self.learnPower(8)
			if self.level >= 17:
				self.powerPoints = 250
				self.specialList.append('Expanded Knowledge')
			if self.level >= 18:
				self.powerPoints = 280
				self.learnPower(9)
			if self.level >= 19:
				self.powerPoints = 311
			if self.level >= 20:
				self.powerPoints = 343
				self.learnPower(9)

			# CALCULATE BONUS POWER POINTS
			self.powerPoints += int((self. level * self.chaMod) / 2)

		# DRUID
		elif self.clas == 'Druid':
			self.tags.update(['Druid Armor', 'Spellcaster', 'Natural', 'Prepared'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(8)
			self.BAB = int(0.75 * self.level)
			self.fortSave = int(self.level / 2) + 2 + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(self.level / 2) + 2 + self.wisMod
			self.classSkills = ['Climb', 'Craft', 'Fly', 'Handle Animal', 'Heal', 'Knowledge(Geography)', 'Knowledge(Nature)', 'Perception', 'Profession', 'Ride', 'Spellcraft', 'Survival', 'Swim']
			self.skillsAtMax = 4 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

			# CLASS FEATURES
			self.spellsPerDay = []
			if self.level >= 1:
				# NATURE BOND
				domainOrCompanion = random.randint(0,1)
				if domainOrCompanion == 0:
					# DOMAIN
					choices = ['Air', 'Animal', 'Earth', 'Fire', 'Plant', 'Water', 'Weather']
					whichDomain = choices[random.randint(0,len(choices)-1)]
					self.specialList.append('Nature Bond: Domain')
					self.specialList.append('{} Domain'.format(whichDomain))
				elif domainOrCompanion == 1:
					# ANIMAL COMPANION
					choices = ['Allosaurus', 'Ankylosaurus', 'Giant Ant', 'Antelope', 'Ape', 'Aurochs', 'Axe Beak', 'Baboon', 'Badger', 'Barbed Ram', 'Dire Bat', 'Bear', 'Giant Beetle', 'Bird', 'Boar', 'War Bull', 'Camel', 'Lion', 'Tiger', 'Cheetah', 'Leopard', 'Giant Chameleon', 'Giant Crab', 'Giant Gecko', 'Giraffe', 'Goblin Dog', 'Hippopotamus', 'Horse', 'Hyena', 'Iguanadon', 'Kangaroo', 'Llama', 'Giant Leech', 'Manta Ray', 'Giant Mantis', 'Megaloceros', 'Monitor Lizard', 'Moose', 'Octopus', 'Orca', 'Ostrich', 'Panda', 'Pony', 'Ram', 'Dire Rat', 'Giant Raven', 'Rhinoceros', 'Roc', 'Giant Scorpion', 'Shark', 'Giant Slug', 'Constrictor Snake', 'Viper Snake', 'Snapping Turtle', 'Giant Spider', 'Squid', 'Stag', 'Stegosaurus', 'Giant Toad', 'Tortoise', 'Triceratops', 'Tyrannosaurus', 'Giant Vulture', 'Walrus', 'Giant Wasp', 'Giant Weasel', 'Wolf']
					whichCompanion = choices[random.randint(0,len(choices)-1)]
					self.specialList.append('Nature Bond: Animal Companion')
					self.specialList.append('{} Companion'.format(whichCompanion))
				self.specialList.append('Nature Sense')
				self.specialList.append('Wild Empathy')
				self.spellsPerDay.append(3)
				self.spellsPerDay.append(1)
			if self.level >= 2:
				self.specialList.append('Woodland Stride')
				self.spellsPerDay[0] += 1
				self.spellsPerDay[1] += 1
			if self.level >= 3:
				self.specialList.append('Trackless Step')
				self.spellsPerDay.append(1)
			if self.level >= 4:
				self.specialList.append("Resist Nature's Lure")
				if self.level >= 20:
					self.specialList.append('Wild Shape (At Will)')
				else:
					self.specialList.append('Wild Shape ({}/day)'.format((self.level - 2) / 2))
				self.spellsPerDay[1] += 1
				self.spellsPerDay[2] += 1
			if self.level >= 5:
				self.spellsPerDay.append(1)
			if self.level >= 6:
				self.spellsPerDay[2] += 1
				self.spellsPerDay[3] += 1
			if self.level >= 7:
				self.spellsPerDay[1] += 1
				self.spellsPerDay.append(1)
			if self.level >= 8:
				self.spellsPerDay[3] += 1
				self.spellsPerDay[4] += 1
			if self.level >= 9:
				self.specialList.append('Venom Immunity')
				self.spellsPerDay[2] += 1
				self.spellsPerDay.append(1)
			if self.level >= 10:
				self.spellsPerDay[4] += 1
				self.spellsPerDay[5] += 1
			if self.level >= 11:
				self.spellsPerDay[3] += 1
				self.spellsPerDay.append(1)
			if self.level >= 12:
				self.spellsPerDay[5] += 1
				self.spellsPerDay[6] += 1
			if self.level >= 13:
				self.specialList.append('A Thousand Faces')
				self.spellsPerDay[4] += 1
				self.spellsPerDay.append(1)
			if self.level >= 14:
				self.spellsPerDay[6] += 1
				self.spellsPerDay[7] += 1
			if self.level >= 15:
				self.specialList.append('Timeless Body')
				self.spellsPerDay[5] += 1
				self.spellsPerDay.append(1)
			if self.level >= 16:
				self.spellsPerDay[7] += 1
				self.spellsPerDay[8] += 1
			if self.level >= 17:
				self.spellsPerDay[6] += 1
				self.spellsPerDay.append(1)
			if self.level >= 18:
				self.spellsPerDay[8] += 1
				self.spellsPerDay[9] += 1
			if self.level >= 19:
				self.spellsPerDay[7] += 1
				self.spellsPerDay[9] += 1
			if self.level >= 20:
				self.spellsPerDay[8] += 1
				self.spellsPerDay[9] += 1

			self.calcBonusSpells(self.wisMod)
			self.prepareSpells()

		# RANGER
		elif self.clas == 'Ranger':
			self.tags.update(['Medium Armor', 'Spellcaster', 'Natural', 'Sneaky', 'Prepared'])
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(10)
			self.BAB = self.level
			self.fortSave = 2 + int(self.level / 2) + self.conMod
			self.refSave = 2 + int(self.level / 2) + self.dexMod
			self.willSave = int(self.level /3) + self.wisMod
			self.classSkills = ['Climb', 'Craft', 'Handle Animal', 'Heal', 'Intimidate', 'Knowledge(Dungeoneering)', 'Knowledge(Geography)', 'Knowledge(Nature)', 'Perception', 'Profession', 'Ride', 'Spellcraft', 'Stealth', 'Survival', 'Swim']
			self.skillsAtMax = 6 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()
			
			# OTHER SPECIAL ABILITIES
			favoredEnemyChoices = ['Aberration', 'Animal', 'Construct', 'Dragon', 'Fey', 'Humanoid(Aquatic)', 'Humanoid(Dwarf)', 'Humanoid(Elf)', 'Humanoid(Giant)', 'Humanoid(Goblinoid)', 'Humanoid(Gnoll)', 'Humanoid(Gnome)', 'Humanoid(Halfling)', 'Humanoid(Human)', 'Humanoid(Orc)','Humanoid(Reptilian)', 'Magical Beast', 'Monstrous Humanoid', 'Ooze', 'Outsider(Air)', 'Outsider(Chaotic)', 'Outsider(Earth)', 'Outsider(Evil)', 'Outsider(Fire)', 'Outsider(Good)', 'Outsider(Lawful)', 'Outsider(Native)', 'Outsider(Water)', 'Plant', 'Undead', 'Vermin']
			self.favoredEnemies = {}
			favoredTerrainChoices = ['Cold', 'Desert', 'Forest', 'Jungle', 'Mountains', 'Plains', 'Swamps', 'Underground', 'Urban', 'Water']
			self.favoredTerrains = {}
			self.spellsPerDay = []
			whichStyle = '' # this and featChoices are both variables used in choosing combat style and feats
			featChoices = []
			if self.level >= 1:
				# CHOOSE FAVORED ENEMY
				whichEnemy = favoredEnemyChoices[random.randint(0,len(favoredEnemyChoices)-1)]
				self.favoredEnemies[whichEnemy] = 2
				favoredEnemyChoices.remove(whichEnemy)
			if self.level >= 2:
				combatStyleChoices = ['Archery', 'Two-Weapon Combat', 'Crossbow', 'Mounted Combat', 'Natural Weapon', 'Thrown Weapon', 'Two-Handed Weapon', 'Weapon & Shield']
				whichStyle = combatStyleChoices[random.randint(0,len(combatStyleChoices)-1)]
				self.specialList.append('Combat Style: {}'.format(whichStyle))
				if whichStyle == 'Archery':
					self.tags.update('Ranged Attacker')
					featChoices.extend(['Far Shot', 'Focused Shot', 'Point Blank Shot', 'Precise Shot', 'Rapid Shot'])
				elif whichStyle == 'Two-Weapon Combat':
					self.tags.update(['Two Weapons', 'Melee'])
					featChoices.extend(['Double Slice', 'Improved Shield Bash', 'Quick Draw', 'Two-Weapon Fighting'])
				elif whichStyle == 'Crossbow:':
					self.tags.update('Ranged Attacker')
					featChoices.extend(['Deadly Aim', 'Focused Shot', 'Precise Shot', 'Rapid Reload'])
				elif whichStyle == 'Mounted Combat':
					self.tags.update('Mounted')
					featChoices.extend(['Mounted Combat', 'Mounted Archery', 'Ride-By Attack', 'Trick Riding'])
				elif whichStyle == 'Natural Weapon':
					self.tags.update(['Melee'])
					featChoices.extend(['Aspect of the Beast', 'Improved Natural Attack', 'Rending Claws', 'Weapon Focus'])
				elif whichStyle == 'Thrown Weapon':
					self.tags.update('Ranged Attacker')
					featChoices.extend(['Distance Thrower', 'Precise Shot', 'Quick Draw', 'Two-Weapon Fighting'])
				elif whichStyle == 'Two-Handed Weapon':
					self.tags.update(['Melee', 'Big Weapon'])
					featChoices.extend(['Cleave', 'Power Attack', 'Pushing Assault', 'Shield of Swings'])
				elif whichStyle == 'Weapon & Shield':
					self.tags.update(['Melee', 'Shield'])
					featChoices.extend(['Improved Shield Bash', 'Shield Focus', 'Shield Slam', 'Two-Weapon Fighting'])
				else:
					print 'Error: not finding which combat style dudeman has'
				chosen = False
				while not chosen:
					whichFeat = random.choice(featChoices)
					if whichFeat not in self.featList:
						self.featList.append(whichFeat)
						chosen = True
					else:
						print '{} already known! Looking again...'.format(whichFeat)
			if self.level >= 3:
				self.featList.append('Endurance')
				# CHOOSE FAVORED TERRAIN
				whichTerrain = favoredTerrainChoices[random.randint(0,len(favoredTerrainChoices)-1)]
				self.favoredTerrains[whichTerrain] = 2
				favoredTerrainChoices.remove(whichTerrain)
			if self.level >= 4:
				partyOrAnimal = random.randint(0,1)
				if partyOrAnimal == 0:
					self.specialList.append("Hunter's Bond: Party")
				elif partyOrAnimal == 1:
					# ANIMAL COMPANION
					choices = ['Allosaurus', 'Ankylosaurus', 'Giant Ant', 'Antelope', 'Ape', 'Aurochs', 'Axe Beak', 'Baboon', 'Badger', 'Barbed Ram', 'Dire Bat', 'Bear', 'Giant Beetle', 'Bird', 'Boar', 'War Bull', 'Camel', 'Lion', 'Tiger', 'Cheetah', 'Leopard', 'Giant Chameleon', 'Giant Crab', 'Giant Gecko', 'Giraffe', 'Goblin Dog', 'Hippopotamus', 'Horse', 'Hyena', 'Iguanadon', 'Kangaroo', 'Llama', 'Giant Leech', 'Manta Ray', 'Giant Mantis', 'Megaloceros', 'Monitor Lizard', 'Moose', 'Octopus', 'Orca', 'Ostrich', 'Panda', 'Pony', 'Ram', 'Dire Rat', 'Giant Raven', 'Rhinoceros', 'Roc', 'Giant Scorpion', 'Shark', 'Giant Slug', 'Constrictor Snake', 'Viper Snake', 'Snapping Turtle', 'Giant Spider', 'Squid', 'Stag', 'Stegosaurus', 'Giant Toad', 'Tortoise', 'Triceratops', 'Tyrannosaurus', 'Giant Vulture', 'Walrus', 'Giant Wasp', 'Giant Weasel', 'Wolf']
					whichCompanion = choices[random.randint(0,len(choices)-1)]
					self.specialList.append("Hunter's Bond: Animal Companion")
					self.specialList.append('{} Companion'.format(whichCompanion))
				self.spellsPerDay.append(0)
			if self.level >= 5:
				whichEnemy = favoredEnemyChoices[random.randint(0,len(favoredEnemyChoices)-1)] # choosing a second favored enemy
				self.favoredEnemies[whichEnemy] = 2
				favoredEnemyChoices.remove(whichEnemy)
				self.favoredEnemies[random.choice(self.favoredEnemies.keys())] += 2
				# random.choice(self.favoredEnemies.values()) += 2 # increase a random favored enemy bonus by 2
				self.spellsPerDay[0] += 1
			if self.level >= 6:
				if whichStyle == 'Archery':
					featChoices.extend(['Crossbow Mastery', 'Improved Precise Shot', 'Parting Shot', 'Point Blank Master', 'Manyshot'])
				elif whichStyle == 'Crossbow':
					featChoices.extend(['Crossbow Mastery', 'Improved Precise Shot'])
				elif whichStyle == 'Mounted Combat':
					featChoices.extend(['Mounted Shield', 'Spirited Charge'])
				elif whichStyle == 'Natural Weapon':
					featChoices.extend(['Eldritch Claws', 'Vital Strike'])
				elif whichStyle == 'Thrown Weapon':
					featChoices.extend(['Close-Quarters Thrower', 'False Opening'])
				elif whichStyle == 'Two-Handed Weapon':
					featChoices.extend(['Furious Focus', 'Great Cleave'])
				elif whichStyle == 'Two-Weapon Combat':
					featChoices.extend(['Improved Two-Weapon Fighting', 'Two-Weapon Defense'])
				elif whichStyle == 'Weapon & Shield':
					featChoices.extend(['Saving Shield', 'Shield Master'])
				else:
					print 'Error: not finding which combat style dudeman has'
				chosen = False
				while not chosen:
					whichFeat = featChoices[random.randint(0,len(featChoices)-1)]
					if whichFeat not in self.featList:
						self.featList.append(whichFeat)
						chosen = True
					else:
						print '{} already known! Looking again...'.format(whichFeat)
			if self.level >= 7:
				self.specialList.append('Woodland Stride')
				self.spellsPerDay.append(0)
			if self.level >= 8:
				self.specialList.append('Swift Tracker')
				whichTerrain = favoredTerrainChoices[random.randint(0,len(favoredTerrainChoices)-1)] # choosing a second favored terrain
				self.favoredTerrains[whichTerrain] = 2
				favoredTerrainChoices.remove(whichTerrain)
				self.favoredTerrains[random.choice(self.favoredTerrains.keys())] += 2
				# random.choice(self.favoredEnemies.values()) += 2 # increase a random favored terrain bonus by 2
				self.spellsPerDay[1] += 1
			if self.level >= 9:
				self.specialList.append('Evasion')
				self.spellsPerDay[0] += 1
			if self.level >= 10:
				whichEnemy = favoredEnemyChoices[random.randint(0,len(favoredEnemyChoices)-1)] # choosing a third favored enemy
				self.favoredEnemies[whichEnemy] = 2
				favoredEnemyChoices.remove(whichEnemy)
				self.favoredEnemies[random.choice(self.favoredEnemies.keys())] += 2
				if whichStyle == 'Archery':
					featChoices.extend(['Pinpoint Targting', 'Shot on the Run'])
				elif whichStyle == 'Crossbow':
					featChoices.extend(['Pinpoint Targeting', 'Shot on the Run'])
				elif whichStyle == 'Mounted Combat':
					featChoices.extend(['Mounted Skirmisher', 'Unseat'])
				elif whichStyle == 'Natural Weapon':
					featChoices.extend(['Multiattack', 'Improved Vital Strike'])
				elif whichStyle == 'Thrown Weapon':
					featChoices.extend(['Pinpoint Targeting', 'Shot on the Run'])
				elif whichStyle == 'Two-Handed Weapon':
					featChoices.extend(['Dreadful Carnage', 'Improved Sunder'])
				elif whichStyle == 'Two-Weapon Combat':
					featChoices.extend(['Greater Two-Weapon Fighting', 'Two-Weapon Rend'])
				elif whichStyle == 'Weapon & Shield':
					featChoices.extend(['Bashing Finish', 'Greater Shield Focus'])
				else:
					print 'Error: not finding which combat style dudeman has'
				chosen = False
				while not chosen:
					whichFeat = featChoices[random.randint(0,len(featChoices)-1)]
					if whichFeat not in self.featList:
						self.featList.append(whichFeat)
						chosen = True
					else:
						print '{} already known! Looking again...'.format(whichFeat)
				self.spellsPerDay.append(0)
			if self.level >= 11:
				self.specialList.append('Quarry')
				self.spellsPerDay[2] += 1
			if self.level >= 12:
				self.specialList.append('Camouflage')
				self.spellsPerDay[1] += 1
			if self.level >= 13:
				whichTerrain = favoredTerrainChoices[random.randint(0,len(favoredTerrainChoices)-1)] # choosing a third favored terrain
				self.favoredTerrains[whichTerrain] = 2
				favoredTerrainChoices.remove(whichTerrain) # removing the chosen terrain from the list of options means we don't have to check if the one we chose is already known
				self.favoredTerrains[random.choice(self.favoredTerrains.keys())] += 2
				self.spellsPerDay[0] += 1
				self.spellsPerDay.append(0)
			if self.level >= 14:
				chosen = False
				while not chosen:
					whichFeat = featChoices[random.randint(0,len(featChoices)-1)]
					if whichFeat not in self.featList:
						self.featList.append(whichFeat)
						chosen = True
					else:
						print '{} already known! Looking again...'.format(whichFeat)
				self.spellsPerDay[3] += 1
			if self.level >= 15:
				whichEnemy = favoredEnemyChoices[random.randint(0,len(favoredEnemyChoices)-1)] # choosing a fourth favored enemy
				self.favoredEnemies[whichEnemy] = 2
				favoredEnemyChoices.remove(whichEnemy)
				self.favoredEnemies[random.choice(self.favoredEnemies.keys())] += 2
				self.spellsPerDay[2] += 1
			if self.level >= 16:
				self.specialList.append('Improved Evasion')
				self.spellsPerDay[1] += 1
			if self.level >= 17:
				self.specialList.append('Hide in Plain Sight')
				self.spellsPerDay[0] += 1
			if self.level >= 18:
				whichTerrain = favoredTerrainChoices[random.randint(0,len(favoredTerrainChoices)-1)] # choosing a second favored terrain
				self.favoredTerrains[whichTerrain] = 2
				favoredTerrainChoices.remove(whichTerrain)
				self.favoredTerrains[random.choice(self.favoredTerrains.keys())] += 2
				chosen = False
				while not chosen:
					whichFeat = featChoices[random.randint(0,len(featChoices)-1)]
					if whichFeat not in self.featList:
						self.featList.append(whichFeat)
						chosen = True
					else:
						print '{} already known! Looking again...'.format(whichFeat)
				self.spellsPerDay[3] += 1
			if self.level >= 19:
				self.specialList.append('Improved Quarry')
				self.spellsPerDay[2] += 1
			if self.level >= 20:
				self.specialList.append('Master Hunter')
				whichEnemy = favoredEnemyChoices[random.randint(0,len(favoredEnemyChoices)-1)] # choosing a third favored enemy
				self.favoredEnemies[whichEnemy] = 2
				favoredEnemyChoices.remove(whichEnemy)
				self.favoredEnemies[random.choice(self.favoredEnemies.keys())] += 2
				self.spellsPerDay[1] += 1
				self.spellsPerDay[3] += 1


			# got to add all the favored enemies and terrains to self.specialList
			for item in self.favoredEnemies:
				self.specialList.append('Favored Enemy: {} +{}'.format(item, self.favoredEnemies[item]))
			for item in self.favoredTerrains:
				self.specialList.append('Favored Terrain: {} +{}'.format(item, self.favoredTerrains[item]))
			self.calcBonusSpells(self.wisMod)
			self.prepareSpells()

		elif self.clas == 'Commoner':
			# CLASS CHASSIS
			self.hitPoints = self.calcHitPoints(4)
			self.BAB = int(0.5 * self.level)
			self.fortSave = int(self.level / 3) + self.conMod
			self.refSave = int(self.level / 3) + self.dexMod
			self.willSave = int(self.level / 3) + self.wisMod
			self.classSkills = ['Climb', 'Craft', 'Handle Animal', 'Jump', 'Perception', 'Profession', 'Ride', 'Swim', 'Use Rope']
			self.skillsAtMax = 2 + self.intMod
			if self.race == 'Human':
				self.skillsAtMax += 1
			self.calcSkills()

		print 'Class features assigned!'



	# function to prepare spells 
	def prepareSpells(self):
		if self.clas == 'Paladin':
			self.spellsPrepared = [[], [], [], []]
			for i  in xrange(len(self.spellsPerDay)):
				while len(self.spellsPrepared[i]) < self.spellsPerDay[i]:
					self.spellsPrepared[i].append(random.choice(paladinSpells[i]))

		if self.clas == 'Ranger':
			self.spellsPrepared = [[], [], [], []]
			for i in xrange(len(self.spellsPerDay)):
				while len(self.spellsPrepared[i]) < self.spellsPerDay[i]:
					self.spellsPrepared[i].append(random.choice(rangerSpells[i]))

		if self.clas == 'Druid':
			self.spellsPrepared = [[], [], [], [], [], [], [], [], [], []]
			for i in xrange(len(self.spellsPerDay)):
				while len(self.spellsPrepared[i]) < self.spellsPerDay[i]:
					self.spellsPrepared[i].append(random.choice(druidSpells[i]))
			if 'Nature Bond: Domain' in self.specialList:
				for i in xrange(len(self.spellsPerDay)-1):
					self.spellsPrepared[i+1].append(domainSpells[self.specialList[self.specialList.index('Nature Bond: Domain')+1]][i])

	# function to assign the character its spells known
	def learnSpells(self):
		if self.clas == 'Bard':
			self.spellList = [[], [], [], [], [], [], []]
			for i in xrange(len(self.spellsKnown)):
				while len(self.spellList[i]) < self.spellsKnown[i]:
					whichSpell = bardSpells[i][random.randint(0,len(bardSpells[i])-1)]
					if whichSpell not in self.spellList[i]:
						self.spellList[i].append(whichSpell)

		if self.clas == 'Beguiler':
			for i in xrange(len(self.spellsPerDay)+1): # +1 b/c cantrips
				self.spellList.append(beguilerSpells[i])
					
		if self.clas == 'Dread Necromancer':
			for i in xrange(len(self.spellsPerDay)): # dread necros dont have cantrips
				self.spellList.append(dreadNecroSpells[i])

		if self.clas == 'Warmage':
			for i in xrange(len(self.spellsPerDay)+1): # +1 b/c cantrips
				self.spellList.append(warmageSpells[i])

	# function to handle the Advanced Learning class feature in Beguiler, Dread Necromancer, and Warmage
	def advancedLearning(self,spellLevel):
		choice = ''
		if self.clas == 'Beguiler':
			choice = random.choice(beguilerADSpells[spellLevel])
		elif self.clas == 'Dread Necromancer':
			choice = random.choice(dreadNecroADSpells[spellLevel])
			spellLevel -= 1 # gotta do this because they have no cantrips
		elif self.clas == 'Warmage':
			choice = random.choice(warmageADSpells[spellLevel])
		self.spellList[spellLevel].append(choice)
		self.specialList.append('Advanced Learning ({})'.format(choice))
		return choice
		
	# function that randomly gives the character a Psionic Mantle
	def assumePsionicMantle(self):
		mantleChoices = ['Chaos', 'Communication', 'Conflict', 'Consumption', 'Corruption & Madness', 'Creation', 'Death', 'Deception', 'Destruction', 'Elements', 'Energy', 'Evil', 'Fate', 'Force', 'Freedom', 'Good', 'Guardian', 'Justice', 'Knowledge', 'Law', 'Life', 'Light & Darkness', 'Magic', 'Mental Power', 'Natural World', 'Pain & Suffering', 'Physical Power', 'The Planes', 'Repose', 'Time']
		while mantleChoices:
			whichMantle = mantleChoices[random.randint(0,len(mantleChoices)-1)]
			if whichMantle in self.mantleList:
				mantleChoices.remove(whichMantle)
			else:
				self.mantleList.append(whichMantle)
				self.specialList.append('{} Mantle'.format(whichMantle))
				return whichMantle

	# function to determine a Psion bonus feat given the level it is earned at
	def getPsionBonusFeat(self,lvl):
		featChoices = ['Body Fuel', 'Burrowing Power', 'Chain Power', 'Closed Mind', 'Combat Manifestation', 'Delay Power', 'Empower Power', 'Enlarge Power', 'Extend Power', 'Maximize Power', 'Opportunity Power', 'Overchannel', 'Power Penetration', 'Psicrystal Affinity', 'Psionic Body', 'Quicken Power', 'Twin Power', 'Unconditional Power', 'Widen Power']
		if lvl >= 3:
			featChoices.append('Craft Universal Item')
			featChoices.append('Psicrystal Containment')
			featChoices.append('Scribe Tattoo')
		if lvl >= 5:
			featChoices.append('Craft Psionic Arms and Armor')
			featChoices.append('Craft Dorje')
		if lvl >= 6:
			featChoices.append('Ghost Attack')
		if lvl >= 12:
			featChoices.append('Craft Psicrown')
			if 'Power Specialization' and 'Weapon Focus' in self.featList:
				featChoices.append('Greater Power Specialization')

		if 'Craft Universal Item' in self.featList:
			featChoices.append('Craft Psionic Construct')
		if 'Dodge' in self.featList:
			featChoices.append('Psionic Dodge')
		if 'Overchannel' in self.featList:
			featChoices.append('Talented')
		if 'Power Penetration' in self.featList:
			featChoices.append('Greater Power Penetration')
		if 'Psionic Endowment' in self.featList:
			featChoices.append('Greater Psionic Endowment')
		if 'Weapon Focus' in self.featList:
			featChoices.append('Power Specialization')

		if self.strength >= 13:
			featChoices.append('Psionic Fist')
			featChoices.append('Psionic Weapon')
		if self.dexterity >= 13:
			if 'Speed of Thought' in self.featList:
				featChoices.append('Psionic Charge')
		if self.constitution >= 13:
			featChoices.append('Rapid Metabolism')
		if self.constitution >= 15:
			featChoices.append('Psionic Hole')
		if self.wisdom >= 13:
			featChoices.append('Inquisitor')
			featChoices.append('Narrow Mind')
			featChoices.append('Speed of Thought')
			featChoices.append('Up the Walls')
		if self.charisma >= 15:
			featChoices.append('Hostile Mind')

		while featChoices:
			whichFeat = featChoices[random.randint(0,len(featChoices)-1)]
			if whichFeat in self.featList:
				featChoices.remove(whichFeat)
			else:
				self.featList.append(whichFeat)
				return whichFeat


	# function for use inside the learnPower function
	# randomly chooses a power from a given list and checks if it's
	# already known by the character. It loops through the available
	# list and returns the name of the power if one is found. Otherwise
	# it will return 0
	def choosePower(self,powerChoices):
		while powerChoices:
			whichPower = powerChoices[random.randint(0,len(powerChoices)-1)]
			if whichPower not in self.powerList:
				return whichPower
			else:
				powerChoices.remove(whichPower)
		return 0

	# function to choose and learn a power for the character
	def learnPower(self,lvl):
		powerChoices = []
		if self.clas == 'Ardent':
			for i in xrange(lvl):
				if 'Chaos' in self.mantleList:
					powerChoices.extend(chaosMantle[i])
				if 'Communication' in self.mantleList:
					powerChoices.extend(communicationMantle[i])
				if 'Conflict' in self.mantleList:
					powerChoices.extend(conflictMantle[i])
				if 'Consumption' in self.mantleList:
					powerChoices.extend(consumptionMantle[i])
				if 'Corruption & Madness' in self.mantleList:
					powerChoices.extend(corruptionAndMadnessMantle[i])
				if 'Creation' in self.mantleList:
					powerChoices.extend(creationMantle[i])
				if 'Death' in self.mantleList:
					powerChoices.extend(deathMantle[i])
				if 'Deception' in self.mantleList:
					powerChoices.extend(deceptionMantle[i])
				if 'Destruction' in self.mantleList:
					powerChoices.extend(destructionMantle[i])
				if 'Elements' in self.mantleList:
					powerChoices.extend(elementsMantle[i])
				if 'Energy' in self.mantleList:
					powerChoices.extend(energyMantle[i])
				if 'Evil' in self.mantleList:
					powerChoices.extend(evilMantle[i])
				if 'Fate' in self.mantleList:
					powerChoices.extend(fateMantle[i])
				if 'Force' in self.mantleList:
					powerChoices.extend(forceMantle[i])
				if 'Freedom' in self.mantleList:
					powerChoices.extend(freedomMantle[i])
				if 'Good' in self.mantleList:
					powerChoices.extend(goodMantle[i])
				if 'Guardian' in self.mantleList:
					powerChoices.extend(guardianMantle[i])
				if 'Justice' in self.mantleList:
					powerChoices.extend(justiceMantle[i])
				if 'Knowledge' in self.mantleList:
					powerChoices.extend(knowledgeMantle[i])
				if 'Law' in self.mantleList:
					powerChoices.extend(lawMantle[i])
				if 'Life' in self.mantleList:
					powerChoices.extend(lifeMantle[i])
				if 'Light & Darkness' in self.mantleList:
					powerChoices.extend(lightAndDarknessMantle[i])
				if 'Magic' in self.mantleList:
					powerChoices.extend(magicMantle[i])
				if 'Mental Power' in self.mantleList:
					powerChoices.extend(mentalPowerMantle[i])
				if 'Natural World' in self.mantleList:
					powerChoices.extend(naturalWorldMantle[i])
				if 'Pain & Suffering' in self.mantleList:
					powerChoices.extend(painAndSufferingMantle[i])
				if 'Physical Power' in self.mantleList:
					powerChoices.extend(physicalPowerMantle[i])
				if 'The Planes' in self.mantleList:
					powerChoices.extend(thePlanesMantle[i])
				if 'Repose' in self.mantleList:
					powerChoices.extend(reposeMantle[i])
				if 'Time' in self.mantleList:
					powerChoices.extend(timeMantle[i])
			whichPower = self.choosePower(powerChoices)
			self.powerList.append(whichPower)
			return whichPower

		elif self.clas == 'Psion': # the psion algorithm prioritizes the psion's discipline and then level
			if 'Egoist(Psychometabolism)' in self.specialList:
				for i in xrange(lvl):
					powerChoices.extend(egoistPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
					powerChoices.extend(pwPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
			if 'Kineticist(Psychokinesis)' in self.specialList:
				for i in xrange(lvl):
					powerChoices.extend(kineticistPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
					powerChoices.extend(pwPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
			if 'Nomad(Psychoportation)' in self.specialList:
				for i in xrange(lvl):
					powerChoices.extend(nomadPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
					powerChoices.extend(pwPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
			if 'Seer(Clairsentience)' in self.specialList:
				for i in xrange(lvl):
					powerChoices.extend(seerPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
					powerChoices.extend(pwPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
			if 'Shaper(Metacreativity)' in self.specialList:
				for i in xrange(lvl):
					powerChoices.extend(shaperPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
					powerChoices.extend(pwPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
			if 'Telepath(Telepathy)' in self.specialList:
				for i in xrange(lvl):
					powerChoices.extend(telepathPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower
					powerChoices.extend(pwPowers[lvl-i-1])
					whichPower = self.choosePower(powerChoices)
					if whichPower != 0:
						self.powerList.append(whichPower)
						return whichPower

		elif self.clas == 'Wilder': # the wilder algorithm prioritizes level only
			for i in xrange(lvl):
				powerChoices.extend(pwPowers[lvl-i-1])
				whichPower = self.choosePower(powerChoices)
				if whichPower != 0:
					self.powerList.append(whichPower)
					return whichPower

	# function that calculates bonus spells per day up to a score of 30 
	# (this generator only creates characters with a max score of 23)
	def calcBonusSpells(self,modifier):
		# print 'Intial spells per day: {}'.format(self.spellsPerDay)
		if modifier == 1:
			bonusSpells = [1,0,0,0,0,0,0,0,0]
		elif modifier == 2:
			bonusSpells = [1,1,0,0,0,0,0,0,0]
		elif modifier == 3:
			bonusSpells = [1,1,1,0,0,0,0,0,0]
		elif modifier == 4:
			bonusSpells = [1,1,1,1,0,0,0,0,0]
		elif modifier == 5:
			bonusSpells = [2,1,1,1,1,0,0,0,0]
		elif modifier == 6:
			bonusSpells = [2,2,1,1,1,1,0,0,0]
		elif modifier == 7:
			bonusSpells = [2,2,2,1,1,1,1,0,0]
		elif modifier == 8:
			bonusSpells = [2,2,2,2,1,1,1,1,0]
		elif modifier == 9:
			bonusSpells = [3,2,2,2,2,1,1,1,1]
		elif modifier <= 10:
			bonusSpells = [3,3,2,2,2,2,1,1,1]

		if self.clas == 'Druid': # druids have to prepare their orisons so they still have a spellsPerDay whose first element is the number of orisons they can prepare
			for i in xrange(9):
				if i+2 <= len(self.spellsPerDay):
					# print 'Level {} Spells Per Day: {} = {} + {}'.format(i+1, self.spellsPerDay[i+1] + bonusSpells[i], self.spellsPerDay[i+1], bonusSpells[i])
					self.spellsPerDay[i+1] += bonusSpells[i]
		else:
			# print 'Calculating bonus spells for this {}...'.format(self.clas)
			# print bonusSpells
			for i in xrange(9):
				if i+1 <= len(self.spellsPerDay):
					# print 'Level {} Spells Per Day: {} = {} + {}'.format(i+1, self.spellsPerDay[i] + bonusSpells[i], self.spellsPerDay[i], bonusSpells[i])
					self.spellsPerDay[i] += bonusSpells[i]
		
		# print 'Final spells per day: {}'.format(self.spellsPerDay)


	# function to find the character a new Sublime maneuver
	# param, lvl, is the level at which the maneuver is learned
	# returns the name of the new maneuver
	# also increments the character's number of known maneuvers
	def learnManeuver(self,lvl):
		# begin by determing the character's highest available maneuver level
		highestLevel = (lvl + 1) / 2

		# if level 9 maneuvers are available the algorithm will choose one of those that is available
		if highestLevel >= 9:
			if 'Desert Wind' in self.availableDiscplines:
				if self.desertWindCount >= 5 and 'Inferno Blast' not in self.maneuverList:
					self.maneuverList.append('Inferno Blast')
					self.desertWindCount += 1
					return 'Inferno Blast'
			if 'Devoted Spirit' in self.availableDiscplines:
				if self.devotedSpiritCount >= 3 and 'Strike of Righteous Vitality' not in self.maneuverList:
					self.maneuverList.append('Strike of Righteous Vitality')
					self.devotedSpiritCount += 1
					return 'Strike of Righteous Vitality'
			if 'Diamond Mind' in self.availableDiscplines:
				if self.diamondMindCount >= 4 and 'Time Stands Still' not in self.maneuverList:
					self.maneuverList.append('Time Stands Still')
					self.diamondMindCount += 1
					return 'Time Stands Still'
			if 'Iron Heart' in self.availableDiscplines:
				if self.ironHeartCount >= 4 and 'Strike of Perfect Clarity' not in self.maneuverList:
					self.maneuverList.append('Strike of Perfect Clarity')
					self.ironHeartCount += 1
					return 'Strike of Perfect Clarity'
			if 'Setting Sun' in self.availableDiscplines:
				if self.settingSunCount >= 5 and 'Tornado Throw' not in self.maneuverList:
					self.maneuverList.append('Tornado Throw')
					self.settingSunCount += 1
					return 'Tornado Throw'
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 5 and 'Five=Shadow Creeping Ice Enervation Strike' not in self.maneuverList:
					self.maneuverList.append('Five-Shadow Creeping Ice Enervation Strike')
					self.shadowHandCount += 1
					return 'Five-Shadow Creeping Ice Enervation Strike'
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 4 and 'Feral Death Blow' not in self.maneuverList:
					self.maneuverList.append('Feral Death Blow')
					self.tigerClawCount += 1
					return 'Feral Death Blow'
			if 'White Raven' in self.availableDiscplines:
				if self.whiteRavenCount >= 4 and "War Master's Charge" not in self.maneuverList:
					self.maneuverList.append("War Master's Charge")
					self.whiteRavenCount +=1 
					return "War Master's Charge"
			if 'Stone Dragon' in self.availableDiscplines and 'Mountain Tombstone Strike' not in self.maneuverList:
				self.maneuverList.append('Mountain Tombstone Strike')
				self.stoneDragonCount += 1
				return 'Mountain Tombstone Strike'

		# from level 8 down, available maneuver choices will be added to a list and then randomly selected.
		choices = []

		if highestLevel >= 8:
			if 'Desert Wind' in self.availableDiscplines and self.desertWindCount >= 3:
				choices.append('Wyrms Flame')
			if 'Devoted Spirit' in self.availableDiscplines and self.devotedSpiritCount >= 2:
				choices.append('Greater Divine Surge')
			if 'Diamond Mind' in self.availableDiscplines:
				choices.append('Diamond Defense')
				if self.diamondMindCount >= 3:
					choices.append('Diamond Nightmare Blade')
			if 'Iron Heart' in self.availableDiscplines:
				if self.ironHeartCount >= 3:
					choices.append('Adamantine Hurricane')
				if self.ironHeartCount >= 2:
					choices.append('Lightning Throw')
			if 'Setting Sun' in self.availableDiscplines and self.settingSunCount >= 3:
				choices.append("Fool's Strike")
			if 'Shadow Hand' in self.availableDiscplines and self.shadowHandCount >= 3:
					choices.append('Enervating Shadow Strike')
					choices.append('One With Shadow')
			if 'Stone Dragon' in self.availableDiscplines:
				if self.stoneDragonCount >= 3:
					choices.append('Adamantine Bones')
				if self.stoneDragonCount >= 2:
					choices.append('Earthstrike Quake')
			if 'Tiger Claw' in self.availableDiscplines and self.tigerClawCount >= 3:
					choices.append('Girallon Windmill Flesh Rip')
					choices.append('Raging Mongoose')
			if 'White Raven' in self.availableDiscplines and self.whiteRavenCount >= 3:
					choices.append('White Raven Hammer')

		# if there were no choices continue on to the next lowest level
		if highestLevel >= 7 and not choices:
			if 'Desert Wind' in self.availableDiscplines:
				if self.desertWindCount >= 3:
					choices.append('Salamander Charge')
				choices.append('Inferno Blade')
			if 'Devoted Spirit' in self.availableDiscplines and self.devotedSpiritCount >= 2:
				choices.append('Castigating Strike')
				choices.append('Shield Counter')
			if 'Diamond Mind' in self.availableDiscplines and self.diamondMindCount >= 3:
				choices.append('Avalanche of Blades')
				choices.append('Quicksilver Motion')
			if 'Iron Heart' in self.availableDiscplines and self.ironHeartCount >= 3:
				choices.append('Finishing Move')
				choices.append('Scything Blade')
			if 'Setting Sun' in self.availableDiscplines and self.settingSunCount >= 3:
				choices.append('Hydra Slaying Strike')
			if 'Shadow Hand' in self.availableDiscplines:
				choices.append('Shadow Blink')
				choices.append('Death in the Dark')
			if 'Stone Dragon' in self.availableDiscplines:
				if self.stoneDragonCount >= 3:
					choices.append('Ancient Mountain Hammer')
				if self.stoneDragonCount >= 2:
					choices.append('Colossus Strike')
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 3:
					choices.append('Hamstring Attack')
					choices.append('Swooping Dragon Strike')
				if self.tigerClawCount >= 2:
					choices.append('Prey on the Weak')
			if 'White Raven' in self.availableDiscplines and self.whiteRavenCount >= 3:
				choices.append('Clarion Call')
				choices.append('Swarming Assault')

		if highestLevel >= 6 and not choices:
			if 'Desert Wind' in self.availableDiscplines and self.desertWindCount >= 2:
				choices.append('Desert Tempest')
				choices.append('Fiery Assault')
				choices.append('Ring of Fire')
			if 'Devoted Spirit' in self.availableDiscplines and self.devotedSpiritCount >= 2:
				choices.append('Rallying Strike')
			if 'Diamond Mind' in self.availableDiscplines and self.diamondMindCount >= 2:
				choices.append('Greater Insightful Strike')
				choices.append('Moment of Alacrity')
			if 'Iron Heart' in self.availableDiscplines and self.ironHeartCount >= 2:
				choices.append('Iron Heart Endurance')
				choices.append('Manticore Parry')
			if 'Setting Sun' in self.availableDiscplines and self.settingSunCount >= 2:
				choices.append('Ballista Throw')
				choices.append('Scorpion Parry')
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 3:
					choices.append('Ghost Blade')
				choices.append('Shadow Noose')
				choices.append('Stalker in the Night')
			if 'Stone Dragon' in self.availableDiscplines:
				if self.stoneDragonCount >= 2:
					choices.append('Iron Bones')
				choices.append('Crushing Vise')
				choices.append('Irresistable Mountain Strike')
			if 'Tiger Claw' in self.availableDiscplines and self.tigerClawCount >= 2:
				choices.append('Rabid Bear Strike')
				choices.append('Wolf Climbs the Mountain')
			if 'White Raven' in self.availableDiscplines and self.whiteRavenCount >= 2:
					choices.append('Order Forged from Chaos')
					choices.append('War Leaders Charge')

		if highestLevel >= 5 and not choices:
			if 'Desert Wind' in self.availableDiscplines and self.desertWindCount >= 2:
				choices.append('Dragons Flame')
				choices.append('Leaping Flame')
				choices.append('Lingering Inferno')
			if 'Devoted Spirit' in self.availableDiscplines and self.devotedSpiritCount >= 1:
				choices.append('Daunting Strike')
				choices.append('Doom Charge')
				choices.append('Law Bearer')
				choices.append('Radiant Charge')
				choices.append('Tide of Chaos')
			if 'Diamond Mind' in self.availableDiscplines:
				if self.diamondMindCount >= 2:
					choices.append('Disrupting Blow')
				choices.append('Rapid Counter')
			if 'Iron Heart' in self.availableDiscplines and self.ironHeartCount >= 2:
				choices.append('Dazing Strike')
				choices.append('Iron Heart Focus')
			if 'Setting Sun' in self.availableDiscplines and self.settingSunCount >= 2:
				choices.append('Mirrored Pursuit')
				choices.append('Soaring Throw')
				choices.append('Stalking Shadow')
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 2:
					choices.append('Bloodletting Strike')
				choices.append('Shadow Stride')
			if 'Stone Dragon' in self.availableDiscplines and self.stoneDragonCount >= 2:
				choices.append('Elder Mountain Hammer')
				choices.append('Mountain Avalanche')
			if 'Tiger Claw' in self.availableDiscplines and self.tigerClawCount >= 2:
				choices.append('Dancing Mongoose')
				choices.append('Pouncing Charge')
			if 'White Raven' in self.availableDiscplines and self.whiteRavenCount >= 2:
				choices.append('Flanking Maneuver')

		if highestLevel >= 4 and not choices:
			if 'Desert Wind' in self.availableDiscplines:
				if self.desertWindCount >= 2:
					choices.append('Firesnake')
					choices.append('Searing Blade')
				if self.desertWindCount >= 1:
					choices.append('Searing Charge')
			if 'Devoted Spirit' in self.availableDiscplines and self.devotedSpiritCount >= 1:
				choices.append('Divine Surge')
				choices.append('Entangling Blade')
			if 'Diamond Mind' in self.availableDiscplines and self.diamondMindCount >= 2:
				choices.append('Bounding Assault')
				choices.append('Mind Strike')
				choices.append('Ruby Nightmare Blade')
			if 'Iron Heart' in self.availableDiscplines and self.ironHeartCount >= 2:
				choices.append('Lightning Recovery')
				choices.append('Mithral Tornado')
			if 'Setting Sun' in self.availableDiscplines:
				if self.settingSunCount >= 2:
					choices.append('Strike of the Broken Shield')
				if self.settingSunCount >= 1:
					choices.append('Comet Throw')
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 2:
					choices.append('Obscuring Shadow Veil')
				choices.append('Hand of Death')
			if 'Stone Dragon' in self.availableDiscplines:
				if self.stoneDragonCount >= 2:
					choices.append('Bonesplitting Strike')
				choices.append('Boulder Roll')
				choices.append('Overwhelming Mountain Strike')
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 2:
					choices.append('Fountain of Blood')
				if self.tigerClawCount >= 1:
					choices.append('Death from Above')
			if 'White Raven' in self.availableDiscplines and self.whiteRavenCount >= 1:
				choices.append('Covering Strike')
				choices.append('White Raven Strike')

		if highestLevel >= 3 and not choices:
			if 'Desert Wind' in self.availableDiscplines:
				if self.desertWindCount >= 1:
					choices.append('Fan the Flames')
					choices.append('Zephyr Dance')
				choices.append('Death Mark')
			if 'Devoted Spirit' in self.availableDiscplines:
				if self.devotedSpiritCount >= 1:
					choices.append('Defensive Rebuke')
					choices.append('Revitalizing Strike')
			if 'Diamond Mind' in self.availableDiscplines:
				choices.append('Insightful Strike')
				choices.append('Mind Over Body')
			if 'Iron Heart' in self.availableDiscplines:
				if self.ironHeartCount >= 1:
					choices.append('Exorcism of Steel')
					choices.append('Iron Heart Surge')
			if 'Setting Sun' in self.availableDiscplines:
				if self.settingSunCount >= 1:
					choices.append('Devastating Throw')
					choices.append('Feigned Opening')
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 1:
					choices.append('Strength Draining Strike')
				choices.append('Shadow Garrote')
			if 'Stone Dragon' in self.availableDiscplines:
				if self.stoneDragonCount >= 1:
					choices.append('Stone Dragons Fury')
				choices.append('Bonecrusher')
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 2:
					choices.append('Flesh Ripper')
				if self.tigerClawCount >= 1:
					choices.append('Soaring Raptor Strike')
			if 'White Raven' in self.availableDiscplines:
				if self.whiteRavenCount >= 1:
					choices.append('Lions Roar')
					choices.append('White Raven Tactics')

		if highestLevel >= 2 and not choices:
			if 'Desert Wind' in self.availableDiscplines:
				if self.desertWindCount >= 1:
					choices.append('Fire Riposte')
					choices.append('Flashing Sun')
					choices.append('Hatchlings Flame')
				choices.append('Burning Brand')
			if 'Devoted Spirit' in self.availableDiscplines:
				choices.append('Foehammer')
				choices.append('Shield Block')
			if 'Diamond Mind' in self.availableDiscplines:
				if self.diamondMindCount >= 1:
					choices.append('Emerald Razor')
				choices.append('Action Before Thought')
			if 'Iron Heart' in self.availableDiscplines:
				choices.append('Disarming Strike')
				choices.append('Wall of Blades')
			if 'Setting Sun' in self.availableDiscplines:
				if self.settingSunCount >= 1:
					choices.append('Baffling Defense')
				choices.append('Clever Positioning')
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 1:
					choices.append('Drain Vitality')
				choices.append('Cloak of Deception')
				choices.append('Shadow Jaunt')
			if 'Stone Dragon' in self.availableDiscplines:
				choices.append('Mountain Hammer')
				choices.append('Stone Vise')
			if 'Tiger Claw' in self.availableDiscplines:
				choices.append('Claw at the Moon')
				choices.append('Rabid Wolf Strike')
			if 'White Raven' in self.availableDiscplines:
				if self.whiteRavenCount >= 1:
					choices.append('Battle Leaders Charge')
					choices.append('Tactical Strike')

		if highestLevel >= 1 and not choices:
			if 'Desert Wind' in self.availableDiscplines:
				choices.append('Blistering Flourish')
				choices.append('Burning Blade')
				choices.append('Distracting Ember')
				choices.append('Wind Stride')
			if 'Devoted Spirit' in self.availableDiscplines:
				choices.append('Crusaders Strike')
				choices.append('Vanguard Strike')
			if 'Diamond Mind' in self.availableDiscplines:
				choices.append('Moment of Perfect Mind')
				choices.append('Sapphire Nightmare Blade')
			if 'Iron Heart' in self.availableDiscplines:
				choices.append('Steel Wind')
				choices.append('Steely Strike')
			if 'Setting Sun' in self.availableDiscplines:
				choices.append('Counter Charge')
				choices.append('Mighty Throw')
			if 'Shadow Hand' in self.availableDiscplines:
				choices.append('Clinging Shadow Strike')
				choices.append('Shadow Blade Technique')
			if 'Stone Dragon' in self.availableDiscplines:
				choices.append('Charging Minotaur')
				choices.append('Stone Bones')
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 1:
					choices.append('Sudden Leap')
				choices.append('Wolf Fang Strike')
			if 'White Raven' in self.availableDiscplines:
				choices.append('Douse the Flames')
				choices.append('Leading the Attack')

		while choices:
			whichManeuver = choices[random.randint(0,len(choices)-1)]
			if whichManeuver not in self.maneuverList:
				self.maneuverList.append(whichManeuver)
				if whichManeuver in desertWind:
					self.desertWindCount += 1
				if whichManeuver in devotedSpirit:
					self.devotedSpiritCount += 1
				elif whichManeuver in diamondMind:
					self.diamondMindCount += 1
				elif whichManeuver in ironHeart:
					self.ironHeartCount += 1
				elif whichManeuver in settingSun:
					self.settingSunCount += 1
				elif whichManeuver in shadowHand:
					self.shadowHandCount += 1
				elif whichManeuver in stoneDragon:
					self.stoneDragonCount += 1
				elif whichManeuver in tigerClaw:
					self.tigerClawCount += 1
				elif whichManeuver in whiteRaven:
					self.whiteRavenCount += 1
				return whichManeuver
			else:
				choices.remove(whichManeuver)


	def learnStance(self,lvl):
		highestLevel = (lvl + 1) / 2
		
		# Stances are slightly different than regular maneuevers. Level will be less important in determining which one to choose.
		choices = []
		if highestLevel >= 8:
			if 'Desert Wind' in self.availableDiscplines:
				if self.desertWindCount >= 3:
					choices.append('Rising Phoenix')
			if 'Devoted Spirit' in self.availableDiscplines:
				if self.devotedSpiritCount >= 3:
					choices.append('Immortal Fortitude')
			if 'Diamond Mind' in self.availableDiscplines:
				if self.diamondMindCount >= 3:
					choices.append('Stance of Alacrity')
			if 'Iron Heart' in self.availableDiscplines:
				if self.ironHeartCount >= 3:
					choices.append('Supreme Blade Parry')
			if 'Setting Sun' in self.availableDiscplines:
				if self.settingSunCount >= 3:
					choices.append('Ghostly Defense')
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 3:
					choices.append('Balance on the Sky')
			if 'Stone Dragon' in self.availableDiscplines:
				if self.stoneDragonCount >= 3:
					choices.append('Strength of Stone')
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 2:
					choices.append('Wolf Pack Tactics')
			if 'White Raven' in self.availableDiscplines:
				if self.whiteRavenCount >= 1:
					choices.append('Swarm Tactics')

		if highestLevel >= 7:
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 2:
					choices.append('Prey on the Weak')

		if highestLevel >= 6:
			if 'Desert Wind' in self.availableDiscplines:
				if self.desertWindCount >= 2:
					choices.append('Fiery Assault')
			if 'Devoted Spirit' in self.availableDiscplines:
				if self.devotedSpiritCount >= 2:
					choices.append('Aura of Chaos')
					choices.append('Aura of Perfect Order')
					choices.append('Aura of Triumph')
					choices.append('Aura of Tyranny')

		if highestLevel >= 5:
			if 'Diamond Mind' in self.availableDiscplines:
				if self.diamondMindCount >= 2:
					choices.append('Hearing the Air')
			if 'Iron Heart' in self.availableDiscplines:
				if self.ironHeartCount >= 2:
					choices.append('Dancing Blade Form')
			if 'Setting Sun' in self.availableDiscplines:
				if self.settingSunCount >= 2:
					choices.append('Shifting Defense')
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 2:
					choices.append('Step of the Dancing Moth')
			if 'Stone Dragon' in self.availableDiscplines:
				if self.stoneDragonCount >= 2:
					choices.append("Giant's Stance")
			if 'White Raven' in self.availableDiscplines:
				if self.whiteRavenCount >= 2:
					choices.append('Press the Advantage')

		if highestLevel >= 3:
			if 'Desert Wind' in self.availableDiscplines:
				if self.desertWindCount >= 1:
					choices.append('Holocaust Cloak')
			if 'Devoted Spirit' in self.availableDiscplines:
				if self.devotedSpiritCount >= 1:
					choices.append('Thicket of Blades')
			if 'Diamond Mind' in self.availableDiscplines:
				if self.diamondMindCount >= 1:
					choices.append('Pearl of Black Doubt')
			if 'Iron Heart' in self.availableDiscplines:
				if self.ironHeartCount >= 1:
					choices.append('Absolute Steel Stance')
			if 'Setting Sun' in self.availableDiscplines:
				if self.settingSunCount >= 1:
					choices.append('Giant Killing Style')
			if 'Shadow Hand' in self.availableDiscplines:
				if self.shadowHandCount >= 1:
					choices.append("Assassin's Stance")
				choices.append('Dance of the Spider')
			if 'Stone Dragon' in self.availableDiscplines:
				if self.stoneDragonCount >= 1:
					choices.append('Crusing Weight of the Mountain')
				choices.append('Roots of the Mountain')
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 1:
					choices.append('Leaping Dragon Stance')
					choices.append('Wolverine Stance')
			if 'White Raven' in self.availableDiscplines:
				if self.whiteRavenCount >= 1:
					choices.append('Tactics of the Wolf')

		if highestLevel >= 1:
			if 'Desert Wind' in self.availableDiscplines:
				choices.append("Flame's Blessing")
			if 'Devoted Spirit' in self.availableDiscplines:
				choices.append("Iron Guard's Glare")
				choices.append('Martial Spirit')
			if 'Diamond Mind' in self.availableDiscplines:
				choices.append('Stance of Clarity')
			if 'Iron Heart' in self.availableDiscplines:
				choices.append('Punishing Stance')
			if 'Setting Sun' in self.availableDiscplines:
				choices.append('Step of the Wind')
			if 'Shadow Hand' in self.availableDiscplines:
				choices.append('Child of Shadow')
				choices.append('Island of Blades')
			if 'Stone Dragon' in self.availableDiscplines:
				choices.append('Stonefoot Stance')
			if 'Tiger Claw' in self.availableDiscplines:
				if self.tigerClawCount >= 1:
					choices.append('Blood in the Water')
				choices.append("Hunter's Sense")
			if 'White Raven' in self.availableDiscplines:
				choices.append('Bolstering Voice')
				choices.append('Leading the Charge')

		while choices:
			whichStance = choices[random.randint(0,len(choices)-1)]
			if whichStance not in self.stanceList:
				self.stanceList.append(whichStance)
				return whichStance
			else:
				choices.remove(whichStance)

	# function to get the character a Rogue talent
	# the parameter is the character's level
	def getRogueTalent(self,lvl):
		talentPool = ['Acrobatic Assist', 'Assault Leader', 'Befuddling Strike', 'Black Market Connections', 'Bleeding Attack', 'Bomber', 'Camouflage', 'Canny Observer', 'Card Sharp', 'Charmer', 'Coax Information', 'Combat Swipe', 'Combat Trick', 'Convincing Lie', 'Cunning Trigger', 'Deft Palm', 'Demand Attention', 'Developed Poison Immunity', 'Disease Use', 'Distracting Attack', 'Esoteric Scholar', 'Expert Leaper', 'Face in the Crowd', 'False Attacker', 'False Friend', 'Fast Fingers', 'Fast Getaway', 'Fast Picks', 'Fast Stealth', 'Finesse Rogue', 'Firearm Training', 'Follow Clues', 'Getaway Artist', 'Got Your Back', 'Green Tongue', 'Guileful Polyglot', 'Hard to Fool', 'Heads Up', 'Hold Breath', 'Honeyed Words', 'Iron Guts', 'Ki Pool', 'Last Ditch Effort', 'Lasting Poison', 'Ledge Walker', 'Nimble Climber', 'Obfuscate Story', 'Offensive Defense', 'Papercraft Tools', 'Peerless Maneuever', 'Philologist', 'Pierce the Darkness', 'Positioning Attack', 'Powerful Sneak', 'Quick Disable', 'Quick Disguise', 'Scrouge', 'Quick Trapsmith', 'Rapid Boost', 'Resiliency', 'Rogue Crawl', 'Rope Master', 'Scavenger', 'Set-Up', 'Slow Reactions', 'Snap Shot', 'Sneaky Maneuever', "Sniper's Eye", 'Stand Up', 'Stem the Flow', 'Strong Impression', 'Strong Stroke', 'Surprise Attack', 'Survivalist', 'Swift Poison', 'Swift Tracker', 'Terrain Mastery', 'Trap Spotter', 'Underhanded', 'Wall Scramble', 'Weapon Training', 'Without a Trace']
		if self.intelligence >= 10:
			talentPool.append('Minor Magic')
		if self.intelligence >= 11:
			talentPool.append('Major Magic')
		if self.intelligence >= 12:
			talentPool.append('Grig Jig')
		if self.wisdom >= 10:
			talentPool.append('Wild Magic')
		if 'Evasion' in self.specialList:
			talentPool.append('Shove Aside')
		if lvl >= 5:
			talentPool.append('Favored Terrain')
		if lvl >= 6:
			talentPool.append('Eerie Disappearance')
		if lvl >= 10:
			talentPool.extend(['Another Day', 'Confounding Blades', 'Crippling Strike', 'Deadly Cocktail', 'Deadly Sneak', 'Defensive Roll', 'Entanglement of Blades', 'Fast Tumble', 'Frugal Trapsmith', 'Feat', 'Hamstring Strike', 'Hard to Fool', 'Harrow Strike', 'Hide in Plain Sight', "Hunter's Surprise", 'Knock-Out Blow', 'Improved Evasion', 'Master of Disguise', 'Opportunist', 'Redirect Attack', 'Rumormonger', 'Skill Mastery', 'Slippery Mind', 'Stealthy Sniper', 'Thoughtful Reexamining', 'Unwitting Ally', 'Weapon Snatcher'])
			if 'Major Magic' in self.rogueTalents:
				talentPool.append('Dispelling Attack')
				talentPool.append('Familiar')
			if 'Powerful Sneak' in self.rogueTalents:
				talentPool.append('Deadly Sneak')

		while talentPool:
			whichTalent = talentPool[random.randint(0,len(talentPool)-1)]
			if whichTalent in self.rogueTalents:
				talentPool.remove(whichTalent)
			else:
				self.rogueTalents.append(whichTalent)
				return whichTalent

	# function to get the character another Fighter Bonus Feat
	# the parameter, lvl, is the level at which the feat is gained
	def getFighterFeat(self,lvl):
		featPool = ['Agile Maneuevers', 'Blind-Fight', 'Catch Off-Guard', 'Combat Reflexes', 'Defensive Combat Training', 'Improved Initiative', 'Intimidating Prowess', 'Point Blank Shot', 'Quick Draw', 'Improved Shield Bash', 'Shield Focus', 'Step Up', 'Throw Anything', 'Improved Unarmed Strike', 'Weapon Finesse', 'Weapon Focus']

		if 'Power Attack' in self.featList:
			featPool.append('Cleave')
			featPool.append('Improved Bull Rush')
			featPool.append('Improved Overrun')

		if 'Combat Expertise' in self.featList:
			featPool.append('Improved Feint')
			featPool.append('Improved Disarm')

		if 'Dodge' in self.featList:
			featPool.append('Mobility')

		if 'Improved Unarmed Strike' in self.featList:
			featPool.append('Scorpion Style')
			if self.dexterity >= 13:
				featPool.append('Improved Grapple')
				featPool.append('Deflect Arrows')

		if 'Point Blank Shot' in self.featList:
			featPool.append('Precise Shot')
			featPool.append('Far Shot')

		if 'Two-Weapon Fighting' in self.featList:
			featPool.append('Double Slice')

		if 'Weapon Focus' in self.featList:
			featPool.append('Dazzing Display')

		if lvl >= 4:
			if 'Cleave' in self.featList:
				featPool.append('Great Cleave')
			if 'Weapon Focus' in self.featList:
				featPool.append('Weapon Specialization')
			if 'Mobility' in self.featList:
				featPool.append('Spring Attack')
				if 'Point Blank Shot' in self.featList and self.dexterity >= 13:
					featPool.append('Shot on the Run')
		if lvl >= 6:
			featPool.append('Disruptive')
			featPool.append('Vital Strike')
			featPool.append('Lunge')
			if 'Improved Bull Rush' in self.featList:
				featPool.append('Greater Bull Rush')
			if 'Improved Overrun' in self.featList:
				featPool.append('Greater Overrun')
			if 'Improved Feint' in self.featList:
				featPool.append('Greater Feint')
			if 'Dazzing Display' in self.featList:
				featPool.append('Shatter Defenses')
			if 'Dodge' in self.featList:
				featPool.append('Wind Stance')
			if self.dexterity >= 17:
				if 'Two-Weapon Fighting' in self.featList:
					featPool.append('Improved Two-Weapon Fighting')
				if 'Rapid Shot' in self.featList:
					featPool.append('Manyshot')
			if 'Scorpion Style' in self.featList:
				featPool.append("Gorgon's Fist")
			if 'Improved Grapple' in self.featList:
				featPool.append('Greater Grapple')
		if lvl >= 8:
			featPool.append('Improved Critical')
			if 'Weapon Focus' in self.featList:
				featPool.append('Greater Weapon Focus')
			if 'Shield Focus' in self.featList:
				featPool.append('Greater Shield Focus')
			if 'Catch Off-Guard' or 'Throw Anything' in self.featList:
				featPool.append('Improvised Weapon Mastery')
		if lvl >= 9:
			featPool.append('Critical Focus')
		if lvl >= 10:
			if 'Disruptive' in self.featList:
				featPool.append('Spellbreaker')
		if lvl >= 11:
			featPool.append('Strike Back')
			if 'Critical Focus' in self.featList:
				featPool.append('Bleeding Critical')
				featPool.append('Sickening Critical')
			if "Gorgon's Fist" in self.featList:
				featPool.append("Medusa's Wrath")
			if 'Shield Slam' in self.featList:
				featPool.append('Shield Master')
			if 'Vital Strike' in self.featList:
				featPool.append('Improved Vital Strike')
			if 'Improved Two-Weapon Fighting' in self.featList:
				if 'Double Slice' in self.featList:
					featPool.append('Two-Weapon Rend')
				if self.dexterity >= 19:
					featPool.append('Greater Two-Weapon Fighting')
			if 'Precise Shot' in self.featList and self.dexterity >= 19:
				featPool.append('Improved Precise Shot')
			if 'Wind Stance' in self.featList and self.dexterity >= 17:
				featPool.append('Lightning Stance')
			if 'Greater Weapon Focus' and 'Shatter Defneses' in self.featList:
				featPool.append('Deadly Stroke')
		if lvl >= 12:
			if 'Weapon Focus' in self.featList:
				featPool.append('Penetrating Strike')
			if 'Weapon Specialization' in self.featList:
				featPool.append('Greater Weapon Specialization')
		if lvl >= 13:
			if 'Critical Focus' in self.featList:
				featPool.append('Crippling Critical')
				featPool.append('Deafening Critical')
				featPool.append('Staggering Critical')
				featPool.append('Tiring Critical')
		if lvl >= 15:
			if 'Critical Focus' in self.featList:
				featPool.append('Blinding Critical')
				featPool.append('Exhausting Critical')
		if lvl >= 16:
			if 'Improved Vital Strike' in self.featList:
				featPool.append('Greater Vital Strike')
			if 'Improved Precise Shot' in self.featList:
				featPool.append('Pinpoint Targeting')
			if 'Penetrating Strike' in self.featList:
				featPool.append('Greater Penetrating Strike')

		if self.strength >= 13:
			featPool.append('Power Attack')

		if self.dexterity >= 13:
			featPool.append('Deadly Aim')

		if self.dexterity >= 15:
			featPool.append('Two-Weapon Fighting')
			if 'Deflect Arrows' in self.featList:
				featPool.append('Snatch Arrows')

		if self.intelligence >= 13:
			featPool.append('Combat Expertise')

		while featPool:
			whichFeat = featPool[random.randint(0,len(featPool)-1)]
			if whichFeat not in self.featList:
				self.featList.append(whichFeat)
				return whichFeat
			else:
				featPool.remove(whichFeat)

		
	# function to get the character another Rage Power
	# lvl is the level that this particular Rage Power was earned. This way a high level character
	# won't be genrated with only level 12+ rage powers.
	# it looks at the character's level and preexisting Rage Powers to determine which 
	# one to choose next
	# returns the name of the Rage Power gained
	def getRagePower(self,lvl):

		# start with checking if the player can get a new power in a chain they're already on
		# Level 16
		if lvl >= 16:
			if 'Energy Absorption' in self.ragePowers:
				if 'Energy Eruption' not in self.ragePowers:
					self.ragePowers.append('Energy Eruption')
					return 'Energy Eruption'
			if 'Deadly Accuracy' and 'Surprise Accuracy' in self.ragePowers:
				if 'Lethal Accuracy' not in self.ragePowers:
					self.ragePowers.append('Lethal Accuracy')
					return 'Lethal Accuracy'

		# Level 12
		if lvl >= 12:
			if 'Disruptive' in self.ragePowers:
				if 'Spellbreaker' not in self.ragePowers:
					self.ragePowers.append('Spellbreaker')
					return 'Spellbreaker'
			if 'Hurling' in self.ragePowers:
				if 'Greater Hurling' not in self.ragePowers:
					self.ragePowers.append('Greater Hurling')
					return 'Greater Hurling'
			if 'Ferocious Trample' in self.ragePowers:
				if 'Greater Ferocious Trample' not in self.ragePowers:
					self.ragePowers.append('Greater Ferocious Trample')
					return 'Greater Ferocious Trample'
			if 'Elemental Rage' in self.ragePowers:
				if 'Greater Elemental Rage' not in self.ragePowers:
					self.ragePowers.append('Greater Elemental Rage')
					return 'Greater Elemental Rage'
			if 'Greater Energy Resistance' in self.ragePowers:
				if 'Energy Absorption' not in self.ragePowers:
					self.ragePowers.append('Energy Absorption')
					return 'Energy Absorption'
			if 'Celestial Totem' in self.ragePowers:
				if 'Greater Celestial Totem' not in self.ragePowers:
					self.ragePowers.append('Greater Celestial Totem')
					return 'Greater Celestial Totem'

		# Level 10
		if lvl >= 10:
			if 'Beast Totem' in self.ragePowers:
				if 'Greater Beast Totem' not in self.ragePowers:
					self.ragePowers.append('Greater Beast Totem')
					return 'Greater Beast Totem'
			if 'Chaos Totem' in self.ragePowers:
				if 'Greater Chaos Totem' not in self.ragePowers:
					self.ragePowers.append('Greater Chaos Totem')
					return 'Greater Chaos Totem'
			if 'Dragon Totem' and 'Dragon Totem Resilience' in self.ragePowers:
				if 'Dragon Totem Wings' not in self.ragePowers:
					self.ragePowers.append('Dragon Totem Wings')
					return 'Dragon Totem Wings'
			if 'Superstition' in self.ragePowers:
				if 'Eater of Magic' not in self.ragePowers:
					self.ragePowers.append('Eater of Magic')
					return 'Eater of Magic'
			if 'Fiend Totem' in self.ragePowers:
				if 'Greater Fiend Totem' not in self.ragePowers:
					self.ragePowers.append('Greater Fiend Totem')
					return 'Greater Fiend Totem'
			if 'Spirit Totem' in self.ragePowers:
				if 'Greater Spirit Totem' not in self.ragePowers:
					self.ragePowers.append('Greater Spirit Totem')
					return 'Greater Spirit Totem'

		# Level 8
		if lvl >= 8:
			if 'Powerful Blow' in self.ragePowers:
				if 'Bleeding Blow' not in self.ragePowers:
					self.ragePowers.append('Bleeding Blow')
					return 'Bleeding Blow'
			if 'Superstition' in self.ragePowers:
				if 'Disruptive' not in self.ragePowers:
					self.ragePowers.append('Disruptive')
					return 'Disruptive'
			if 'Dragon Totem' in self.ragePowers:
				if 'Dragon Totem Resilience' not in self.ragePowers:
					self.ragePowers.append('Dragon Totem Resilience')
					return 'Dragon Totem Resilience'
			if 'Lesser Elemental Rage' in self.ragePowers:
				if 'Elemental Rage' not in self.ragePowers:
					self.ragePowers.append('Elemental Rage')
					return 'Elemental Rage'
			if 'Energy Resistance' in self.ragePowers:
				if 'Greater Energy Resistance' not in self.ragePowers:
					self.ragePowers.append('Greater Energy Resistance')
					return 'Greater Energy Resistance'
			if 'Ferocious Beast' in self.ragePowers:
				if 'Greater Ferocious Beast' not in self.ragePowers:
					self.ragePowers.append('Greater Ferocious Beast')
					return 'Greater Ferocious Beast'
			if 'Ferocious Mount' in self.ragePowers:
				if 'Greater Ferocious Mount' not in self.ragePowers:
					self.ragePowers.append('Greater Ferocious Mount')
					return 'Greater Ferocious Mount'
				if 'Ferocious Trample' not in self.ragePowers:
					self.ragePowers.append('Ferocious Trample')
					return 'Ferocious Trample'
			if 'Ground Breaker' in self.ragePowers:
				if 'Greater Ground Breaker' not in self.ragePowers:
					self.ragePowers.append('Greater Ground Breaker')
					return 'Greater Ground Breaker'
			if 'Hive Totem' and 'Hive Totem Resilience' in self.ragePowers:
				if 'Hive Totem Toxicity' not in self.ragePowers:
					self.ragePowers.append('Hive Totem Toxicity')
					return 'Hive Totem Toxicity'
			if 'Lesser Hurling' in self.ragePowers:
				if 'Hurling' not in self.ragePowers:
					self.ragePowers.append('Hurling')
					return 'Hurling'
			if 'Primal Scent' in self.ragePowers:
				if 'Scent' not in self.ragePowers:
					self.ragePowers.append('Scent')
					return 'Scent'
			if 'Surprise Accuracy' in self.ragePowers:
				if 'Sharpened Accuracy' not in self.ragePowers:
					self.ragePowers.append('Sharpened Accuracy')
					return 'Sharpened Accuracy'
			if 'Spell Sunder' in self.ragePowers:
				if 'Sunder Enchantment' not in self.ragePowers:
					self.ragePowers.append('Sunder Enchantment')
					return 'Sunder Enchantment'
			if 'Intimidating Glare' in self.ragePowers:
				if 'Terrifying Howl' not in self.ragePowers:
					self.ragePowers.append('Terrifying Howl')
					return 'Terrifying Howl'

		# Level 6
		if lvl >= 6:
			if 'Intimidating Glare' in self.ragePowers:
				if 'Battle Roar' not in self.ragePowers:
					self.ragePowers.append('Battle Roar')
					return 'Battle Roar'
			if 'Lesser Beast Totem' in self.ragePowers:
				if 'Beast Totem' not in self.ragePowers:
					self.ragePowers.append('Beast Totem')
					return 'Beast Totem'
			if 'Raging Climber' in self.ragePowers:
				if 'Bestial Climber' not in self.ragePowers:
					self.ragePowers.append('Bestial Climber')
					return 'Bestial Climber'
			if 'Raging Leaper' in self.ragePowers:
				if 'Bestial Leaper' not in self.ragePowers:
					self.ragePowers.append('Bestial Leaper')
					return 'Bestial Leaper'
			if 'Raging Swimmer' in self.ragePowers:
				if 'Bestial Swimmer' not in self.ragePowers:
					self.ragePowers.append('Bestial Swimmer')
					return 'Bestial Swimmer'
			if 'Lesser Chaos Totem' in self.ragePowers:
				if 'Chaos Totem' not in self.ragePowers:
					self.ragePowers.append('Chaos Totem')
					return 'Chaos Totem'
			if 'Animal Fury' and 'Intimidating Glare' in self.ragePowers:
				if 'Dragon Totem' not in self.ragePowers:
					self.ragePowers.append('Dragon Totem')
					return 'Dragon Totem'
			if 'Lesser Fiend Totem' in self.ragePowers:
				if 'Fiend Totem' not in self.ragePowers:
					self.ragePowers.append('Fiend Totem')
					return 'Fiend Totem'
			if 'Superstition' in self.ragePowers:
				if 'Ghost Rager' not in self.ragePowers:
					self.ragePowers.append('Ghost Rager')
					return 'Ghost Rager'
			if 'Guarded Life' in self.ragePowers:
				if 'Greater Guarded Life' not in self.ragePowers:
					self.ragePowers.append('Greater Guarded Life')
					return 'Greater Guarded Life'
			if 'Hive Totem' in self.ragePowers:
				if 'Hive Totem Resilience' not in self.ragePowers:
					self.ragePowers.append('Hive Totem Resilience')
					return 'Hive Totem Resilience'
			if 'Lesser Hurling' in self.ragePowers:
				if 'Hurling Charge' not in self.ragePowers:
					self.ragePowers.append('Hurling Charge')
					return 'Hurling Charge'
			if 'Overbearing Advance' in self.ragePowers:
				if 'Overbearing Onslaught' not in self.ragePowers:
					self.ragePowers.append('Overbearing Onslaught')
					return 'Overbearing Onslaught'
			if 'Raging Leaper' in self.ragePowers:
				if 'Raging Flier' not in self.ragePowers:
					self.ragePowers.append('Raging Flier')
					return 'Raging Flier'
			if 'Rolling Dodge' in self.ragePowers:
				if 'Reflexive Dodge' not in self.ragePowers:
					self.ragePowers.append('Reflexive Dodge')
					return 'Reflexive Dodge'
			if 'Renewed Vigor' in self.ragePowers:
				if 'Regenerative Vigor' not in self.ragePowers:
					self.ragePowers.append('Regenerative Vigor')
					return 'Regenerative Vigor'
			if 'Renewed Vitality' in self.ragePowers:
				if 'Renewed Life' not in self.ragePowers:
					self.ragePowers.append('Renewed Life')
					return 'Renewed Life'
			if 'Witch Hunter' in self.ragePowers:
				if 'Spell Sunder' not in self.ragePowers:
					self.ragePowers.append('Spell Sunder')
					return 'Spell Sunder'
			if 'Ferocious Mount' in self.ragePowers:
				if 'Spirit Steed' not in self.ragePowers:
					self.ragePowers.append('Spirit Steed')
					return 'Spirit Steed'
			if 'Lesser Spirt Totem' in self.ragePowers:
				if 'Spirit Totem' not in self.ragePowers:
					self.ragePowers.append('Spirit Totem')
					return 'Spirit Totem'
			if 'Moment of Clarity' and 'Perfect Clarity' in self.ragePowers:
				if 'Ultimate Clarity' not in self.ragePowers:
					self.ragePowers.append('Ultimate Clarity')
					return 'Ultimate Clarity'
			if 'World Serpent Totem' in self.ragePowers:
				if 'World Serpent Spirit' not in self.ragePowers:
					self.ragePowers.append('World Serpent Spirit')
					return 'World Serpent Spirit'
			if 'World Serpent Spirit' and 'World Serpent Totem' in self.ragePowers:
				if 'World Serpent Totem Unity' not in self.ragePowers:
					self.ragePowers.append('World Serpent Totem Unity')
					return 'World Serpent Totem Unity'

		# Level 4
		if lvl >= 4:
			if 'Surprise Accuracy' in self.ragePowers:
				if 'Deadly Accuracy' not in self.ragePowers:
					self.ragePowers.append('Deadly Accuracy')
					return 'Deadly Accuracy'
			if 'Animal Fury' in self.ragePowers:
				if 'Hive Totem' not in self.ragePowers:
					self.ragePowers.append('Hive Totem')
					return 'Hive Totem'
				if 'Penetrating Bite' not in self.ragePowers:
					self.ragePowers.append('Penetrating Bite')
					return 'Penetrating Bite'
			if 'Swift Foot' in self.ragePowers:
				if 'Sprint' not in self.ragePowers:
					self.ragePowers.append('Sprint')
					return 'Sprint'

		# Here we check for Rage Powers that require another Rage Power but have no level requirement
		if 'Brawler' in self.ragePowers:
			newPower = 'Greater Brawler'
			if newPower not in self.ragePowers:
				self.ragePowers.append(newPower)
				return newPower
		if 'Smasher' in self.ragePowers:
			newPower = 'Gearbreaker'
			if newPower not in self.ragePowers:
				self.ragePowers.append(newPower)
				return newPower
		if 'Animal Fury' in self.ragePowers:
			newPower = 'Greater Animal Fury'
			if newPower not in self.ragePowers:
				self.ragePowers.append(newPower)
				return newPower
		if 'Reckless Abandon' in self.ragePowers:
			newPower = 'Inspire Ferocity'
			if newPower not in self.ragePowers:
				self.ragePowers.append(newPower)
				return newPower
		if 'Low-Light Vision' in self.ragePowers or 'Low-Light Vision' in self.specialList:
			newPower = 'Night Vision'
			if newPower not in self.ragePowers:
				self.ragePowers.append(newPower)
				return newPower
		if 'Moment of Clarity' in self.ragePowers:
			newPower = 'Perfect Clarity'
			if newPower not in self.ragePowers:
				self.ragePowers.append(newPower)
				return newPower
		if 'Animal Fury' in self.ragePowers:
			newPower = 'Savage Jaw'
			if newPower not in self.ragePowers:
				self.ragePowers.append(newPower)
				return newPower
		if 'Superstition' in self.ragePowers:
			newPower = 'Witch Hunter'
			if newPower not in self.ragePowers:
				self.ragePowers.append(newPower)
				return newPower


		# If the character isn't on a Rage Power Chain yet we randomly choose a power for them based solely on their level. Highest available levels first
		# Level 12
		if lvl >= 12:
			choices = ["Boar's Charge", 'Come and Get Me', 'Deathless Frenzy', 'Fearless Rage', 'Mighty Swing']
			while choices:
				whichPower = choices[random.randint(0,len(choices)-1)]
				if whichPower not in self.ragePowers:
					self.ragePowers.append(whichPower)
					return whichPower
				else:
					choices.remove(whichPower)

		# Level 10
		if lvl >= 10:
			choices = ['Body Bludgeon', 'Flesh Wound']
			while choices:
				whichPower = choices[random.randint(0,len(choices)-1)]
				if whichPower not in self.ragePowers:
					self.ragePowers.append(whichPower)
					return whichPower
				else:
					choices.remove(whichPower)
				
		# Level 8
		if lvl >= 8:
			choices = ['Celestial Totem', 'Clear Mind', 'Fierce Fortitude', 'Increased Damage Reduction', 'Internal Fortitude', 'Tor Linnorm Death Curse', 'Unexpected Strike']
			while choices:
				whichPower = choices[random.randint(0,len(choices)-1)]
				if whichPower not in self.ragePowers:
					self.ragePowers.append(whichPower)
					return whichPower
				else:
					choices.remove(whichPower)

		# Level 6
		if lvl >= 6:
			choices = ['Boasting Taunt', 'Fueled by Vengeance', 'Ground Breaker', 'Savage Dirty Trick']
			while choices:
				whichPower = choices[random.randint(0,len(choices)-1)]
				if whichPower not in self.ragePowers:
					self.ragePowers.append(whichPower)
					return whichPower
				else:
					choices.remove(whichPower)

		# Level 4
		if lvl >= 4:
			choices = ['Lesser Elemental Rage', 'Impelling Disarm', 'Cairn Linnorm Death Curse', 'Crag Linnorm Death Curse', 'Fjord Linnorm Death Curse', 'Ice Linnorm Death Curse', 'Taiga Linnorm Death Curse', 'Renewed Vigor']
			while choices:
				whichPower = choices[random.randint(0,len(choices)-1)]
				if whichPower not in self.ragePowers:
					self.ragePowers.append(whichPower)
					return whichPower
				else:
					choices.remove(whichPower)

		# Level 2
		# This is the last stop. These are Rage Powers with absolutely no prerequisites
		choices = ['Animal Fury', 'Armor Ripper', 'Auspicious Mark', 'Lesser Beast Totem', 'Brawler', 'Breathtaker', 'Lesser Celestial Totem', 'Lesser Chaos Totem', 'Energy Resistance', 'Ferocious Beast', 'Ferocious Mount', 'Lesser Fiend Totem', 'Good For What Ails You', 'Guarded Life', 'Lesser Hurling', 'Intimidating Glare', 'Knockback', 'Knockdown', 'Liquid Courage', 'Low-Light Vision', 'Moment of Clarity', 'No Escape', 'Overbearing Advance', 'Powerful Blow', 'Quick Reflexes', 'Raging Climber', 'Raging Grappler', 'Raging Leaper', 'Raging Swimmer', 'Reckless Abandon', 'Roaring Drunk', 'Rolling Dodge', 'Roused Anger', 'Savage Intuition', 'Lesser Spirit Totem', 'Staggering Drunk', 'Strength Surge', 'Superstition', 'Surprise Accuracy', 'Swift Foot', 'Water Sense', 'World Serpent Totem']
		while choices:
			whichPower = choices[random.randint(0,len(choices)-1)]
			if whichPower not in self.ragePowers:
				self.ragePowers.append(whichPower)
				return whichPower
			else:
				choices.remove(whichPower)

	# function to get the character some equipment fit for a PC
	def getEquipment(self):
		# ARMOR
		magicArmorBonus = int(self.level / 4)
		if 'Unarmored' in self.tags:
			if magicArmorBonus > 0:
				self.equipment['Armor'] = 'Bracers of Armor +{}'.format(magicArmorBonus)
				self.armorClass += magicArmorBonus
				self.flatFootedArmorClass += magicArmorBonus
		if 'Light Armor' in self.tags:
			self.equipment['Armor'] = '+{} Studded Leather Armor'.format(magicArmorBonus)
			self.armorClass += magicArmorBonus + 3
			self.flatFootedArmorClass += magicArmorBonus + 3
		if 'Medium Armor' in self.tags:
			self.equipment['Armor'] = '+{} Breastplate'.format(magicArmorBonus)
			self.armorClass += magicArmorBonus + 5
			self.flatFootedArmorClass += magicArmorBonus + 5
		if 'Heavy Armor' in self.tags:
			self.equipment['Armor'] = '+{} Full Plate Armor'.format(magicArmorBonus)
			self.armorClass += magicArmorBonus + 8
			self.flatFootedArmorClass += magicArmorBonus + 8
		if 'Druid Armor' in self.tags:
			self.equipment['Armor'] = '+{} Hide Armor'.format(magicArmorBonus)
			self.armorClass += magicArmorBonus + 3
			self.flatFootedArmorClass += magicArmorBonus + 3

		# WEAPON
		magicWeaponBonus = int(self.level / 3)

		# fighters have that Weapon Training thing so let's make sure the fighter gets the right weapon
		if self.clas == 'Fighter':
			weaponTrainingBonus = int((self.level - 1) / 4)
			if 'Weapon Training +{} (Axes)'.format(weaponTrainingBonus) in self.specialList:
				if 'Big Weapon' in self.tags:
					self.equipment['Main Hand'] = '+{} Greataxe'.format(magicWeaponBonus)
				elif 'Two Weapons' in self.tags:
					self.equipment['Main Hand'] = '+{} Handaxe'.format(magicWeaponBonus)
					self.equipment['Off Hand'] = '+{} Handaxe'.format(magicWeaponBonus)
				elif 'Shield' in self.tags:
					self.equipment['Main Hand'] = '+{} Battleaxe'.format(magicWeaponBonus)
					self.equipment['Off Hand'] = '+{} Spiked Iron Light Shield'.format(magicWeaponBonus)
					self.armorClass += magicArmorBonus + 2
					self.touchArmorClass += magicArmorBonus + 2
				else:
					self.equipment['Main Hand'] = '+{} Waraxe'.format(magicWeaponBonus)
			elif 'Weapon Training +{} (Heavy Blades)'.format(weaponTrainingBonus) in self.specialList:
				if 'Big Weapon' in self.tags:
					self.equipment['Main Hand'] = '+{} Greatsword'.format(magicWeaponBonus)
				elif 'Shield' in self.tags:
					self.equipment['Main Hand'] = '+{} Longsword'.format(magicWeaponBonus)
					self.equipment['Off Hand'] = '+{} Spiked Iron Light Shield'.format(magicWeaponBonus)
					self.armorClass += magicArmorBonus + 2
					self.touchArmorClass += magicArmorBonus + 2
				else:
					self.equipment['Main Hand'] = '+{} Katana'.format(magicWeaponBonus)
			elif 'Weapon Training +{} (Light Blades)'.format(weaponTrainingBonus) in self.specialList:
				if 'Two Weapons' in self.tags:
					choices = ['Dagger', 'Shortsword', 'Kukri']
					self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
					self.equipment['Off Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
				else:
					self.equipment['Main Hand'] = '+{} Rapier'.format(magicWeaponBonus)
			elif 'Weapon Training +{} (Bows)'.format(weaponTrainingBonus) in self.specialList:
				choices = ['Composite Shortbow', 'Composite Longbow']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Weapon Training +{} (Close)'.format(weaponTrainingBonus) in self.specialList:
				choices = ['Cestus', 'Punching Dagger']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
				self.equipment['Off Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Weapon Training +{} (Crossbows)'.format(weaponTrainingBonus) in self.specialList:
				if 'Two Weapons' in self.tags:
					self.equipment['Main Hand'] = '+{} Hand Crossbow'.format(magicWeaponBonus)
					self.equipment['Off Hand'] = '+{} Hand Crossbow'.format(magicWeaponBonus)
				else:
					choices = ['Double Crossbow', 'Heavy Repeating Crossbow']
					self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Weapon Training +{} (Double)'.format(weaponTrainingBonus) in self.specialList:
				choices = ['Dire Flail', 'Kusarigama', 'Two-Bladed Sword']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Weapon Training +{} (Firearms)'.format(weaponTrainingBonus) in self.specialList:
				if 'Two Weapons' in self.tags:
					self.equipment['Main Hand'] = '+{} Pistol'.format(magicWeaponBonus)
					self.equipment['Off Hand'] = '+{} Pistol'.format(magicWeaponBonus)
				else:
					choices = ['Blunderbuss', 'Musket']
					self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Weapon Training +{} (Hammers)'.format(weaponTrainingBonus) in self.specialList:
				if 'Two Weapons' in self.tags:
					self.equipment['Main Hand'] = '+{} Light Hammer'.format(magicWeaponBonus)
					self.equipment['Off Hand'] = '+{} Light Hammer'.format(magicWeaponBonus)
				elif 'Shield' in self.tags:
					self.equipment['Main Hand'] = '+{} Warhammer'.format(magicWeaponBonus)
					self.equipment['Off Hand'] = '+{} Spiked Iron Light Shield'.format(magicWeaponBonus)
					self.armorClass += magicArmorBonus + 2
					self.touchArmorClass += magicArmorBonus + 2
				else:
					self.equipment['Main Hand'] = '+{} Greathammer'.format(magicWeaponBonus)
			elif 'Weapon Training +{} (Monk)'.format(weaponTrainingBonus) in self.specialList:
				choices = ['Bo Staff', 'Kusarigama', 'Cestus', 'Nunchaku']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Weapon Training +{} (Polearms)'.format(weaponTrainingBonus) in self.specialList:
				choices = ['Guisarme', 'Halberd']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Weapon Training +{} (Spears)'.format(weaponTrainingBonus) in self.specialList:
				choices = ['Javelins', 'Harpoon', 'Lance', 'Spear']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Weapon Training +{} (Thrown)'.format(weaponTrainingBonus) in self.specialList:
				choices = ['Dagger', 'Harpoon', 'Sling', 'Shurikens']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			
		elif 'Melee' in self.tags:
			if 'Two Weapons' in self.tags:
				choices = ['Shortsword', 'Handaxe', 'Light Hammer', 'Kukri', 'Dagger']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
				self.equipment['Off Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Big Weapon' in self.tags:
				choices = ['Greatsword', 'Greataxe', 'Greathammer']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			elif 'Shield' in self.tags:
				choices = ['Longsword', 'Battleaxe', 'Warhammer']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
				self.equipment['Off Hand'] = '+{} Spiked Iron Light Shield'.format(magicWeaponBonus)
				self.armorClass += magicArmorBonus + 2
				self.touchArmorClass += magicArmorBonus + 2
			elif 'Sneaky' in self.tags:
				choices = ['Dagger', 'Katana', 'Throwing Knives']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
			else:
				choices = ['Dagger', 'Rapier', 'Falchion', 'Lance', 'Scythe', 'Halberd']
				self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
		elif 'Ranged Attacker' in self.tags:
			choices = ['Composite Longbow', 'Throwing Knives', 'Heavy Repeating Crossbow', 'Composite Shortbow', 'Sling']
			self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))
		else:
			choices = ['Dagger', 'Blunderbuss']
			self.equipment['Main Hand'] = '+{} {}'.format(magicWeaponBonus, random.choice(choices))

		print 'Equipment Found!'
		print self.equipment



	# function to do anything at the last minute
	def finalCheck(self):
		# check if Touch or Flat-footed exceeds the character's normal AC
		if self.flatFootedArmorClass > self.armorClass:
			self.flatFootedArmorClass = self.armorClass
		if self.touchArmorClass > self.armorClass:
			self.touchArmorClass = self.armorClass



	# function to make an attack and damage roll using one of the character's weapons
	# required parameters are the character's effective BAB on this attack and which ability score modifier to use
	# by default this rolls for the main hand weapon
	# if using a two-handed weapon just specify twoHanded = True when calling this
	# returns a list containing two elements, the first is the resulting attack roll and the second is the total damage
	def rollAttack(self,bab,abiMod,equipmentSlot = 'Main Hand',twoHanded = False):
		parsedWeapon = self.equipment[equipmentSlot][3:]
		weaponBonus = int(self.equipment[equipmentSlot][1])
		weaponDamage = weapons[parsedWeapon][0]
		numOfDice = int(weaponDamage[0])
		dieSize = int(weaponDamage[2:])
		naturalRoll = random.randint(1,20)
		attackRoll = naturalRoll + bab + abiMod + weaponBonus
		damage = 0
		for i in xrange(numOfDice):
			damageNaturalRoll = random.randint(1,dieSize)
			damage += damageNaturalRoll
		damage += abiMod + weaponBonus
		if twoHanded: # if using a two-handed weapon one's strength bonus on damage is multiplied by 1.5
			damage += int(abiMod / 2) # so here we just add another half if the attack is two-handed.
		if naturalRoll >= weapons[parsedWeapon][1]:
			print 'FUCKING CRITICAL!!'
			damage = damage * weapons[parsedWeapon][2]
		print 'Attack Roll: {}		Damage: {}'.format(attackRoll, damage)
		return [attackRoll, damage]

	def fullAttack(self,abiMod,twoHanded = False):
		if self.BAB >= 16:
			numOfAttacks = 4
		elif self.BAB >= 11:
			numOfAttacks = 3
		elif self.BAB >= 6:
			numOfAttacks = 2
		else:
			numOfAttacks = 1
		for i in xrange(numOfAttacks):
			self.rollAttack(self.BAB - (i*5), abiMod)


	def writeCharacterToFile(self, fileName):
		outFile = open(fileName, "w")

		outFile.write('{}\n'.format(self.name))
		outFile.write('Level {} {} {}\n'.format(self.level, self.race, self.clas))
		outFile.write('HP: {}\n'.format(self.hitPoints))
		outFile.write('Ability Scores\n')
		outFile.write('Str {} ({})\n'.format(self.strength, self.strMod))
		outFile.write('Dex {} ({})\n'.format(self.dexterity, self.dexMod))
		outFile.write('Con {} ({})\n'.format(self.constitution, self.conMod))
		outFile.write('Int {} ({})\n'.format(self.intelligence, self.intMod))
		outFile.write('Wis {} ({})\n'.format(self.wisdom, self.wisMod))
		outFile.write('Cha {} ({})\n'.format(self.charisma, self.chaMod))
		outFile.write('\n')
		outFile.write('Armor Class {}	(Touch {} / Flat-Footed {})\n'.format(self.armorClass, self.touchArmorClass, self.flatFootedArmorClass))
		outFile.write('Fort +{}\n'.format(self.fortSave))
		outFile.write('Ref +{}\n'.format(self.refSave))
		outFile.write('Will +{}\n'.format(self.willSave))
		outFile.write('BAB +{}\n'.format(self.BAB))


		# this is where im going to have to write the character's basic attack form
		# Need a single attack, and full attack displayed
		# but only if the character has the appropriate tags: Melee or Ranged Attacker
		if 'Melee' in self.tags or 'Ranged Attacker' in self.tags:
			parsedWeapon = self.equipment['Main Hand'][3:]
			weaponBonus = int(self.equipment['Main Hand'][1])
			weaponDamage = weapons[parsedWeapon][0]
			numOfDice = int(weaponDamage[0])
			dieSize = int(weaponDamage[2:])
			attackBonus = weaponBonus + self.BAB
			damageBonus = self.strMod + weaponBonus
			if 'Weapon Finesse' in self.featList or 'Ranged Attacker' in self.tags:
				attackBonus += self.dexMod
			else:
				attackBonus += self.strMod
			if 'Weapon Focus' in self.featList:
				attackBonus += 1
			if 'Weapon Specialization' in self.featList:
				damageBonus += 2
			if 'Big Weapon' in self.tags: # 2 handed
				damageBonus += int(0.5 * self.strMod)
			outFile.write('Basic Attack: {} +{} ATK {}d{}+{} {}-20/x{}\n'.format(parsedWeapon, attackBonus, numOfDice, dieSize, damageBonus, weapons[parsedWeapon][1], weapons[parsedWeapon][2]))

		outFile.write('\n')

		if self.clas == 'Barbarian':
			 outFile.write('Rage Powers: \n')
			 for i in xrange(len(self.ragePowers)):
			 	outFile.write('{}\n'.format(self.ragePowers[i]))
		if self.clas == 'Ranger':
			outFile.write('Favored Terrains: {}\n'.format(self.favoredTerrains))
			outFile.write('Favored Enemies: {}\n'.format(self.favoredEnemies))
		if self.clas == 'Rogue':
			outFile.write('Rogue Talents: \n')
			for i in xrange(len(self.rogueTalents)):
				outFile.write('{}\n'.format(self.rogueTalents[i]))
		if 'Martial Adept' in self.tags:
			outFile.write('NumOf Maneuvers Readied: {}\n'.format(self.maneuversReadied))
			outFile.write('Maneuvers Known: \n')
			for i in xrange(len(self.maneuverList)):
				outFile.write('{}\n'.format(self.maneuverList[i]))
			outFile.write('ENDMANEUVERSKNOWN\n')
			outFile.write('Stances Known: \n')
			for i in xrange(len(self.stanceList)):
				outFile.write('{}\n'.format(self.stanceList[i]))
			outFile.write('ENDSTANCES\n')
		if 'Psionic' in self.tags:
			outFile.write('Power Points: {}\n'.format(self.powerPoints))
			outFile.write('Powers Known: \n')
			for i in xrange(len(self.powerList)):
				outFile.write('{}\n'.format(self.powerList[i]))
		if 'Spellcaster' in self.tags:
			outFile.write('Spells per Day: {}\n'.format(self.spellsPerDay))
			if 'Spontaneous' in self.tags:
				outFile.write('Spells Known: \n')
				for i in xrange(len(self.spellList)):
					outFile.write('{}\n'.format(self.spellList[i]))
			if 'Prepared' in self.tags:
				outFile.write('Spells Prepared: \n')
				for i in xrange(len(self.spellsPrepared)):
					outFile.write('{}\n'.format(self.spellsPrepared[i]))
		outFile.write('\n')
		sortedSkills = sorted(self.skillBonus.items(), key=operator.itemgetter(1))
		sortedSkills.reverse()
		outFile.write('Skills: \n')
		for i in sortedSkills:
			outFile.write('{}: {}\n'.format(i[0], i[1]))
		outFile.write('ENDSKILLS\n')
		outFile.write('\n')
		outFile.write('Special: \n')
		for i in xrange(len(self.specialList)):
			outFile.write('{}\n'.format(self.specialList[i]))
		outFile.write('ENDSPECIAL\n')
		outFile.write('\n')
		outFile.write('Feats: \n')
		for i in xrange(len(self.featList)):
			outFile.write('{}\n'.format(self.featList[i]))
		outFile.write('ENDFEATS\n')
		outFile.write('\n')
		outFile.write('Equipment: {}\n'.format(self.equipment))
		outFile.write('\n')
		outFile.write('Languages: {}\n'.format(self.languagesKnown))
		outFile.write('\n')
		outFile.write('Tags: {}\n'.format(self.tags))

		outFile.close()




	def printCharacter(self):
		print '{} is a Level {} {} {}'.format(self.name, self.level, self.race, self.clas)
		print 'HP: {}'.format(self.hitPoints)
		self.printAbilityScores()
		print 'Armor Class: {}'.format(self.armorClass)
		print 'Touch AC: {}		Flat-Footed AC: {}'.format(self.touchArmorClass, self.flatFootedArmorClass)
		if self.clas == 'Crusader':
			print 'Maneuevers Known: {}'.format(self.maneuverList)
			print 'Stances Known: {}'.format(self.stanceList)
		if self.clas == 'Swordsage':
			print 'Maneuevers Known: {}'.format(self.maneuverList)
			print 'Stances Known: {}'.format(self.stanceList)
		if self.clas == 'Warblade':
			print 'Maneuevers Known: {}'.format(self.maneuverList)
			print 'Stances Known: {}'.format(self.stanceList)
		if self.clas == 'Barbarian':
			print 'Rage Powers: {}'.format(self.ragePowers)
		if self.clas == 'Rogue':
			print 'Rogue Talents: {}'.format(self.rogueTalents)
		if self.clas == 'Ardent':
			print 'Power Points: {}'.format(self.powerPoints)
			print 'Powers Known: {}'.format(self.powerList)
			print 'Mantles: {}'.format(self.mantleList)
		if self.clas == 'Psion':
			print 'Power Points: {}'.format(self.powerPoints)
			print 'Powers Known: {}'.format(self.powerList)
		if self.clas == 'Wilder':
			print 'Power Points: {}'.format(self.powerPoints)
			print 'Powers Known: {}'.format(self.powerList)
		if self.clas == 'Bard':
			print 'Spells Per Day: {}'.format(self.spellsPerDay)
			for i in xrange(7):
				if self.spellsKnown[i] != 0:
					print 'Level {} Spells Known: {}'.format(i, self.spellList[i])
		if self.clas == 'Beguiler':
			print 'Spells Per Day: {}'.format(self.spellsPerDay)
			for i in xrange(len(self.spellList)):
				print 'Level {} Spells Known: {}'.format(i, self.spellList[i])
		if self.clas == 'Dread Necromancer':
			print 'Spells Per Day: {}'.format(self.spellsPerDay)
			for i in xrange(len(self.spellList)):
					print 'Level {} Spells Known: {}'.format(i+1, self.spellList[i])
		if self.clas == 'Paladin':
			print 'Spells Per Day: {}'.format(self.spellsPerDay)
			for i in xrange(len(self.spellsPerDay)):
				if self.spellsPerDay[i] != 0:
					print 'Level {} Spells Prepared: {}'.format(i+1, self.spellsPrepared[i])
		if self.clas == 'Warmage':
			print 'Spells Per Day: {}'.format(self.spellsPerDay)
			for i in xrange(len(self.spellList)):
					print 'Level {} Spells Known: {}'.format(i, self.spellList[i])
		if self.clas == 'Druid':
			print 'Spells Per Day: {}'.format(self.spellsPerDay)
			for i in xrange(len(self.spellsPrepared)):
				print 'Level {} Spells Prepared: {}'.format(i, self.spellsPrepared[i])
		if self.clas == 'Ranger':
			print 'Favored Enemies: {}'.format(self.favoredEnemies)
			print 'Favored Terrains: {}'.format(self.favoredTerrains)
			print 'Spells Per Day: {}'.format(self.spellsPerDay)
			for i in xrange(len(self.spellsPrepared)):
				print 'Level {} Spells Prepared: {}'.format(i+1, self.spellsPrepared[i])
		print 'Fortitude: +{}'.format(self.fortSave)
		print 'Reflex: +{}'.format(self.refSave)
		print 'Will: +{}'.format(self.willSave)
		print 'BAB: +{}'.format(self.BAB)
		print 'Special: {}'.format(self.specialList)
		print 'Feats: {}'.format(self.featList)
		self.printSkills()
		print 'Equipment: {}'.format(self.equipment)
		print 'Languages Known: {}'.format(self.languagesKnown)
		print 'Tags: {}'.format(self.tags)

	# function to print te character's skills. 
	# the user may specify how many skills to print, by default this value is 10
	# skills are sorted by bonus in descending order. 
	def printSkills(self,numOfSkillsToPrint = 10):
		sortedSkills = sorted(self.skillBonus.items(), key=operator.itemgetter(1))
		sortedSkills.reverse()
		sortedSkills = sortedSkills[:numOfSkillsToPrint]
		for i in sortedSkills:
			print '{}: {}'.format(i[0], i[1])

	# generateCharacter totally procedurally generates a character, from rolling its stats, to choosing class and race
	def generateCharacter(self):
		print 'Assigning ability scores...'
		self.assignAbilityScores(self.rollStats())
		print 'Ability scores assigned!'
		print 'Assigning race...'
		self.assignRace()
		print 'Race assigned! - {}'.format(self.race)
		print 'Calculating armor class...'
		self.calcArmorClass()
		print 'Armor Class calculated: {}'.format(self.armorClass)
		print 'Choosing class...'
		self.chooseClass()
		print 'Class chosen! - {}'.format(self.clas)
		self.getClassFeatures()
		self.getFeats()
		self.getEquipment()

	# buildAClass builds a character of a chosen class
	def buildACharacterOfClass(self,chosenClass):
		print 'Setting class as {}...'.format(chosenClass)
		self.setClass(chosenClass)
		print 'Class set as {}!'.format(chosenClass)
		self.assignAbilityScoresByClass(self.rollStats())
		self.assignRace()
		self.calcArmorClass()
		self.getClassFeatures()
		self.getFeats()
		self.getEquipment()
		self.finalCheck()

	def buildACharacter(self,chosenRace,chosenClass):
		self.setClass(chosenClass)
		self.assignAbilityScoresByClass(self.rollStats())
		self.race = chosenRace
		self.getRacialTraits()
		self.calcArmorClass()
		self.getClassFeatures()
		self.getFeats()
		self.getEquipment()
		self.finalCheck()


# rangerMan = Character('Ranger-Man', 20)
# rangerMan.buildACharacterOfClass('Ranger')
# rangerMan.writeCharacterToFile('rangerMan.txt')


# print 'Beginning generation of gang of kobolds...'
# koboldNames = ['Yikyik', 'Yapyap', 'Jibjib', 'Bruce', 'Olp', 'Jamada', 'Makroo', 'Zornesk']
# for i in xrange(4):
# 	kobold = Character(random.choice(koboldNames), random.randint(2,4))
# 	print 'Initialized Kobold #{} - {}!'.format(i+1, kobold.name)
# 	kobold.buildACharacter('Kobold', random.choice(['Barbarian', 'Rogue', 'Ranger', 'Druid', 'Wilder']))
# 	print '{} built!'.format(kobold.name)
# 	kobold.writeCharacterToFile('{}.txt'.format(kobold.name))
# 	print '{}.txt created!'.format(kobold.name)
