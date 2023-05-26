# Indeed Web Scraper
Indeed Web Scraper is a script that collects job data for Data Scientists in Barcelona from [indeed.com](https://es.indeed.com) and stores it in a CSV file. This script saves you from having to browse through hundreds of job listings on the website.

This work is part of Assignment 1 of the course "Data Typology and Life Cycle" in the Master's in Data Science program at Universitat Oberta de Catalunya.

## Team Members
This project was carried out by [Joan Prieto](https://github.com/joanPri) and Ricardo Martinez.

## Explanation
In this project, you will find two different scripts, each implementing current scraping methodologies. The script named **"main.py"** collects data from the selected website using requests to make HTTP requests and BeautifulSoup to extract the content of the web page for further processing.

On the other hand, there is another script called **"scrapper.py"** that uses the Selenium methodology to extract data from the web page. Selenium allows for more comprehensive interaction with the web page, enabling the execution of page-specific scripts and performing button clicks. It also relies on HTTP requests and a driver (which varies depending on the browser) for this purpose. The driver acts as a connection to the browser, allowing the web page to be tested.

*Note: The scripts are completely independent, and there is no need to run them simultaneously.*

## Installation
To run the "main.py" script (in Python), you need to install the following libraries:

```python
import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
import re
import time
```

To run the "scrapper.py" script (in Python), you need to install the following libraries:

```python
import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
```

To use Selenium, you need a driver that acts as an interface with the browser. The drivers are located in the "Drivers" folder. In this project, the driver is linked to the Firefox browser, but we also provide drivers for Chrome and Microsoft Edge. You can change one line of code to use the desired browser with its corresponding driver. The drivers are included in the project (in the "drivers" folder).

## Development Environment
We used the Anaconda distribution to carry out the project, which provides the Python package for working with the programming language. Therefore, it is necessary to have Anaconda installed on Windows 10 (we chose this operating system for its ease of use and wide implementation).

## Running the Script (Usage)
To run both scripts provided in this project, you should have the "geckodriver" driver (for the "scrapper.py" script) in the same folder. This driver corresponds to Firefox, which we chose, but you can use another driver (the attached folder includes drivers for Edge and Chrome) to implement the scraper. From the command prompt in Anaconda, navigate to the directory where the file is located and execute the scripts as follows:

```
scrapper.py
main.py
```

Alternatively, you can add `python` before the script names.

In the case of the "main.py" script, as it cannot interact with JavaScript or page scripts, it collects a limited range of data. The script collects data from Indeed and exports the following fields to a CSV dataset:
- Job Title (string): Retrieves the title

 tag of each click card.
- Company (string): Retrieves the tag of the advertising company.
- Description (string): Retrieves the complete description.
- Link (URL)
- Location (in this case, it will be Barcelona or surrounding areas)

In the case of the "scrapper.py" script, as it interacts with JavaScript and scripts, it collects more diverse information, although in smaller quantities due to the limitation mentioned above. It exports the following fields:
- Job Title (string): Retrieves the title tag of each click card.
- Company (string): Retrieves the tag of the advertising company.
- Description (string): Retrieves the complete description.
- Link (URL)
- Location (in this case, it will be Barcelona or surrounding areas)
- Job Description (summary of the offer)
- Publication Date (when it was published)
- Profile - Whether the offer is for junior, senior, or undefined (this field is calculated by searching for these words in the entire content).

We would like to highlight the following points of interest:
- To interact with the elements offered by the selected web page, we used Selenium. When using Selenium instead of Requests, we encountered the challenge of bots detection by websites and access denial due to "hcaptcha." Although we attempted to implement more human-like behavior in our bot (modifying the user agent in the driver options when making requests, handling alert dialogs, etc.), we were only able to scrape the first 5 pages due to these limitations. Therefore, we obtained the total job postings from the first 4 pages.
- In contrast, Requests performs a complete parse of the entire pagination.

## Future Steps
To further explore the world of web scraping, we need to gain a better understanding of how these bot detectors work and implement techniques that more accurately simulate human interaction. It would also be a good idea to add a menu or the possibility to add parameters to the script execution.

## Documentation
If you want to see the description of the assignment, please refer to the [documentation](https://github.com/joanPri/indeed-web-scrapper/tree/main/doc).

## Example Output
To see an example of the job listings exported using the script, click [here](https://github.com/joanPri/indeed-web-scrapper/blob/main/indeedScrap_selenium.csv).

## Summary
In conclusion, the two scripts would be used in different scenarios:
- a) If only parsing the directly rendered web page after an HTTP request is required, the "main.py" script with its methodology is more lightweight than Selenium and provides faster processing.
- b) If dynamic elements, scripts, and JavaScript code need to be executed, Selenium would be the preferred choice despite the aforementioned limitation.
