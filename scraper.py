#!/usr/bin/python

import urllib2
import re
import datetime

re_posting = re.compile(r'(?P<cl_posting_item><p class="srch row" data-pid="\d+">.*?</p>)', re.DOTALL)
re_pid = re.compile(r'data-pid="(?P<pid>\d+)"', re.DOTALL)
re_url = re.compile(r'<a href="(?P<url>.*?.html)">', re.DOTALL)
re_date = re.compile(r'<span class="itemdate">(?P<month>[A-Z][a-z]{2}) (?P<day>\d+)</span>', re.DOTALL)
re_title = re.compile(r'<a href="http://.*?.html">(?P<title>.*?)</a>', re.DOTALL)
re_price = re.compile(r'<span class="itemprice">\$(?P<price>\d+)</span>', re.DOTALL)
re_location = re.compile(r'<span class="itempnr">.*?<small>.*?\((?P<location>.*?)\).*?</small>', re.DOTALL)

raw_string = '<p class="srch row" data-pid="3757140411"> <span class="i">&nbsp;</span> <span class="title1"> <span class="pl"> <small><span class="itemdate">Apr 21</span></small> <a href="http://sfbay.craigslist.org/eby/tid/3757140411.html"> Save here with discount Coachella tickets </a> </span> </span> <span class="title2"> <span class="itempnr">  <span class="itempp"></span> <small> (alameda)</small> </span>  <small class="gc"><a href="/tid/" data-cat="tid">tickets - by dealer</a></small> <span class="itempx"> <span class="p"> </span></span> </span> <br class="c"> </p>'

def extract_posting_info(posting_list):
   # structure in {pid: {info1:value, info2:value}}
   posting_map = {}
   for posting in posting_list:
       posting_info_map = {}
       pid = extract_pid(posting, posting_info_map)
       extract_url(posting, posting_info_map)
       extract_date(posting, posting_info_map)
       extract_title(posting, posting_info_map)
       extract_price(posting, posting_info_map)
       extract_location(posting, posting_info_map)

       posting_map[pid] = posting_info_map

   return posting_map

def extract_pid(posting, posting_info_map):
    pid = re_pid.findall(posting)
    if pid:
        posting_info_map['pid'] = pid[0]
        return pid[0]

def extract_url(posting, posting_info_map):
    url = re_url.findall(posting)
    if url:
        posting_info_map['url'] = url[0]
        return url[0]

def extract_date(posting, posting_info_map):
    date = re_date.findall(posting)
    if date:
        posting_info_map['month'] = date[0][0]
        posting_info_map['day'] = date[0][1]
        return (date[0][0], date[0][1])

def extract_title(posting, posting_info_map):
    title = re_title.findall(posting)
    if title:
        posting_info_map['title'] = title[0]
        return title[0]

def extract_price(posting, posting_info_map):
    price = re_price.findall(posting)
    if price:
        posting_info_map['price'] = price[0]
        return price[0]

def extract_location(posting, posting_info_map):
    location = re_location.findall(posting)
    if location:
        posting_info_map['location'] = location[0]
        return location[0]

def match_posting(string):
    match_list = re_posting.findall(raw_string)
    return match_list

def write_html(filename, html):
    f = open(filename, 'w')
    f.write(html)
    f.close()

def find_postings(url):
    f = urllib2.urlopen(url, 'r')
    html = f.read()
    f.close()

    #print 'writing html'
    #write_html('html.txt', html)
    #raw_input()

    match_list = re_posting.findall(html)

    return match_list


def main():
    url = 'http://sfbay.craigslist.org/search/tia?zoomToPosting=&query=nicky+romero&srchType=A&minAsk=&maxAsk='

    print match_posting(raw_string)
    print find_postings(url)

if __name__ == '__main__':
    main()
