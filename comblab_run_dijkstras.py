# ENGSCI233: Lab - Combinatorics
# comblab_run_dijkstras.py 

# PREPARATION:
# Complete the activities in comblab_practice.py.

# SUBMISSION:
# - YOU MUST submit this file to complete the lab. 
# - DO NOT change the file name.


# EXERCISE: Dijkstra's shortest path algorithm.
# For this task, you will develop an implementation of the Dijkstra's shortest path algorithm.


# TO DO:
# - In comblab_functions.py, COMPLETE the function DIJKSTRA.
# - Your function must have three input arguments (in order):
#   ~ A network object.
#   ~ The NAME of a source node.
#   ~ The NAME of a destination node.
# - The function must have two outputs (in order):
#   ~ The shortest DISTANCE between source and destination.
#   ~ The shortest PATH between source and destination, a LIST of node NAMES. 
# - How do I know its CORRECT? Test your implementation by PASSING the ASSERT commands below.
# - You DO NOT need to modify any of the commands below.

from comblab_functions import*

# CREATE a simple network to test your algorithm
	# create network object
test = Network()
	# read in and set up the test network
test.read_network(filename='test_network.txt')
	
# RUN your shortest path algorithm
distance, shortest_path = dijkstra(network=test, source_name='A', destination_name='F')

# check that it PASSES the asserts below
	# correct path length
assert(distance == 7)
	# correct path
assert(all([p1==p2 for p1,p2 in zip(shortest_path, ['A','B','C','E','F'])]))


# -------------------------------------------------------------------------------#

# EXERCISE: Pacific Peoples Migration 
# By 1300 AD, Maori had settled in New Zealand: but where did they originate from? Archaelogical evidence
# and language suggest that Maori are descended from people of the Eastern Polynesian islands: the Society
# Islands, Cook Islands and French Polynesia. They were capable seafarers, traveling in sophisticated Waka
# ama (outrigger canoes), using weather systems and stars for navigation, and carrying plants and animals to
# cultivate new settlements. 

# We shall consider a modern day restaging of the great Pacific migration, in which participants have
# access to modern sailing vessels. In keeping with their desire to explore, discover and settle new
# lands, we shall restrict the individual sailing legs to discrete "hops" (arcs) between adjacent islands
# (nodes). Instead of assigning each hop a distance, we shall instead imagine a travel time, which
# incorporates both distance as well as difficulty of travel (given currents and weather).

# For this task, you will use your shortest path algorithm to plan a migratory route for modern Pacific
# voyagers through Micronesia and eventually arriving in New Zealand. Of course, the early Pacific people
# did not have access to satellite mapping or Dijkstra's algorithm (that we know of)... and yet they still
# managed to settle some of the most remote islands in the Pacific. 

# TO DO:
# - Inspect the Waka ama voyage map, linked on the Canvas Module page and the lab document.
# - Determine the shortest path that modern-day explorers should take to travel from Taiwan to Hokianga.
# - Which pair of locations in the network are the furthest apart? Describe how you arrived at this answer.
# - WRITE your answers to the questions above in the file 'comblab_questions.txt'.

# set up pacific network
pacific = Network()
# read in and set up the test network
pacific.read_network(filename='Waka.txt')
	
# RUN your shortest path algorithm
distance, shortest_path = dijkstra(network=pacific, source_name='Taiwan', destination_name='Hokianga')
print(distance, shortest_path)

# set up dictionary and list of all nodes in network.
dictionary = {}
nodes = [nd.name for nd in pacific.nodes]

# loop through all nodes twice to get every combination and direction.
for start in nodes:
	for finish in nodes:
		# call the algorithm.
		distance, shortest_path = dijkstra(network=pacific, source_name=start, destination_name= finish)
		# only collate info if reachable and not 0 distance.
		if distance != np.inf and distance != 0:
			dictionary[start+' --> '+finish] = distance

# find max in dictionary collated values.
maximum = max(dictionary.values())
# unpack dictionary items and find string associated with max (shortest) distance.
for name, dist in dictionary.items(): 
    if dist == maximum:
        print(name)



# Some SUGGESTIONS if you're getting a bit stuck.
# - "There is no network file for the Pacific Migration?" Quite right, you'll need one though...
# - How many pairs of nodes are there in total?
# - What does the command [nd.name for nd in ntwk.nodes] return? (for Network object ntwk).
