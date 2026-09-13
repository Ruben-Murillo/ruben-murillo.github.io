# Ruben Murillo Engineering Portfolio

Static, self-contained portfolio for GitHub Pages.

## Publish on GitHub Pages
1. Create or use the repository `theamazingruben.github.io`.
2. Upload the **contents of this folder** to the repository root, preserving the folders.
3. Commit to the `main` branch.
4. In **Settings → Pages**, choose **Deploy from a branch**, then `main` and `/ (root)`.
5. Visit `https://theamazingruben.github.io`.

## Local preview
From this folder:
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`.

## Included local media
The Fan Machine, Coin Counter and RC Car images are stored directly under `assets/images/`. They no longer depend on Wix or a GitHub Actions migration workflow.

The current upload batch did not contain Soda Dispenser media, so that project uses a clean placeholder instead of broken image links. Add the original soda photos later under `assets/images/soda-machine/` if desired.

## Suggested next additions
- Original Voltron photos, video and PowerPoint.
- Raspberry Pi 5 lab screenshots / architecture diagram.
- GitHub profile and project repository links.
- Custom domain.
- Future ROS2 AMR project.
