from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
# from django.db import models
from .models import Article


def find_article():
    url = 'https://medium.com/blockchain'
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(r).read()
    soup = BeautifulSoup(html, 'html.parser')
    stories = soup.find_all('div', {'class': [
        'col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size6of12',
        'col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size4of12']})
    for story in stories:
        title = story.find('h3').text if story.find('h3') else '-'
        description = story.find('div', {
            'class': 'u-fontSize18 u-letterSpacingTight u-lineHeightTight u-marginTop7 u-textColorNormal u-baseColor--textNormal'}).text if story.find(
            'div', {
                'class': 'u-fontSize18 u-letterSpacingTight u-lineHeightTight u-marginTop7 u-textColorNormal u-baseColor--textNormal'}) else '-'
        slug = story.find('a')['href'].split('/')[-1]
        author = story.find('a', {
            'class': 'ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken'})[
            'href'].split('@')[-1]
        story_url = story.find('a')['href']
        story_page = Request(story_url, headers={'User-Agent': 'Mozilla/5.0'})
        story_html = urlopen(story_page).read()
        story_soup = BeautifulSoup(story_html, 'html.parser')
        sections = story_soup.find_all('section')
        for section in sections:
            body = section.find('p')
            tags = section.find('p')

        # my_user = MyUser(username=author)
        # my_user.save()
        # my_user_profile = Profile(user=my_user.id)
        # my_user_profile.save()
        Article.objects.create(
            slug=slug,
            title=title,
            description=description,
            body=body,
            # author=author,
            # author=models.ForeignKey(my_user_profile, default=1, on_delete=models.SET_DEFAULT),
            # tags=tags
        )
        # Article.tags.add(tags)
        sleep(5)
        return 'done!!!!'