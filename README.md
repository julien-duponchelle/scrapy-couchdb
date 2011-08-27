Description
===========
It's a pipeline which allow you to store scrapy items in CouchDB database.

Install
=======
   pip install "CouchDB"

Configure your settings.py:
----------------------------
    ITEM_PIPELINES = [
      'scrapycouchdb.CouchDBPipeline',
    ]


    COUCHDB_SERVER = 'http://192.168.84.84:5984/'
    COUCHDB_DB = 'offers'
    COUCHDB_UNIQ_KEY = 'uuid'
    COUCHDB_IGNORE_FIELDS = ['visit_id', 'visit_status']


Changelog
=========
0.1
Initial version

Licence
=======
Copyright 2011 Julien Duponchelle

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
