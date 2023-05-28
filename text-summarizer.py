import streamlit as st 

# NLP libs 


from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def sumy_summarizer(docx):
   parser=PlaintextParser.from_string(docx, Tokenizer("English"))
   lex_summarizer=LexRankSummarizer()
   summary=lex_summarizer(parser.document,3)
   summary_list = [str(sentence) for sentence in summary]
   result=' '.join(summary_list)
   return result


def main():
   """ NLP App """
   st.title("Text Summarizer")
   st.subheader("Natural Language Processing on the GO!")
   
   # Text summarizer 
   text = st.text_area("Enter your text here", "Enter atleast 100 words")
   
   
   if st.button("Summarize"):
      summary_result=sumy_summarizer(text)
      st.success(summary_result)
         
      
  
   
   
if __name__=="__main__":
   main()
