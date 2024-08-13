## Mailing-with-Excel-data-challenge

This project is an Email automatization robot built with Python and the RPA library.
The robot creates Emails with data from a local .xlsx file, authorizes with a given Gmail account
and then sends the generated Emails to the target recepient. Great for saving time when there is a lot of mail to send)

## Technology Stack:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Robocorp](https://img.shields.io/badge/-Robocorp-464646?style=flat&logo=Robocorp&logoColor=56C0C0&color=008080)](https://www.robocorp.com/)

## Project setup:

* Fork and locally clone the the GitHub repository:

* Navigate to the locally cloned repository, create and activate virtual environment:

for Linux/macOS:
'''
python3.11 -m venv myenv
source myenv/bin/activate
'''
for Windows:
'''
python -m venv myenv
myenv\Scripts\activate
'''

* Create an .env file in the project root directory, fill it as demonstrated in the example .env file
You will need to create an app password in Google to allow the robiot to access Gmail see more here:
'''
https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237
'''

* See the Running and Dependencies sections below if you have questions about project requirements and launch.


## Template: Python - Minimal

This Robocorp template leverages the new [Python framework](https://github.com/robocorp/robocorp), the [libraries](https://github.com/robocorp/robocorp/blob/master/docs/README.md#python-libraries) from to same project as well.

The template provides the basic structure of a Python project: logging out of the box and controlling tasks without fiddling with the base Python stuff.
The environment contains the most used libraries, so you do not have to start thinking about those right away. 

👉 Other templates are available as well via our tooling and on [Portal](https://robocorp.com/portal/tag/template)

## Running

#### VS Code
1. Get [Robocorp Code](https://robocorp.com/docs/developer-tools/visual-studio-code/extension-features) -extension for VS Code.
1. You'll get an easy-to-use side panel and powerful command-palette commands for running, debugging, code completion, docs, etc.

#### Command line

1. [Get RCC](https://github.com/robocorp/rcc?tab=readme-ov-file#getting-started)
1. Use the command: `rcc run`

## Results

🚀 After running the bot, check out the `log.html` under the `output` -folder.

## Dependencies

We strongly recommend getting familiar with adding your dependencies in [conda.yaml](conda.yaml) to control your Python dependencies and the whole Python environment for your automation.

<details>
  <summary>🙋‍♂️ "Why not just pip install...?"</summary>

Think of [conda.yaml](conda.yaml) as an equivalent of the requirements.txt, but much better. 👩‍💻 With `conda.yaml`, you are not just controlling your PyPI dependencies; you control the complete Python environment, which makes things repeatable and easy.

👉 You will probably need to run your code on another machine quite soon, so by using `conda.yaml`:
- You can avoid `Works on my machine` -cases
- You do not need to manage Python installations on all the machines
- You can control exactly which version of Python your automation will run on 
  - You'll also control the pip version to avoid dep. resolution changes
- No need for venv, pyenv, ... tooling and knowledge sharing inside your team.
- Define dependencies in conda.yaml, let our tooling do the heavy lifting.
- You get all the content of [conda-forge](https://prefix.dev/channels/conda-forge) without any extra tooling

> Dive deeper with [these](https://github.com/robocorp/rcc/blob/master/docs/recipes.md#what-is-in-condayaml) resources.

</details>
<br/>

> The full power of [rpaframework](https://robocorp.com/docs/python/rpa-framework) -libraries is also available on Python as a backup while we implement the new Python libraries.

## Additionally:

👉 Try out [Robocorp ReMark 💬](https://chat.robocorp.com)

For more information, check out the following:
- [Robocorp Documentation -site](https://robocorp.com/docs)
- [Portal for more examples](https://robocorp.com/portal)
- Follow main [robocorp -repository](https://github.com/robocorp/robocorp) as it is the main location where we developed the libraries and the framework.


## Project Author:
Stanislav Berezovskii, https://github.com/StanislavBerezovskii
