# Copyright (c) Sunlight Labs, 2013, under the terms of the BSD-3 clause
# license.
#
#  Contributors:
#
#    - Paul Tagliamonte <paultag@sunlightfoundation.com>


from pupa.scrape import Jurisdiction

from .people import ColumbusPersonScraper
from .events import ColumbusEventScraper


class Columbus(Jurisdiction):
    jurisdiction_id = 'ocd-jurisdiction/country:us/state:oh/place:columbus/council'

    def get_metadata(self):
        return {'name': 'Columbus City Council',
                'url': 'http://council.columbus.gov/',
                'terms': [{'name': '2013-2014', 'sessions': ['2013'],
                           'start_year': 2013, 'end_year': 2014
                          }],
                'provides': ['people', 'events',],
                'parties': [],  # No parties on the city council
                'session_details': {'2013': {'_scraped_name': '2013'}},
                'feature_flags': [],}

    def get_scraper(self, term, session, scraper_type):
        bits = {
            "people": ColumbusPersonScraper,
            "events": ColumbusEventScraper,
        }
        if scraper_type in bits:
            return bits[scraper_type]

    def scrape_session_list(self):
        return ['2013']
