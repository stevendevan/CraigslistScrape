HTTP_STUFF = 'https://'
REGION = 'losangeles'
CRAIGSLIST_DOMAIN = '.craigslist.org/'
CRAIGSLIST_SEARCH_PAGE = 'search/'
CRAIGSLIST_CATEGORY = 'mcy'
STARTING_POST_PARAMETER = '?s='
SEARCH_OPTIONS = ''
POSTS_PER_PAGE = 120

class url_builder():
  def __init__(self):
    self.starting_post_num = 0

  def get_url(self):
    return HTTP_STUFF + REGION + CRAIGSLIST_DOMAIN + CRAIGSLIST_SEARCH_PAGE + self.get_category() + \
           self.get_start_post_param() + self.get_filter_params()

  def get_category(self):
    return CRAIGSLIST_CATEGORY

  def get_start_post_param(self):
    return STARTING_POST_PARAMETER + str(self.starting_post_num)

  def get_filter_params(self):
    return SEARCH_OPTIONS
