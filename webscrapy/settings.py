# -*- coding: utf-8 -*-

# Scrapy settings for webscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'webscrapy'

SPIDER_MODULES = ['webscrapy.spiders']
NEWSPIDER_MODULE = 'webscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'webscrapy.middlewares.WebscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'webscrapy.middlewares.mySpiderMiddleware':400,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'webscrapy.pipelines.RedisPipeline': 1,
   'webscrapy.pipelines.CsvPipeline': 2,
   'webscrapy.pipelines.XiuxiuMoivePipline': 3,
   'webscrapy.pipelines.Rong360Pipline': 4,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_LEVEL = 'DEBUG'
cookies={
        'bid':'_1Nu-ZxaERY',
        'll':'108296',
        '_vwo_uuid_v2':'FC2987368160BC790B957D3969B557E5|cd3bf9c623ec1cf6be935cc3829aca42',
        '__utma':'30149280.360979357.1510109357.1510109357.1510116222.2',
        '__utmc':'30149280',
        '__utmz':'30149280.1510109357.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
        'ue':'470109166@qq.com',
        'push_noty_num':'0',
        'push_doumail_num':'0',
        'ap':'1',
        'ps':'y',
        '_pk_ref.100001.8cb4':'%5B%22%22%2C%22%22%2C1511765952%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DfyvehqjjI9qYyhd7ZfrL-sgOVBMKo9cqjwsqea8seyi%26ck%3D5724.2.111.146.149.173.142.244%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26wd%3D%26eqid%3Df25bfd55000087b9000000055a1bb7b8%22%5D',
        'dbcl2':'53824705:yXWChHmMeFI',
        'ck':'1_qV',
        '_pk_id.100001.8cb4':'c511dfb7abd8b1a0.1510291447.3.1511765972.1510549766.',
        '_pk_ses.100001.8cb4':'*'
    }
headers={
        'User-Agent':USER_AGENT
    }
INDEX=0




#test
