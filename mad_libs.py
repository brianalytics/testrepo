#Mad Libs Program

#Words resquested from user
adjective1 = input('Enter an adjective: ')
game = input('Enter the name of an outdoor game: ')
adjective2 = input('Enter another adjective: ')
friend = input('Enter the name of a friend: ')
verb = input('Enter a verb ending in ing: ')
adjective3 = input('Enter one more adjective: ')

#Words requested from user-formatted
ajective1 = input('Enter an adjective: ').lower()
game = input('Enter the name of an outdoor game: ').lower()
adjective2 = input('Enter another adjective: ').lower()
friend = input('Enter the name of a friend: ').capitalize()
verb = input('Enter a verb ending in ing: ').lower()
adjective3 = input('Enter one more adjective: ')

#Test run
print(adjective1, game, adjective2, friend, verb, adjective3)

#Story template
story = 'It was a ADJECTIVE1 summer day at the beach. My friends and I were in the water playing GAME. As a ADJECTIVE2 wave came closer, my friend NAMEOFFRIEND yelled, "Look! There\'s a jellyfish VERB-ING!"As we got closer, we saw that the jellyfish was indeed VERB-ING! NAMEOFFRIEND ran out of the water and onto the sand. NAMEOFFRIEND was afraid of VERB-ING jellyfish. The rest of us stayed in the water playing GAME because VERB-ING jellyfish are ADJECTIVE3.As '

#Story template formatted
story = (f'It was a {adjective1} summer day at the beach. My friends and I were in the water playing {game}. As a {adjective2} wave came closer, my friend {friend} yelled, "Look! There\'s a jellyfish {verb}!" As we got closer, we saw that the jellyfish was indeed {verb}! {friend} ran out of the water and onto the sand. {friend} was afraid of {verb} jellyfish. The rest of us stayed in the water playing {game} because {verb} jellyfish are {adjective3}.')

print(story)
