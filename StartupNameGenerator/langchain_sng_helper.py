from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_startup_name_and_roles(business):
    # Chain 1: Startup Name
    name_prompt = PromptTemplate(
    input_variables=['business_field'],
    template = "I want to open a startup in the field of {business_field}.Suggest me a fancy name for this")


    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="startup_name")

    # Chain 2: Roles
    roles_prompt = PromptTemplate(
    input_variables = ['startup_name'],
    template = "Suggest some roles or positions for {startup_name}")



    roles_chain = LLMChain(llm=llm, prompt=roles_prompt, output_key="roles")

    chain = SequentialChain(
        chains=[name_chain, roles_chain],
        input_variables=['business_field'],
        output_variables=['startup_name', "roles"]
    )

    response = chain({'business_field': business})

    return response

if __name__ == "__main__":
    print(generate_startup_name_and_roles("Sustainability and Clean Energy"))
