import gradio as gr

def test():
    return "TEST2HF е во функција!"

demo = gr.Interface(fn=test, inputs=[], outputs="text")
demo.launch()
