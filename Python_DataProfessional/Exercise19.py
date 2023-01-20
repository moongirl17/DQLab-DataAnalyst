#Tuple manipulasi

# Fitur .count()
print(">>> Fitur .count()")
tuple_score = ('Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud')
score_budi = tuple_score.count('Budi')
score_sud = tuple_score.count('Sud')
print(score_budi)
print(score_sud) 

# Fitur .index()
print(">>> Fitur .index()")
tuple_score = ('Budi','Sud','Budi','Budi','Budi','Sud','Sud')
score_pertama_sud = tuple_score.index('Sud')+1
print(score_pertama_sud)