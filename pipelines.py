# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#-------------------INSTRUCTIONS--------------------------#
# 1. Change Table Names to Desired Table Names
    # Functions: create_table(), udpate_table()
# 2. Change Database Location if Desired create_connection()
# 3. Conditional Databasing at the end update_table() commented out
# 4. Change the amount of item entries in the table
# 5. Change the names of the item entries


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class TemplateSpiderPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host     = 'localhost',
            user     = 'root',
            passwd   = 'Y5d7fp32!@',
            database = '21Nov2022'
        )
        self.cursor = self.conn.cursor()
      
    def create_table(self):
        #--------Main Team Table-----------#
        self.cursor.execute('DROP TABLE IF EXISTS weather')
        self.cursor.execute('''CREATE TABLE weather (low_temp text, high_temp text, day_of_month text)''')

        
        #---------Top Stats on Each Team--------#
    
        self.conn.commit()


    def process_item(self, item, spider):                  # Updates The Database
        self.update_table(item)
        return item

    def update_table(self, item):                            # Updates The Table
        self.cursor.execute('INSERT INTO weather VALUES (%s,%s, %s)', (item['low_temp'], item['high_temp'], item['day_of_month']))

        self.conn.commit()
    #---------More Advances Conditional Parsing USEFUL--------------#
        # item_group1 = ['', '', '', '']                     #
        # item_group2 = ['', '', '']                         # Different Yield Item Statements

        #--------------Conditional Statement to Check Which Database to Update-----------------------#
        # if team_list[0] in item.keys(): # No Keys Are Shared Just Check if First Item Matches
            # self.cursor.execute('INSERT INTO table_name VALUES (%s,%s)', (item['item_1'], item['item_2']))
        # elif stats_list[0] in item.keys(): # 
            # self.cursor.execute('INSERT INTO table_name2 VALUES (%s,%s)', (item['item_3'], item['item_4']))
        # else:
            # pass

        # self.conn.commit()

