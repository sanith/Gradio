import numpy as np
import gradio as gr


def flip_text(X):
    return X[::-1]


def flip_image(X):
    return np.fliplr(X)


with gr.Blocks() as demo:
    gr.Markdown("Flip text or Image Files using the demo")
    with gr.Tab("Flip Text"):
        text_input = gr.Textbox()
        text_output = gr.Textbox()
        text_button = gr.Button("Flip")
    with gr.Tab("Flip Image"):
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
            image_button = gr.Button("Flip")

    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me ...")

    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)


demo.launch()