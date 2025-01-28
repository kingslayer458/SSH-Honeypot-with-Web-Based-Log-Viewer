# SSH-Honeypot-with-Web-Based-Log-Viewer
\documentclass{article}
\usepackage{hyperref}

\title{SSH Honeypot with Web-Based Log Viewer}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle

\section*{Introduction}
This repository contains a lightweight SSH honeypot implemented in Python using the \texttt{paramiko} library. It also includes a Flask-based web application for monitoring logs in real-time.

\section*{Features}

\subsection*{SSH Honeypot}
\begin{itemize}
    \item Simulates an SSH server to log unauthorized access attempts and commands executed by attackers.
    \item Runs on a custom port (default: \texttt{2222}).
    \item Captures and logs:
    \begin{itemize}
        \item Client IP address.
        \item Commands sent by the client.
    \end{itemize}
\end{itemize}

\subsection*{Web-Based Log Viewer}
\begin{itemize}
    \item Real-time display of logs via a Flask-based web interface.
    \item Automatically updates logs without requiring a page refresh.
    \item Simple and clean user interface.
\end{itemize}

\section*{Getting Started}

\subsection*{Prerequisites}
\begin{itemize}
    \item Python 3.7 or higher.
    \item Installed Python libraries: \texttt{paramiko}, \texttt{flask}.
\end{itemize}

Install the required dependencies:
\begin{verbatim}
pip install paramiko flask
\end{verbatim}

\subsection*{Running the Honeypot}
Start the SSH honeypot:
\begin{verbatim}
python ssh_honeypot.py
\end{verbatim}

Logs will be saved in \texttt{ssh_honeypot.log} in the same directory.

\subsection*{Running the Web-Based Log Viewer}
Start the Flask app:
\begin{verbatim}
python app.py
\end{verbatim}

Open your browser and navigate to:
\begin{verbatim}
http://<server-ip>:5000/
\end{verbatim}

\section*{File Structure}
\begin{verbatim}
.
├── ssh_honeypot.py        # SSH Honeypot implementation
├── app.py                 # Flask-based log viewer
├── ssh_honeypot.log       # Log file created by the honeypot (auto-generated)
├── templates/
│   └── index.html         # HTML template for the web interface
└── README.md              # Project description and setup guide
\end{verbatim}

\section*{Security Considerations}
\begin{itemize}
    \item \textbf{Isolate the honeypot}: Run it in a sandboxed environment, such as a virtual machine or container.
    \item \textbf{Legal compliance}: Verify that deploying a honeypot is legal in your region.
    \item \textbf{Access control}: Restrict access to the web interface to authorized users only.
\end{itemize}

\section*{Planned Improvements}
\begin{itemize}
    \item Add authentication to the web-based interface.
    \item Implement WebSocket-based real-time log updates.
    \item Add support for more advanced SSH server simulations.
\end{itemize}

\section*{License}
This project is licensed under the MIT License. See the \texttt{LICENSE} file for details.

\end{document}


