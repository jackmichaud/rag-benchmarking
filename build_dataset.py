import environment_variables

from langsmith import Client

# QA
inputs = [
    "What is the main objective of Catan?",
    "How many players can play Catan?",
    "What are the five types of resources in Catan?",
    "How do players acquire resources in Catan?",
    "What is required to build a road?",
    "What is required to build a settlement?",
    "What is required to build a city?",
    "What is required to buy a development card?",
    "What does the robber do?",
    "How is the longest road determined?",
    "How is the largest army determined?",
    "What are development cards?",
    "How many victory pointsis a settlement worth?",
    "How many victory points is a city worth?",
    "What happens when a 7 is rolled?",
    "Can you trade resources with other players?",
    "What is a port in Catan?",
    "How many development cards can you play per turn?",
    "What is the starting player determined by?",
    "Can roads be placed anywhere on the board?",
    "Can settlements be placed anywhere on the board?",
    "What does a knight card do?",
    "What does the road building card do?",
    "What does the year of plenty card do?",
    "What does the monopoly card do?",
    "Can you play a development card the same turn you buy it?",
    "How do you win the game?",
    "What happens if two players tie for the longest road or largest army?",
    "Can you build more than one road on your turn?",
    "What are the possible numbers on the hex tiles?",
    "Can cities be built on hex tiles with any number?",
    "How many resource cards do you start with?",
    "What is the maximum number of resource cards you can hold without penalty?",
    "What happens when you run out of a specific resource in the bank?",
    "Can you build more than one settlement on your turn?",
    "How do you get a port?",
    "How do you use a port?",
    "What are hex tiles?",
    "Can the robber be moved to the desert tile?",
    "What is a resource card?",
    "How many roads do players start with?",
    "How many settlements do players start with?",
    "How many cities do players start with?",
    "What is the setup process for Catan?",
    "What is the purpose of the dice in Catan?",
    "Can you upgrade a settlement to a city?",
    "Can development cards be traded between players?",
    "How do you keep track of victory points?",
    "What is the maximum number of development cards you can hold?",
    "Can you place a road without connecting it to a settlement or city?"
]

outputs = [
    "The main objective is to be the first player to reach 10 victory points.",
    "Catan can be played by 3 to 4 players in the base game, and up to 6 players with expansions.",
    "Brick, wood, ore, wheat, and sheep.",
    "Players acquire resources based on dice rolls that match the numbers on the hex tiles adjacent to their settlements or cities.",
    "1 brick and 1 wood.",
    "1 brick, 1 wood, 1 wheat, and 1 sheep.",
    "2 wheat and 3 ore.",
    "1 wheat, 1 sheep, and 1 ore.",
    "The robber prevents resource production on the hex it occupies and allows the player who moved it to steal a resource card from another player adjacent to that hex.",
    "The player with the longest continuous road of at least 5 segments receives the Longest Road card, worth 2 victory points.",
    "The player with the largest army of at least 3 knight cards receives the Largest Army card, worth 2 victory points.",
    "Development cards are special cards that provide various benefits, such as knights, road building, and additional victory points.",
    "1 victory point.",
    "2 victory points.",
    "The robber is moved, and any player with more than 7 resource cards must discard half of them.",
    "Yes, players can trade resources with each other on their turn.",
    "A port allows players to trade resources at a more favorable rate, such as 2:1 or 3:1.",
    "You can play one development card per turn.",
    "The starting player is determined by the highest roll of two dice during setup.",
    "No, roads must connect to a player's existing roads, settlements, or cities.",
    "No, settlements must be placed at the intersection of three hexes, at least two road segments away from any other settlements or cities.",
    "A knight card allows a player to move the robber and steal a resource card from a player adjacent to the robber's new location.",
    "The road building card allows a player to place two new roads on the board.",
    "The year of plenty card allows a player to take any two resource cards from the bank.",
    "The monopoly card allows a player to choose a resource and take all of that resource from other players.",
    "No, development cards cannot be played on the same turn they are purchased.",
    "You win the game by being the first player to reach 10 victory points.",
    "If two players tie, neither player receives the points until one player has a longer road or larger army.",
    "Yes, as long as you have the resources and the roads connect to your existing roads, settlements, or cities.",
    "The possible numbers are 2 through 12, excluding 7.",
    "Yes, cities can be built on any hex tile, regardless of the number.",
    "Players start with resource cards based on the hexes adjacent to their second settlement.",
    "You can hold up to 7 resource cards without penalty; if you have more when a 7 is rolled, you must discard half.",
    "If the bank runs out of a resource, no more of that resource can be drawn until some are returned.",
    "Yes, as long as you have the resources and the placements follow the building rules.",
    "You get a port by building a settlement on a port location.",
    "To use a port, you must trade the specified number of resources indicated by the port.",
    "Hex tiles are the terrain pieces that make up the Catan board, representing different types of land that produce resources.",
    "Yes, the robber can be moved to the desert tile, which does not produce any resources.",
    "A resource card represents one of the five resources (brick, wood, ore, wheat, sheep) used in the game.",
    "Players start with 15 road pieces.",
    "Players start with 5 settlement pieces.",
    "Players start with 4 city pieces.",
    "Players take turns placing two settlements and two roads on the board, collecting resources from the hexes adjacent to their second settlement.",
    "The dice determine which hexes produce resources each turn based on the numbers placed on the hex tiles.",
    "Yes, you can upgrade a settlement to a city by paying 2 wheat and 3 ore.",
    "No, development cards cannot be traded between players.",
    "Victory points are tracked by counting settlements, cities, development cards, and special cards like Longest Road and Largest Army.",
    "There is no limit to the number of development cards a player can hold.",
    "No, roads must always connect to a player's existing roads, settlements, or cities."
]

qa_pairs = [{"question": q, "answer": a} for q, a in zip(inputs, outputs)]

# Create dataset
client = Client()
dataset_name = "RAG_test_catan"
dataset = client.create_dataset(
    dataset_name=dataset_name,
    description="QA pairs about Catan.",
)
client.create_examples(
    inputs=[{"question": q} for q in inputs],
    outputs=[{"answer": a} for a in outputs],
    dataset_id=dataset.id,
)