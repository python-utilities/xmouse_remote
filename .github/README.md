# XMouse Remote
[heading__title]:
  #xmouse-remote
  "&#x2B06; Top of ReadMe File"


Python2/3 mouse wrapper API of `Xlib`


## [![Byte size of __init__.py][badge__master__xmouse_remote__source_code]][xmouse_remote__master__source_code] [![Open Issues][badge__issues__xmouse_remote]][issues__xmouse_remote] [![Open Pull Requests][badge__pull_requests__xmouse_remote]][pull_requests__xmouse_remote] [![Latest commits][badge__commits__xmouse_remote__master]][commits__xmouse_remote__master]



------


#### Table of Contents


- [:arrow_up: Top of ReadMe File][heading__title]

- [:zap: Quick Start][heading__quick_start]

  - [:memo: Edit Your ReadMe File][heading__your_readme_file]
  - [:snake: Utilize XMouse Remote][heading__utilize]
  - [:floppy_disk: Commit and Push][heading__commit_and_push]

- [&#x1F5D2; Notes][heading__notes]

- [&#x2696; License][heading__license]


------



## Quick Start
[heading__quick_start]:
  #quick-start
  "&#9889; Perhaps as easy as one, 2.0,..."


**Bash Variables**


```Bash
_module_name='xmouse_remote'
_module_https_url="https://github.com/python-utilities/${_module_name}.git"
_module_relative_path="lib/modules/${_module_name}"
```


**Bash Submodule Commands**


```Bash
cd "<your-git-project-path>"

git checkout masters
mkdir -vp "lib/modules"

git submodule add\
 -b master --name "${_module_name}"\
 "${_module_https_url}" "${_module_relative_path}"
```


### Your ReadMe File
[heading__your_readme_file]:
  #your-readme-file
  "&#x1F4DD; Suggested additions for your ReadMe.md file so everyone has a good time with submodules"


Suggested additions for your _`ReadMe.md`_ file so everyone has a good time with submodules


```MarkDown
Clone with the following to avoid incomplete downloads


    git clone --recurse-submodules <url-for-your-project>


Update/upgrade submodules via


    git submodule update --init --merge --recursive
```


### Utilize XMouse Remote
[heading__utilize]:
  #utilize-xmouse-remote
  "&#x1F40D; How to make use of this submodule within another project"


```Python
#!/usr/bin/env python


from lib.modules.xmouse_remote import XMouse_Remote


mouse = XMouse_Remote(display = ':0')

print("XMouse_Remote location -> {}".format(mouse.location))
mouse.move_absolute(x = 5, y = 5)
```


### Commit and Push
[heading__commit_and_push]:
  #commit-and-push
  "&#x1F4BE; It may be just this easy..."


```Bash
git add .gitmodules
git add lib/modules/xmouse_remote


## Add any changed files too


git commit -F- <<'EOF'
:heavy_plus_sign: Adds `python-utilities/xmouse_remote#1` submodule

# ... anything else noteworthy
EOF


git push origin master
```


**:tada: Excellent :tada:** your repository is now ready to begin unitizing code from this project!


___


## Notes
[heading__notes]:
  #notes
  "&#x1F5D2; Additional resources and things to keep in mind when developing"


There maybe bugs or missing features, Pull Requests are welcome.

___


## License
[heading__license]:
  #license
  "&#x2696; Legal bits of Open Source software"


Legal bits of Open Source software


```
XMouse Remote ReadMe documenting how things like this could be utilized
Copyright (C) 2019  S0AndS0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```



[badge__commits__xmouse_remote__master]:
  https://img.shields.io/github/last-commit/python-utilities/xmouse_remote/master.svg

[commits__xmouse_remote__master]:
  https://github.com/python-utilities/xmouse_remote/commits/master
  "&#x1F4DD; History of changes on this branch"


[xmouse_remote__community]:
  https://github.com/python-utilities/xmouse_remote/community
  "&#x1F331; Dedicated to functioning code"


[xmouse_remote__gh_pages]:
  https://github.com/python-utilities/xmouse_remote/tree/gh-pages
  "Source code examples hosted thanks to GitHub Pages!"



[badge__demo__xmouse_remote]:
  https://img.shields.io/website/https/python-utilities.github.io/xmouse_remote/index.html.svg?down_color=darkorange&down_message=Offline&label=Demo&logo=Demo%20Site&up_color=success&up_message=Online

[demo__xmouse_remote]:
  https://python-utilities.github.io/xmouse_remote/index.html
  "&#x1F52C; Check the example collection tests"


[badge__issues__xmouse_remote]:
  https://img.shields.io/github/issues/python-utilities/xmouse_remote.svg

[issues__xmouse_remote]:
  https://github.com/python-utilities/xmouse_remote/issues
  "&#x2622; Search for and _bump_ existing issues or open new issues for project maintainer to address."


[badge__pull_requests__xmouse_remote]:
  https://img.shields.io/github/issues-pr/python-utilities/xmouse_remote.svg

[pull_requests__xmouse_remote]:
  https://github.com/python-utilities/xmouse_remote/pulls
  "&#x1F3D7; Pull Request friendly, though please check the Community guidelines"


[badge__master__xmouse_remote__source_code]:
  https://img.shields.io/github/size/python-utilities/xmouse_remote/__init__.py.svg?label=__init__.py

[xmouse_remote__master__source_code]:
  https://github.com/python-utilities/xmouse_remote/blob/master/__init__.py
  "&#x2328; Project source, one Python file of importable code!"