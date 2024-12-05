from transformers import pipeline

class QAModel:
    def __init__(self):
        # Load a pre-trained question-answering model
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

    def answer_question(self, question: str, context: str):
        result = self.qa_pipeline(question=question, context=context)
        return result.get("answer", "Sorry, I couldn't find an answer.")
