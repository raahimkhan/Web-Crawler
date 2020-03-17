
# Importing libraries
from bs4 import BeautifulSoup
import requests

# Some global lists
my_list = []
my_list2 = []
x = my_list2


def request(site):  # This function requests a web page
    req = requests.get(site)  # Built in function in requests library to ping a website for information
    return req


def crawler(site):   # This function takes a starting URL and an empty list as inputs
    output = request(site)
    extract = output.text  # output.text basically extracts all text from the provided URL
    components = BeautifulSoup(extract, "html.parser")  # it breaks the extracted data into its components

    for k in components.findAll('a'):
        k = str(k.get('href'))
        if k in my_list:  # If link already present then move to next link
            continue

        if 'http' not in k:  # If link does not start with http then include http
            k = str(site) + '/' + str(k)

        if 'mailto:' in k:  # Don't crawl mailto
            continue

        my_list.append(k)  # Append the final link in list

    x = list(dict.fromkeys(my_list))  # Removes duplicate links
    for links in x:  # Links inside my_list2 after removing duplicate links
        with open('Crawler.html', 'a') as f:  # Write links to html file
            f.write(links)
            f.close()
        print(links)

    return


# Main Program
if __name__ == "__main__":
    print("My First Web Crawler")
    print("Enter website for example http://www.carameltechstudios.com")
    print(" ")
    website = input("Enter site :  ")
    crawler(website)
    for i in range(1, (len(my_list))):
        link = str(my_list[i])
        crawler(link)

    for contents in x:  # Links inside my_list2 after removing duplicate links
        with open('Crawler.html', 'a') as f:  # Write links to html file
            f.write(links)
            f.close()
        print(contents)
