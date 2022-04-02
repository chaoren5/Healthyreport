import time
#import db
import logging
from report import report

logging.basicConfig(filename='health_report.log',level=logging.INFO)

if __name__ == '__main__':
    while True:
        id = '14ac58ff-8508-4601-a16a-123ad0bb59bd'
        report(id)
        time.sleep(86400)
# Maybe I can make a seesion list, once someone need this script to auto-report, I can simply add
# his session into my session list, and Python script will traverse the list, to post each session id
# to complete reports.