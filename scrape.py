import csv
from bs4 import BeautifulSoup

def scrape_channel_data(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    channel_data = []
    for contributor_wrap in soup.find_all('div', class_='contributor-wrap'):
        contributor_name = contributor_wrap.find('div', class_='contributor__name-content').text.strip()
        channel_id = contributor_wrap.find('a', class_='contributor-link')['href'].split('/')[-1]
        social_id = contributor_wrap.find('a', class_='contributor-link')['href'].split('/')[-2]
        channel_data.append((contributor_name, channel_id, social_id))

    return channel_data

if __name__ == "__main__":
    html_file = "Top YouTube Channels (Page 10) _ HypeAuditor YouTube Ranking.html"  # Replace with the path to your HTML file
    channel_data = scrape_channel_data(html_file)

    with open('channel_data10.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Channel Name', 'Channel ID', 'Social ID'])
        writer.writerows(channel_data)

    print("Channel data scraped and saved to channel_data.csv")
