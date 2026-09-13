# Ruben Murillo Engineering Portfolio

Static portfolio built for GitHub Pages.

## Publish on GitHub Pages
1. Create a GitHub repository named `<your-github-username>.github.io`.
2. Upload the contents of this folder to the repository root.
3. Commit and push to the `main` branch.
4. In **Settings → Pages**, set **Source** to **Deploy from a branch**, then select `main` and `/ (root)`.
5. Your site will be available at `https://<your-github-username>.github.io`.

## Local preview
From this folder:
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`.

## Important migration note
The Arduino project cards currently reference the existing Wix-hosted project images so the first version has visuals immediately. For a fully independent site, download your original photos/videos from Wix and replace those URLs with files under `assets/images/`.

## Suggested next edits
- Add original Voltron photos, video and PowerPoint.
- Add screenshots/diagram for the Raspberry Pi 5 lab.
- Add GitHub profile/repository links.
- Add a custom domain after the GitHub Pages version is live.
- Add the future ROS2 AMR project as the new featured project.
