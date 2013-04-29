#!/usr/bin/python

import scraper

raw_string = '<p class="srch row" data-pid="3757140411"> <span class="i">&nbsp;</span> <span class="title1"> <span class="pl"> <small><span class="itemdate">Apr 21</span></small> <a href="http://sfbay.craigslist.org/eby/tid/3757140411.html"> Save here with discount Coachella tickets </a> </span>  </span> <span class="title2"> <span class="itempnr">  <span class="itempp"><span class="itemprice">$80</span></span> <small> (alameda)</small> </span> <small class="gc"><a href="/tid/" data-cat="tid">tickets - by dealer</a></small> <span class="itempx"> <span class="p"> </span></span> </span> <br class="c"> </p>'

def test_match_posting(posting):
    match_list = scraper.re_posting.findall(posting)
    print 'test_match_posting result: ', match_list

    if match_list:
        print 'PASSED'
    else:
        print 'FAILED'

def test_extract_pid(posting):
    pid = scraper.extract_pid(posting, {})
    print 'test_extract_pid result: ', pid
    
    if pid:
        print 'PASSED'
    else:
        print 'FAILED'

def test_extract_url(posting):
    url = scraper.extract_url(posting, {})
    print 'test_extract_url result: ', url

    if url:
        print 'PASSED'
    else:
        print 'FAILED'

def test_extract_date(posting):
    date = scraper.extract_date(posting, {})
    print 'test_extract_date result: ', date

    if date:
        print 'PASSED'
    else:
        print 'FAILED'
    # remember that date is a tupe (m, d)

def test_extract_title(posting):
    title = scraper.extract_title(posting, {})
    print 'test_extract_title result: ', title

    if title:
        print 'PASSED'
    else:
        print 'FAILED'

def test_extract_price(posting):
    price = scraper.extract_price(posting, {})
    print 'test_extract_price result: ', price

    if price:
        print 'PASSED'
    else:
        print 'FAILED'

def test_extract_location(posting):
    location = scraper.extract_location(posting, {})
    print 'test_extract_location result: ', location

    if location:
        print 'PASSED'
    else:
        print 'FAILED'

def test_extract_posting_info(postings):
    posting_info = scraper.extract_posting_info(postings)
    print 'test_extract_posting_info result: ', posting_info

    if posting_info:
        print 'PASSED'
    else:
        print 'FAILED'


def main():
    test_match_posting(raw_string)
    test_extract_pid(raw_string)
    test_extract_url(raw_string)
    test_extract_date(raw_string)
    test_extract_title(raw_string)
    test_extract_price(raw_string)
    test_extract_location(raw_string)
    test_extract_posting_info([raw_string])

if __name__ == '__main__':
    main()
