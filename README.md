<h1> Simple email automation :email: </h1>  

[![Linkedin: Pabloarruda](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/pabloarruda/)
[![Github: Pablo-aa](https://img.shields.io/github/followers/pablo-aa?style=social)](https://github.com/pablo-aa)
[![Open In Colab](https://img.shields.io/badge/Made%20by-Pablo%20Araujo-%23ea004f)](https://www.linkedin.com/in/pabloarruda/)

You need to send **SEVERAL** emails with specific content for each person and you don't want to do it by hand? This could help you!

<h2> Installation 🛠 </h2>

- Local Machine </br>
    Install <a href="https://www.python.org/downloads/">Python</a></br>
    Install <a href="https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html">Pandas</a></br>
    
- Online </br>
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

<h2> How to use? 📄</h2>

1. Create a excel table (.xlsx) like this 📁:

| Name  | Email  | Message  | Personal Info |
|-------|--------|----------|---------------|
|name 1 |email1  |message 1 | information 1 |
|name 2 |email2  |message2  | information 2 |
|name 3 |email3  |message3  | information 3 |

2. Configure some parts of the code 👨🏽‍💻 

```python
  # I. Configure your message in create_message function:
  def create_message(name, message, personal_info):
	return f'''
		<p>Olá {name}, </p>
		<p>{message}</p>
		<p>{personal_info}<p>
	'''
  # II. Configure your email credentials in envia_email function:
  def envia_email(corpo_email, dest):
      
      -> msg['Subject'] = 'Email Subject here'

      -> msg['From'] = 'email@gmail.com'

      -> password = "****" # Enter your password here
  
```
3. It's Done! ✅




  
