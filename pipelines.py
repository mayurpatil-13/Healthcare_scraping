# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class HealthcareVacancyPipeline(object):
    def __init__(self):
        self.create_conn()
        self.create_table()
        
    def create_conn(self):
        self.conn = sqlite3.connect('new17_db.db')
        self.cur = self.conn.cursor()
        
    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS data_tb""")
        self.cur.execute("""create table data_tb(title text,
        company_name text,
        location text  
        )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        self.cur.execute("""insert into  data_tb values (?,?,?)""",
                         (item['title'][0] ,
                         item['company_name'][0],
                         item['location'][0]) )

        self.conn.commit()
