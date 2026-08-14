# Lead Triage Console

A web-based lead qualification and triage application built with HTML, CSS, JavaScript, and Flask.

The application allows users to upload lead data from a CSV file, clean and analyze the data, identify duplicate or invalid records, score leads based on business criteria, and analyze lead intent using AI.

## Features

- Upload lead data through CSV files
- Automatically clean and normalize lead information
- Detect duplicate leads
- Validate lead information
- Score leads based on:
  - Company size
  - Monthly budget
  - Job title
  - Buying intent
- Identify potentially disqualified leads
- Generate explanations for lead scores
- AI-powered analysis of lead notes
- Keyword-based fallback when AI analysis is unavailable
- Dashboard for reviewing qualified and disqualified leads

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- Flask
- Anthropic API
- Papa Parse

## Project Structure

```text
lead-triage-console/
│
├── static/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md