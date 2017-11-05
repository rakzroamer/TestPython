fscore = float(score)

if not fscore <= 0.0 or fscore >= 1.0:
    if fscore >0.0 and fscore <0.6:
        print ("F")
    elif fscore >=0.6 and fscore <0.7:
        print ("D")
    elif fscore >=0.7 and fscore <0.8:
        print ("C")
    elif fscore >=0.8 and fscore <0.9:
        print ("B")
    else:
        print ("A")
