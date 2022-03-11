from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="Sahajtomar/German_Zeroshot")

sequence = "Letzte Woche gab es einen Selbstmord in einer nahe gelegenen kolonie"
candidate_labels = ["Verbrechen","Tragödie","Stehlen"]
hypothesis_template = "In deisem geht es um {}."

print(classifier(sequence, candidate_labels, hypothesis_template=hypothesis_template))