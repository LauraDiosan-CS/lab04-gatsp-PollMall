from GA import GA

# ga=GA('laborator\\Lab4\\results\\easy_example.txt')
# ga=GA('laborator\\Lab4\\results\\easy_01_tsp.txt')
# ga=GA('laborator\\Lab4\\results\\medium_01_tsp.txt')
# ga=GA('laborator\\Lab4\\results\\hard_01_tsp.txt')

# ga=GA('laborator\\Lab4\\tsp-students\\50p_easy_01_tsp.txt')
# ga=GA('laborator\\Lab4\\tsp-students\\50p_hard_01_tsp.txt')
# ga=GA('laborator\\Lab4\\tsp-students\\50p_medium_01_tsp.txt')
# ga=GA('laborator\\Lab4\\tsp-students\\100p_fricker26.txt')
ga=GA('laborator\\Lab4\\tsp-students\\150p_eil51.txt')

best=ga.resolve()
print(best)