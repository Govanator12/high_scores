class HighScores(object):
	scores = 0

	def __init__(self, scores):
		self.scores = scores

	def latest(self):
		return self.scores[-1]

	def personal_best(self):
		return max(self.scores)

	def personal_top_three(self):
		scores_list_sorted = sorted(self.scores)
		scores_list_sorted.reverse()

		if (len(scores_list_sorted)) <= 3:
			return scores_list_sorted

		else:	
			top_three_scores = []
			top_three_scores.append(scores_list_sorted[0])
			top_three_scores.append(scores_list_sorted[1])
			top_three_scores.append(scores_list_sorted[2])

			return top_three_scores





