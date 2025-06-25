# greylabsproject
# 🎧 Audio Annotation Tool (Google Colab)

This is an interactive audio annotation tool built for **Google Colab**. It lets you:

- 📂 Upload a `.wav` or `.mp3` file
- 📈 Visualize the waveform
- 🔊 Play the audio directly in the notebook
- ✍️ Manually annotate segments by typing start/end times and labels
- 💾 Export annotations as a CSV file

---

## 🛠️ Features

✅ Upload audio files (`.wav`, `.mp3`, etc.)  
✅ Automatically converts audio to waveform data  
✅ Plot waveform using Plotly  
✅ Play audio within notebook  
✅ Enter annotation (start, end, label) using widgets  
✅ Download annotations as `annotations.csv`

---

## 📚 How to Use

1. **Open the tool in Google Colab**

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

2. **Run each cell step-by-step**:
   - Install packages
   - Upload a `.wav` or `.mp3` file
   - View the waveform
   - Listen to the audio
   - Add annotations manually
   - Export annotations to CSV

---

## 📝 Annotation Format

Each annotation contains:

| Start (s) | End (s) | Label       |
|-----------|---------|-------------|
| 1.23      | 2.45    | "Speaker 1" |
| 3.00      | 4.10    | "Noise"     |

These are saved in a CSV file when you click **Export Annotations to CSV**.

---

## 💡 Future Ideas

- Click-to-select waveform segments
- Zoomable waveform viewer
- Support for loading multiple audio files
- JSON export format

---

## 🔧 Requirements

This notebook uses:

- `pydub`
- `plotly`
- `ipywidgets`
- `IPython`
- `numpy`
- `pandas`

All of these are installed automatically in Colab with:

```python
!pip install -q pydub plotly IPython
