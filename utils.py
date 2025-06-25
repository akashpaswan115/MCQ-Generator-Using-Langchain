# ✅ Updated: Integrated with EURON API instead of Groq

# Import required libraries
import os
from typing import List
from dotenv import load_dotenv
from euriai.langchain_llm import EuriaiLangChainLLM
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator

# Load environment variables from .env file
load_dotenv()

# ✅ Use secure API key loading
api_key = os.getenv("EURON_API_TOKEN")

# Define data model for Multiple Choice Questions
class MCQQuestion(BaseModel):
    question: str = Field(description="The question text")
    options: List[str] = Field(description="List of 4 possible answers")
    correct_answer: str = Field(description="The correct answer from the options")

    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)

# Define data model for Fill in the Blank Questions
class FillBlankQuestion(BaseModel):
    question: str = Field(description="The question text with '_____' for the blank")
    answer: str = Field(description="The correct word or phrase for the blank")

    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)

class QuestionGenerator:
    def __init__(self):
        # ✅ Use Euron-compatible LangChain LLM
        self.llm = EuriaiLangChainLLM(
            api_key=api_key,
            model="gpt-4.1-nano",
            temperature=0.9
        )

    def generate_mcq(self, topic: str, difficulty: str = 'medium') -> MCQQuestion:
        mcq_parser = PydanticOutputParser(pydantic_object=MCQQuestion)

        prompt = PromptTemplate(
            template=(
                "Generate a {difficulty} multiple-choice question about {topic}.\n\n"
                "Return ONLY a JSON object with these exact fields:\n"
                "- 'question': A clear, specific question\n"
                "- 'options': An array of exactly 4 possible answers\n"
                "- 'correct_answer': One of the options that is the correct answer\n\n"
                "Example format:\n"
                '{{\n'
                '    "question": "What is the capital of France?",\n'
                '    "options": ["London", "Berlin", "Paris", "Madrid"],\n'
                '    "correct_answer": "Paris"\n'
                '}}\n\n'
                "Your response:"
            ),
            input_variables=["topic", "difficulty"]
        )

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                response = self.llm.invoke(prompt.format(topic=topic, difficulty=difficulty))
                parsed_response = mcq_parser.parse(response)
                if not parsed_response.question or len(parsed_response.options) != 4:
                    raise ValueError("Invalid format")
                return parsed_response
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise RuntimeError(f"MCQ Generation Failed: {str(e)}")
                continue

    def generate_fill_blank(self, topic: str, difficulty: str = 'medium') -> FillBlankQuestion:
        fill_blank_parser = PydanticOutputParser(pydantic_object=FillBlankQuestion)

        prompt = PromptTemplate(
            template=(
                "Generate a {difficulty} fill-in-the-blank question about {topic}.\n\n"
                "Return ONLY a JSON object with these exact fields:\n"
                "- 'question': A sentence with '_____' marking where the blank should be\n"
                "- 'answer': The correct word or phrase that belongs in the blank\n\n"
                "Example format:\n"
                '{{\n'
                '    "question": "The capital of France is _____.",\n'
                '    "answer": "Paris"\n'
                '}}\n\n'
                "Your response:"
            ),
            input_variables=["topic", "difficulty"]
        )

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                response = self.llm.invoke(prompt.format(topic=topic, difficulty=difficulty))
                parsed_response = fill_blank_parser.parse(response)
                if "_____" not in parsed_response.question:
                    raise ValueError("Question missing blank marker")
                return parsed_response
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise RuntimeError(f"FillBlank Generation Failed: {str(e)}")
                continue
