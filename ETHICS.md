Purpose of Data Collection
The program gathers a list of 500 books from The Complete 500 Booklist, curated by OCLC, a global library organization that offers shared technology services, original research, and community programs to its members and the wider library community. This list is based on the number of libraries that hold copies of each book. Identified as the top 500 timeless novels, these books are found in thousands of libraries worldwide, according to WorldCat, the world's largest database of library materials. Originally published in 2024, the program uses this list to randomly select 5 books for a Monthly Reading List, providing users with curated literary recommendations.

Data Sources and robots.txt Compliance
URL: https://www.oclc.org/en/worldcat/library100/top500.html
javascript
Copy code
User-agent: *
Crawl-Delay: 5
Disallow: */contacts/all-contacts.*.html$
Disallow: */contacts/all-contacts/us-sales.*.html$
Disallow: */member-stories.*.html$
Disallow: */services/a-z.*.html$
Disallow: */services/a-z/*
Disallow: */developer/gallery.*.en.html$
Disallow: */developer/news.*.en.html$
Disallow: */developer/develop/web-services.*.en.html$

User-agent: two
Disallow: /
SITEMAP: https://www.oclc.org/sitemap.xml

Adherence to Robots.txt
The program strictly follows the guidelines specified in the robots.txt file to ensure no restricted content is scraped. Only publicly accessible book titles and author names from The Complete 500 List are collected, ensuring compliance with data access rules.

Scraping Limitations to Prevent Disruption
The information retrieved from The Complete 500 List consists of publicly available content. The scraping process is minimal and designed to avoid any disruption to the source website.

Data Handling and Privacy
No user data is collected in the process.

Data Usage
The collected data is solely used for educational and research purposes.
