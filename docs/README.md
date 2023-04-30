# socialdata2023-assignment2
Assignment 2 in Socialdata


Set up ruby and jekyll according to Sune's guide.

First time run:

```
bundle install
```


To run the webpage locally with live-updates when developing change the following in the `_config.yml` file. You need to change the `baseurl` to `""`. Remember to switch back when pushing to github.

```
#for github pages - whenever you push to the repo below line should be uncommented.
baseurl: "socialdata2023-assignment2"

#for local development - only change temporarily.
baseurl: ""
```


To run the webpage locally with live-updates (i.e. you make a change -> it will display it immediatly on your localhost.)


```
bundle exec jekyll serve --livereload
```

To make changes go to `index.markdown`
