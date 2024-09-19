Purpose of data collection
    The program collects a list of 500 books from The Complete 500 booklist from OCLC, a global library organisation that provides shared technology services, original research, and community programs for its membership and the library community at large. This list is based on how many libraries have a copy of a book on their selves. The list of books collected are identified as the top 500 timeless novels, those found in thousands of libraries around the world - using WorldCat, the world's largest database of library materials. The list was originally published in 2024. The program uses the list to randomly pick out 5 books as a Monthly Reading List for the user.

Data sources and robots.txt 
url = https://www.oclc.org/en/worldcat/library100/top500.html
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

Respect the robots (url.com/robots.txt)
    The program collects a list of book titles and author names from The Complete 500 List. There is no breach of scrapping disallowed content.

Limit scraping to avoid disruption
    The information scrapped from the Complete 500 List is public content.
    
Data handling and privacy
    No user data collected.

Data usage
    Collected data is for educational/research purposes only

