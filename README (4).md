# Jarvis Voice Assistant

A simple wake-word voice assistant. Say "jarvis" to wake it up, then give
it a command:

- **"open <site>"** — opens any site in the list: google, youtube,
  gmail, github, spotify, netflix, amazon, wikipedia, twitter, instagram,
  facebook, whatsapp, maps, drive, reddit, linkedin, calendar, chatgpt,
  claude
- **"play geography"** / **"play skyfall"** — opens the matching track

Add more sites by adding an entry to the `SITES` dict (`jarvis_assistant.py`)
or the `SITES` object (`index.html`) — key is the spoken name, value is the
URL.

Two versions are included:

- **`jarvis_assistant.py`** — runs locally, uses your system microphone via
  `speech_recognition` and speaks replies with `pyttsx3`.
- **`index.html`** — runs in the browser using the Web Speech API, with a
  live waveform visualizer built from your mic input. No installs needed.

## Run the CLI version

```bash
pip install -r requirements.txt
python3 jarvis_assistant.py
```

`PyAudio` (a dependency of `speech_recognition`'s microphone support) can be
fiddly to install:
- **macOS**: `brew install portaudio` first, then `pip install pyaudio`
- **Windows**: `pip install pyaudio` usually works directly, or grab a
  prebuilt wheel if it fails
- **Linux**: `sudo apt install portaudio19-dev` first, then `pip install pyaudio`

## Run the web version

Open `index.html` in **Chrome** or another Chromium-based browser (Web
Speech API support elsewhere, like Firefox, is limited). Click **Start
Jarvis** and allow microphone access when prompted.

**Note:** for the microphone to work reliably, the page needs to be served
over `https://` or `http://localhost` — opening the file directly
(`file://...`) may be blocked by the browser. GitHub Pages (below) serves
over `https://`, so that's the easiest way to get a working mic permission
prompt.

## Hosting the web version on GitHub Pages

1. On this repo's page, go to **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to `Deploy from a branch`,
   pick the `main` branch and `/ (root)` folder, then **Save**.
3. After a minute or two, it'll be live at
   `https://jainaradhy27.github.io/JARVIS/`.

## A note on file names

GitHub added `(5)` / `(2)` suffixes to some files because of repeated
uploads with the same name. Rename `index (5).html` to plain `index.html`
(click the file, then the pencil icon, edit the filename at the top, then
commit) — GitHub Pages specifically looks for `index.html` to serve as the
homepage, so the site won't load correctly until that's renamed.

## A note on the removed API key

The original script had an unused, hardcoded API key sitting in the code.
It's been removed here — nothing in this version relies on it. If you had
plans for it (e.g. a news feature), load it from an environment variable
or a local `.env` file instead, and add that file to `.gitignore` so it
never gets committed. A key sitting in a public repo can be found and
misused within minutes of pushing.
