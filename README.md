# PDF Text Percentage Checker and Mover

This Python script calculates the percentage of a PDF document that is covered by searchable text. If the text percentage is below a specified threshold, it moves the file to a specified destination folder. It can be useful for automatically identifying scanned PDFs and organizing them separately for further processing.

## Overview

Many PDF documents contain searchable text, making it easy to extract information programmatically. However, some PDFs may consist mainly of scanned images, making text extraction difficult or impossible. This script helps in identifying such scanned PDFs by calculating the percentage of the document that contains searchable text. If the text percentage is below a specified threshold, it moves the file to a designated folder for further inspection or processing.

## Requirements

- Python 3.x
- PyMuPDF (fitz) library