# STEP 1: Install required packages
!pip install -q pydub plotly IPython

# STEP 2: Import modules
import numpy as np
import wave
import plotly.graph_objs as go
from pydub import AudioSegment
from IPython.display import Audio, display
import ipywidgets as widgets
import pandas as pd
import io
from google.colab import files

# STEP 3: Upload audio
from google.colab import files
uploaded = files.upload()

filename = list(uploaded.keys())[0]  # get uploaded filename

# STEP 4: Load and process audio
def load_waveform(filename):
        audio = AudioSegment.from_file(filename)
            audio_np = np.array(audio.get_array_of_samples())
                if audio.channels == 2:
                            audio_np = audio_np.reshape((-1, 2))
                                sr = audio.frame_rate
                                    duration = len(audio_np) / sr
                                        return audio_np, sr, duration

                                    audio_np, sample_rate, duration = load_waveform(filename)

                                    # STEP 5: Plot waveform
                                    time = np.linspace(0, duration, num=len(audio_np))
                                    fig = go.Figure()
                                    fig.add_trace(go.Scatter(x=time, y=audio_np if audio_np.ndim == 1 else audio_np[:, 0], mode='lines', name='Waveform'))
                                    fig.update_layout(title='Waveform Viewer', xaxis_title='Time (s)', yaxis_title='Amplitude', showlegend=False)
                                    fig.show()

                                    # STEP 6: Play audio
                                    display(Audio(filename))

                                    # STEP 7: Manual annotation widgets
                                    annotations = []

                                    start_box = widgets.FloatText(description='Start (s):')
                                    end_box = widgets.FloatText(description='End (s):')
                                    label_box = widgets.Text(description='Label:')
                                    add_button = widgets.Button(description='Add Annotation')
                                    output = widgets.Output()

                                    def add_annotation(b):
                                            with output:
                                                        start = round(start_box.value, 2)
                                                                end = round(end_box.value, 2)
                                                                        label = label_box.value
                                                                                if end <= start:
                                                                                                print("âŒ End must be after start.")
                                                                                                        else:
                                                                                                                        annotations.append((start, end, label))
                                                                                                                                    print(f"âœ… Added: {start}-{end} labeled '{label}'")

                                                                                                                                    add_button.on_click(add_annotation)

                                                                                                                                    display(widgets.VBox([start_box, end_box, label_box, add_button, output]))

                                                                                                                                    # STEP 8: Export annotations as CSV
                                                                                                                                    def export_annotations():
                                                                                                                                            df = pd.DataFrame(annotations, columns=["Start", "End", "Label"])
                                                                                                                                                buf = io.StringIO()
                                                                                                                                                    df.to_csv(buf, index=False)
                                                                                                                                                        buf.seek(0)
                                                                                                                                                            files.download("annotations.csv")

                                                                                                                                                            # Export button
                                                                                                                                                            export_btn = widgets.Button(description="í³¥ Export Annotations to CSV")

                                                                                                                                                            def on_export(b):
                                                                                                                                                                    export_annotations()

                                                                                                                                                                    export_btn.on_click(on_export)
                                                                                                                                                                    display(export_btn)
