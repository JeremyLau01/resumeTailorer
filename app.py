from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")

def index():
  flash("Enter your job description")
  return render_template("index.html")

def add_format():
  global overleaf
  format = r'''%-------------------------
% Resume in Latex
% Author : Jeremy Lau
% Based off of: https://github.com/sb2nov/resume
% License : MIT
%------------------------

\documentclass[letterpaper,12pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}


%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\begin{document}'''
  overleaf += format

def add_header():
  global overleaf
  header_no_location = r'''\begin{center}
    \textbf{\Huge \scshape Jeremy Lau} \\ \vspace{1pt}
    \small 617-208-9500 $|$ \href{mailto:jlau1@bu.edu}{\underline{jlau1@bu.edu}} $|$ 
    \href{https://www.linkedin.com/in/jeremy-lau1/}{\underline{linkedin.com/in/jeremy-lau1/}} $|$
    \href{https://github.com/JeremyLau01}{\underline{github.com/JeremyLau01}}
\end{center}'''
  header_boston = r'''\begin{center}
    \textbf{\Huge \scshape Jeremy Lau} \\ \vspace{1pt}
    \small 617-208-9500 $|$ \href{mailto:jlau1@bu.edu}{\underline{jlau1@bu.edu}} $|$
    \href{https://www.linkedin.com/in/jeremy-lau1/}{\underline{linkedin.com/in/jeremy-lau1/}} $|$
    \href{https://github.com/JeremyLau01}{\underline{github.com/JeremyLau01}} $|$ Boston, MA
\end{center}'''
  strings_to_check = ["MA", "Boston", "Massachusetts"]
  contains = False
  for location in strings_to_check:
     if location in job_description:
        contains = True
  if contains:
     overleaf += "\n" + header_boston     
  else:
    overleaf += "\n" + header_no_location
    
def get_languages(my_languages):
    global job_description
    # Split the sentence into words
    new_job_description = job_description.lower().replace(",", "")
    for language in my_languages:
       new_job_description += " " + language

    words = new_job_description.split()

    # Count the occurrences of each word in the sentence
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort the word_list first by count and then by order of appearance
    sorted_languages = sorted(my_languages, key=lambda x: (-word_counts.get(x.lower(), 0), new_job_description.index(x.lower())))
    return sorted_languages

def add_experience():
  global overleaf, job_description
  
  xp1_start = r'''\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheading
      {Strong Compute (YC W22)}{Aug. 2023 -- Oct. 2023}
      {'''
  # SWE intern, AI Team Lead (leadership)
  xp1_skills_list = []
  if "leadership" in job_description.lower() or "managing" in job_description.lower() or "manage" in job_description.lower() or "lead" in job_description.lower() or "management" in job_description.lower() or "ai" in job_description.lower().split() or "machine learning" in job_description.lower() or "artificial intelligence"  in job_description.lower():
     xp1_role = r'''AI Team Lead'''
     xp1_skills_list.append("Leadership")
  else:
     xp1_role = r'''Software Engineering Intern'''
  
  # Python, External stakeholder: ISC,
  holder_xp1 = ""
  if "stakeholder" in job_description.lower() or "client" in job_description.lower():
     xp1_skills_list.append("External Stakeholder: ISC")
  if "agile" in job_description.lower():
     xp1_skills_list.append("Agile")
  if "quality assurance" in job_description.lower() or "qa" in job_description.lower() or "quality" in job_description.lower() or "verification" in job_description.lower() or "validation" in job_description.lower():
     xp1_skills_list.append("QA testing")
  if "python" in job_description.lower():
     xp1_skills_list.append("Python")

  if len(xp1_skills_list) > 0:
     for skill in xp1_skills_list:
        holder_xp1 += skill + ", "
     holder_xp1 = holder_xp1[:-2]
     xp1_skills = r''' $|$ \emph{''' + holder_xp1 + r'''}'''
  else:
     xp1_skills = r''''''
  xp1_end = r'''}{Sydney, Australia}
      \resumeItemListStart
        \resumeItem{Reduced 86\% of expected operational cost by implementing a budgeting workflow}
        \resumeItem{Led agile team of 6 to increase 91\% of training efficiency for Python machine learning model}
        \resumeItem{Managed 2 successful major deliverables including documentation, final code, data, and analysis}
      \resumeItemListEnd'''
  
  xp2_start = r'''\resumeSubheading
      {Draper}{May 2023 -- July 2023}
      {'''
  xp2_role = r'''Software Engineering Intern'''

  # quality assurance testing, ci/cd, C#, Unity; External stakeholder: United States Navy
  holder_xp2 = ""
  xp2_skills_list = []
  if "stakeholder" in job_description.lower() or "client" in job_description.lower():
     xp2_skills_list.append("External Stakeholder: United States Navy")
  if "quality assurance" in job_description.lower() or "qa" in job_description.lower().split() or "quality" in job_description.lower() or "verification" in job_description.lower() or "validation" in job_description.lower():
     xp2_skills_list.append("QA testing")
  if "c#" in job_description.lower():
     xp2_skills_list.append("C\#")

  if len(xp2_skills_list) > 0:
     for skill in xp2_skills_list:
        holder_xp2 += skill + ", "
     holder_xp2 = holder_xp2[:-2]
     xp2_skills = r''' $|$ \emph{''' + holder_xp2 + r'''}'''
  else:
     xp2_skills = r''''''
  xp2_end = r'''}{Boston, MA}
      \resumeItemListStart
        \resumeItem{Improved 24\% of performance for Navy submarine simulation by upgrading 12 C\# scripts}
        \resumeItem{Resolved 4 third-party asset and plugin compatibility issues to adapt the project to Unity 2021 updates}
        \resumeItem{Performed 3 quality assurance processes: MATLAB testing, code review process, and git version control}
      \resumeItemListEnd'''
  
  xp3_start = r'''\resumeSubheading
      {Chinese Family Recipes}{Jan. 2023 -- Apr. 2023}
      {'''
  
  if "fullstack" in job_description.lower() or "full stack" in job_description.lower() or "full-stack" in job_description.lower() or (("frontend" in job_description.lower() or "front-end" in job_description.lower() or "front end" in job_description.lower()) and ("backend" in job_description.lower() or "back end" in job_description.lower() or "back-end" in job_description.lower() or "database" in job_description.lower())):
     xp3_role = r'''Full Stack Developer Intern'''
  elif "frontend" in job_description.lower() or "front-end" in job_description.lower() or "front end" in job_description.lower():
     xp3_role = r'''Front End Developer Intern'''
  elif "web developer" in job_description.lower() or "website developer" in job_description.lower():
     xp3_role = r'''Web Developer Intern'''
  else:
     xp3_role = r'''Software Engineering Intern'''
  
  xp3_skills_list = []
  xp3_langs = ["HTML", "CSS", "JavaScript"]

  if "react" in job_description.lower() or "react.js" in job_description.lower():
     xp3_skills_list.append("React")
  if "node" in job_description.lower() or "node.js" in job_description.lower():
     xp3_skills_list.append("Node.js")
  
  dict_xp3 = {}
  for lang in xp3_langs:
     dict_xp3[lang] = job_description.lower().count(lang.lower())
  
  sorted_words = sorted(dict_xp3.items(), key=lambda x: (-x[1], x[0]))
  # Filter out words with count <= 0
  sorted_words = [(word, count) for word, count in sorted_words if count > 0]
  # Extract only the words (keys) from the sorted list
  sorted_words_only = [word for word, count in sorted_words]

  xp3_skills_list += sorted_words_only

  if len(xp3_skills_list) > 0:
     holder_xp3 = ""
     for skill in xp3_skills_list:
        holder_xp3 += skill + ", "
     holder_xp3 = holder_xp3[:-2]
     xp3_skills = r''' $|$ \emph{''' + holder_xp3 + r'''}'''
  else:
     xp3_skills = r''''''
  xp3_end = r'''}{Boston, MA}
      \resumeItemListStart
        \resumeItem{Developed 28 fully responsive React frontend pages and a Nodejs backend for full-stack recipe site}
        \resumeItem{Used HTML, CSS, and JavaScript to create a component-based design in React}
        \resumeItem{Integrated Firebase to securely store 20+ listings using JavaScript SDK methods}
    \resumeItemListEnd
    \resumeSubHeadingListEnd
'''
  
  overleaf += "\n" + xp1_start + xp1_role + xp1_skills + xp1_end + xp2_start + xp2_role + xp2_skills + xp2_end + xp3_start + xp3_role + xp3_skills + xp3_end

def add_projects():
  global overleaf, job_description

  # Etc. 
  p1_keywords = ["Test Automation: JUnit, Jenkins, Gradle, Git", "QA tools: JUnit, Jenkins, GitHub, Agile, Scrum", "CI/CD Pipeline: JUnit, Jenkins, Gradle, Git"]
  p1_other_skills = ["JavaFX", "Java", "JUnit", "Jenkins", "Gradle", "Git"]

  # Sort these by occurances; also mark by ... (keywords, then skills)
  p1_skills_holder = ""
  if "automated testing" in job_description.lower() or "test automation" in job_description.lower() or "automated software testing" in job_description.lower() or "software testing" in job_description.lower() or "test case" in job_description.lower() or "testing" in job_description.lower():
     p1_skills_holder = p1_keywords[0]
  elif "quality assurance" in job_description.lower() or "qa" in job_description.lower() or "quality" in job_description.lower() or "verification" in job_description.lower() or "validation" in job_description.lower():
     p1_skills_holder = p1_keywords[1]
  elif "ci" in job_description.lower() or "cd" in job_description.lower() or "continuous" in job_description.lower() or "continuous integration" in job_description.lower() or "continuous deployment" in job_description.lower() or "continuous development" in job_description.lower():
     p1_skills_holder = p1_keywords[2]
  else:
     if "git" in job_description.lower().split():
        p1_skills_holder += "Git"

  if p1_skills_holder == "":
     p1_skills = ""
  else:
     p1_skills = r''' $|$ \emph{''' + p1_skills_holder + r'''}'''
  
  if "java" in job_description.lower():
    if p1_skills == "":
       p1_skills += "Java"
    else:
       p1_skills += ", Java"

  p2_skills_holder = ""
  p2_list = []
  if "python" in job_description.lower():
     p2_list.append("Python")
  
  if "machine learning" in job_description.lower() or "ml" in job_description.lower().split() or "ai" in job_description.lower().split():
     p2_list.append("Machine Learning")
     p2_list.append("Keras")
     p2_list.append("scikit-learn")
  elif "keras" in job_description.lower():
     p2_list.append("Keras")
  elif "scikit" in job_description.lower() or "sci-kit" in job_description.lower():
     p2_list.append("scikit-learn")
  
  if "git" in job_description.lower().split():
     p2_list.append("Git")
  
  if len(p2_list) > 0:
     for skill in p2_list:
        p2_skills_holder += skill + ", "
     p2_skills_holder = p2_skills_holder[:-2]
     p2_skills = r''' $|$ \emph{''' + p2_skills_holder + r'''}'''
  else:
     p2_skills = r''''''

  p1_start = r'''%-----------PROJECTS-----------
\section{Projects}
    \resumeSubHeadingListStart
      \resumeProjectHeading
          {\textbf{Java File Manager}'''
  
  p1_end = r'''}{Sept. 2023 -- Oct. 2023}
          \resumeItemListStart
            \resumeItem{Achieved 95\% code coverage for Java file management system, used Jenkins and JUnit for automated unit testing and Continuous Integration/Continuous Deployment (CI/CD), Gradle for application building}
            \resumeItem{Executed scrum and agile methodologies over a 4-week sprint, utilized Jira for backlog and artifacts}
          \resumeItemListEnd'''
  
  p2_start = r'''
      \resumeProjectHeading
        {\textbf{Python ML Predictor}'''
  
  p2_end = r'''}{Apr. 2023 -- May 2023}
          \resumeItemListStart
            \resumeItem{Trained 11 CNN and KNN models to accurately detect pneumonia from chest X-ray images}
            \resumeItem{Raised validation accuracy from 70\% to 88\% by tuning preprocessing, convolutional, max pool layers}
        \resumeItemListEnd
      \resumeSubHeadingListEnd'''

  projects = p1_start + p1_skills + p1_end + p2_start + p2_skills + p2_end
  overleaf += "\n" + projects

def add_activities():
   global overleaf
   activities = r'''\section{Activities and Societies}
    \resumeSubHeadingListStart
        \resumeItem{\textbf{PM Ready Executive Board:} University club teaching students how to become Product Managers}
        \resumeItem{\textbf{Hobbies:} Badminton, Soccer, Basketball, Game Development}
    \resumeSubHeadingListEnd'''
   overleaf += "\n" + activities

def load_end():
  global overleaf
  overleaf += "\n" + r'''\end{document}'''

def add_education():
  global overleaf, job_description
  pre_courses = r'''%-----------EDUCATION-----------
  \section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Boston University}{Boston, MA}
      {Bachelor of Arts in Computer Science, GPA: 3.87}{Sept. 2021 -- May 2025}
  \resumeItemListStart
        \resumeItem{\textbf{Relevant Courses:} '''
  post_courses = r'''}
      \resumeItemListEnd
    \resumeSubheading
      {University of Sydney}{Sydney, Australia}
      {Bachelor of Arts in Computer Science}{Aug. 2023 -- December 2023}
  \resumeSubHeadingListEnd'''
  courses = ""
  courses_start = []
  courses_end = []
  if "machine learning" in job_description.lower() or "ai" in job_description.lower().split() or "artificial intelligence" in job_description.lower() or "ml" in job_description.lower().split():
     courses_start += ["Intro to AI", "Distributed Systems", "Probability", "Linear Algebra"]
  else:
     courses_end += ["Intro to AI", "Distributed Systems", "Probability", "Linear Algebra"]
  
  if "sql" in job_description.lower() or "xml" in job_description.lower() or "database" in job_description.lower() or "relational" in job_description.lower():
     courses_start.append("SQL and XML Databases")
  else:
     courses_end = ["SQL and XML Databases"] + courses_end
  
  if "java" in job_description.lower().split():
     courses_start += ["Java", "Agile Development in Java"]
  else:
     courses_end = ["Java", "Agile Development in Java"] + courses_end

  if "python" in job_description.lower():
     courses_start.append("Python")
  else:
     courses_end = ["Python"] + courses_end
  
  courses_end = ["Data Structures and Algorithms"] + courses_end
  
  all_courses = courses_start + courses_end

  for course in all_courses:
     courses += course + ", "
  courses = courses[:-2]

  overleaf += "\n" + pre_courses + courses + post_courses

# Change if statements when learn new languages
def add_languages():
  global sorted_languages
  txt_languages = ""
  for lang in sorted_languages:
    add_txt = ""
    if txt_languages != "":
      add_txt += ", "
    if lang == "html":
      add_txt += "HTML"
    elif lang == "css":
      add_txt += "CSS"
    elif lang == "sql":
      add_txt += "SQL"
    elif lang == "c#":
      add_txt += "C\#"
    else:
      add_txt += lang.capitalize()
    txt_languages += add_txt
  return txt_languages

def add_cicd():
  global cicd
  keywords_cicd = ["continuous integration", "continuous development", "continuous deployment", "ci/cd", "ci", "cd"]
  cicd = False
  for keyword in keywords_cicd:
     if keyword in job_description.lower().split():
        cicd = True
  
  if cicd:
    return r'''\textbf{Continuous Integration / Continuous Deployment (CI/CD)}{: JUnit, Jenkins, Gradle, Git, Jira}\\''' + "\n"
  else:
    return ""

def add_skills():
   global overleaf, job_description
   pre_skills = r'''\section{Technical Skills}
 \begin{itemize}[leftmargin=0.15in, label={}]
    \small{\item{
    '''
   post_skills = r''' \end{itemize}'''
   
   languages = r'''\textbf{Languages}{: ''' + add_languages() + r'''} \\''' + "\n"
   
   cicd = add_cicd()

   if cicd:
    frameworks = r'''\textbf{Frameworks}{: React, Node.js, Firebase, .NET} \\
    }}''' + "\n"
   else:
    frameworks = r'''\textbf{Frameworks}{: React, Node.js, JUnit, Jenkins, Gradle, Firebase, Git, .NET} \\
    }}''' + "\n"
   
   if "ml" in job_description.lower().split() or "ai" in job_description.lower().split() or "machine learning" in job_description.lower() or "artificial intelligence" in job_description.lower() or "keras" in job_description.lower() or "pytorch" in job_description.lower() or "scikit-learn" in job_description.lower():
      machine_learning = r'''\textbf{ML/AI}{: PyTorch, Keras, scikit-learn, distributed computing} \\
    }}''' + "\n"
   else:
      machine_learning = r''''''

   overleaf += "\n" + pre_skills + languages + frameworks + cicd + machine_learning + post_skills

def main(job_description):
    global sorted_languages, overleaf, languages_I_know

    overleaf = ""
    languages_I_know = ["python", "java", "javascript", "sql", "c#", "html", "css"]

    add_format()
    add_header()
    sorted_languages = get_languages(languages_I_know)
    add_education()
    add_skills()
    add_experience()
    add_projects()
    add_activities()  
    load_end()
    return overleaf

@app.route("/greet", methods=["POST", "GET"])
def greet():
  global job_description
  job_description = request.form['name_input']

  overleaf_output = main(job_description)
  text = overleaf_output.split('\n')
  flash(text)
  
  return render_template("index.html", data=text)