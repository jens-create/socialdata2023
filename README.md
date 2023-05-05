# socialdata2023
This is the repo for the DTU course Social Data Analysis and Visualization

The repo contains my answers to the DTU course.

## How to update github pages

Set up ruby and jekyll according to Sune's guide.

First time run:

```
bundle install
```


To run the webpage locally with live-updates when developing change the following in the `_config.yml` file. You need to change the `baseurl` to `""`. Remember to switch back when pushing to github.

```
#for github pages - whenever you push to the repo below line should be uncommented.
baseurl: "socialdata2023"

#for local development - only change temporarily.
baseurl: ""
```

To run the webpage locally with live-updates (i.e. you make a change -> it will display it immediatly on your localhost.)

```
bundle exec jekyll serve --livereload
```

To make changes go to `index.md` and make changes there. The page is built from the `index.md` file and the `_layouts/default.html` file. The `default.html` file contains the html structure of the page. The `index.md` file contains the content of the page. The `index.md` file is written in markdown. You can read about markdown here: https://www.markdownguide.org/basic-syntax/



## How to fetch from original repo

```
git fetch upstream
git merge upstream/main main
```
