# Calculator

A simple calculator with two versions:

- **`calculator.py`** — runs in your terminal. Enter expressions like
  `12 + 4` and it prints the result. Type `quit` to exit.
- **`index.html`** — a browser calculator styled after a real handheld,
  with an LCD-style screen (ghost digits and all). No installs needed.

## Run the CLI version

```bash
python3 calculator.py
```

## Run the web version

Open `index.html` in any browser. Works with mouse clicks or your keyboard
(numbers, `+ - * /`, `Enter` for `=`, `Escape` for clear).

## Hosting the web version on GitHub Pages

1. Push this repo to GitHub (steps below).
2. On the repo page, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to `Deploy from a branch`,
   pick the `main` branch and `/ (root)` folder, then **Save**.
4. After a minute or two, it'll be live at
   `https://<your-username>.github.io/<repo-name>/`.

## Pushing this project to GitHub

From inside this folder:

```bash
git init
git add .
git commit -m "Initial commit: calculator (CLI + web)"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

Create the empty repo on GitHub first (no README/license, so it stays
empty) so the `git push` above has somewhere to land.
