import couchdb
from scrapy.conf import settings
from scrapy import log
import datetime

class CouchDBPipeline(object):
    def __init__(self):
        couch = couchdb.Server(settings['COUCHDB_SERVER'])
        self.db = couch[settings['COUCHDB_DB']]

    def process_item(self, item, spider):
        data = {}
        for key in item.keys():
            if key in settings['COUCHDB_IGNORE_FIELDS']:
                continue
            elif isinstance(item[key], datetime.datetime):
                data[key] = item[key].isoformat()
            else:
                data[key] = item[key]
            #Throw exception if unknow type
        data['_id'] = data[settings['COUCHDB_UNIQ_KEY']]
        try:
            old = self.db[data['_id']]
            data['_rev'] = old['_rev']
        except couchdb.http.ResourceNotFound:
            change = True

        #Only save the document if new content
        if data.has_key('_rev'):
            change = False
            for key in data.keys():
                if not old.has_key(key):
                    change = True
                else:
                    if old[key] != data[key]:
                        change = True
        if change:
            self.db.save(data)
            log.msg("Item wrote to CouchDB database %s/%s" %
                    (settings['COUCHDB_SERVER'], settings['COUCHDB_DB']),
                    level=log.DEBUG, spider=spider)  
        return item
