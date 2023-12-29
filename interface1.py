import gradio as gr


def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(lines=1, placeholder="Name Here..."),
            "checkbox", gr.Slider(0, 100, 20)],
    outputs=["text", "number"],
)
demo.launch()