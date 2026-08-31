<h1 align="center">WhatsApp Message Parser</h1>

<p align="center">
  <a href="whatsappMessagesParser.py"><img src="https://img.shields.io/badge/Project-whatsappMessagesParser.py-555555.svg" alt="Project entry file"></a>
  <a href="https://scholar.google.com/citations?user=bvyKhaEAAAAJ&hl=en"><img src="https://img.shields.io/badge/Publications-Google_Scholar-4285F4.svg" alt="Google Scholar"></a>
  <a href="https://www.kaggle.com/nizamuddinmaitlo"><img src="https://img.shields.io/badge/Profile-Kaggle-20BEFF.svg" alt="Kaggle profile"></a>
</p>

<p align="center"><b>Repository maintained by Nizamuddin Maitlo</b></p>

<p align="center">A local Tkinter utility for cleaning pasted messages and identifying their language.</p>

## 🔥 Overview

This lightweight desktop application accepts pasted message text, removes URLs, emojis, and punctuation, normalizes case, and labels each cleaned line with a language code using `langid`.

## ✨ Features

- Tkinter desktop interface.
- URL, emoji, punctuation, and case normalization.
- Per-line language identification.
- Immediate display of cleaned text and detected language codes.

## 🧪 Method and protocol

- Input is pasted into the local text box.
- Each line is cleaned independently.
- Language identification uses the locally installed `langid` model.
- The current script displays results without writing them to disk.

## 📁 Repository contents

| File | Purpose |
|---|---|
| `whatsappMessagesParser.py` | GUI, text cleaning, language detection, and result display |

## 🛠️ Setup

Install the Python dependencies:

~~~bash
python -m pip install langid googletrans
~~~

Tkinter is bundled with many Python installations; some Linux distributions require a separate Python Tk package.

## 📦 Data and inputs

| Resource | Purpose | Availability |
|---|---|---|
| Pasted message text | Input cleaned and classified by language | User-provided input |

No external dataset is required, and the current script does not save pasted messages to a repository file.

## 🚀 Running the project

Launch the desktop application:

~~~bash
python whatsappMessagesParser.py
~~~

## ♻️ Reproducibility

- Record the Python and library versions used for each run.
- Keep preprocessing, splits, thresholds, and random seeds fixed when comparing results.
- Do not commit private input data, generated model weights, or machine-specific paths.
- Revalidate results when the dataset, sensor, operating environment, or dependency versions change.

## 📚 Publications

No paper-specific DOI is currently associated with this repository. This section is intentionally kept separate from related publications to avoid implying a publication-to-code relationship that has not been established.



## ⚠️ Scope and limitations

Regular-expression emoji removal is not exhaustive, and short or code-switched messages can be difficult to classify reliably. Review cleaned output before using it for analysis or downstream automation.

## 📄 License

No standalone license file is currently included in this repository.

## 🤝 Acknowledgements

This project uses open-source Python libraries and the data or inputs described above. We thank the original dataset, framework, and software contributors.
