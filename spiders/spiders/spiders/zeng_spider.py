# -*- coding:utf-8 -*-
import os,sys
import re
import scrapy
from bs4 import BeautifulSoup
from spiders.items import StarSpidersItem
t = open('test.txt','w')
database_noblog = ['url', 'chinese_name', 'english_name', 'used_name', 'nation', 'location', 'birthday', 'birthplace', 'height', 'weight', 'bloodType', 'constellation', 'graduateSchool', 'profession', 'company', 'representative', 'relatedStar']
database_withblog = ['url', 'chinese_name', 'english_name', 'used_name', 'nation', 'location', 'birthday', 'birthplace', 'height', 'weight', 'bloodType', 'constellation', 'graduateSchool', 'profession', 'company', 'representative', 'microblog' ,'relatedStar']
class TestSpider(scrapy.Spider):
	name = "test"

	start_urls = ["http://www.ijq.tv/mingxing/14664762343661.html"]

	def parse(self, response):
		soup = BeautifulSoup(response.body_as_unicode(),"lxml")
		details = soup.find(id='v-details-list').find_all('p')
		item = StarSpidersItem()
		item['url'] = response.url
		for detail in details:
			pair =  detail.getText().split(u'：')
			first = pair[0].replace('\xc2\xa0','').replace(u'　','')
			second = pair[1]
			if u'《' in second:
				second = '_'.join(pair[1].replace(u'《',' ').replace(u'》',' ').split())
			if u'中文名' == first:
				item['chinese_name'] = second
				print u'中文名'
			if u'英文名' == first:
				item['english_name'] = second
				print u'英文名'
			if u'曾用名' == first:
				item['used_name'] = second
				print u'曾用名'			
			if u'民族' == first:
				item['nation'] = second
				print u'民族'
			if u'国家地区' == first:
				item['location'] = second
				print u'国家地区'
			if u'出生日期' == first:
				item['birthday'] = second
				print u'出生日期'
			if u'出生地' == first:
				item['birthplace'] = second
				print u'出生地'
			if u'身高' == first:
				item['height'] = second
				print u'身高'
			if u'体重' == first:
				item['weight'] = second
				print u'体重'			
			if u'血型' == first:
				item['bloodType'] = second
				print u'血型'
			if u'星座' == first:
				item['constellation'] = second
				print u'星座'
			if u'毕业院校' == first:
				item['graduateSchool'] = second
				print u'毕业院校'
			if u'职业' == first:
				item['profession'] = second
				print u'职业'
			if u'经纪公司' == first:
				item['company'] = second
				print u'经纪公司'
			if u'微博' == first:
				item['microblog'] = second
				print u'微博'			
			if u'代表作' == first:
				item['representative'] = second
				print u'代表作'
			if u'相关明星' == first:
				item['relatedStar'] = second
				print u'相关明星'
		summary = soup.find(id='v-summary').find_all('div',id='hutia')
		item['personal'] = u''
		if summary:
			item['personal'] = summary[0].getText()
		return item
		# if len(details) == 16:
		# 	for x in xrange(16):
		# 		content = details[x].getText().split(u'：')[1]
		# 		if u'《' in content:
		# 			content = '_'.join(content.replace(u'《',' ').replace(u'》',' ').split())
		# 		print database_noblog[x]
		# 		item[database_noblog[x]] = content
		# 		t.write(content + '\n')
		# 	item['microblog'] = u''
		# elif len(details) == 17:
		# 	for x in xrange(17):
		# 		t.write(details[x].getText() + '\n')
		# 		content = details[x].getText().split(u'：')
		# 		first = content[0].replace('\xc2\xa0','').replace(u'　','')
		# 		second = u''
		# 		if first == u'微博':
		# 			second = details[x].find('a').get('href')
		# 		else:
		# 			second = content[1]
		# 		item[database_withblog[x]] = second
		# 		#t.write(second + '\n')
		# summary = soup.find(id='v-summary').find_all('div',id='hutia')
		# if summary:
		# 	item['personal'] = summary[0].getText()
		# 	#t.write(summary[0].getText() + '\n')
		# item['relatedStar'] = u'unkown'
		# return item



		# for detail in details:
		# 	pair =  detail.getText().split(u'：')
		# 	first = pair[0].replace('\xc2\xa0','').replace(u'　','')
		# 	second = pair[1]
		# 	if u'《' in second:
		# 		second = '_'.join(pair[1].replace(u'《',' ').replace(u'》',' ').split())
		# 	if u'中文名' == first:
		# 		print u'中文名'
		# 	if u'英文名' == first:
		# 		print u'英文名'
		# 	t.write(first + ',' + second + '\n')

	# 诗词页面分析
	# "http://www.shicimingju.com/chaxun/list/20697.html"
	# def parse(self, response):
	# 	soup = BeautifulSoup(response.body_as_unicode(),"lxml")
	# 	main = soup.find(id='middlediv')	
	# 	jjzz = main.find(class_='jjzz').find_all('a')
	# 	category = main.find(class_='listscmk')
	# 	if category:
	# 		categories = category.find_all('a')
	# 		category = u''
	# 		for cate in categories:
	# 			category = category + cate.getText() + '_'
	# 	else:
	# 		category = u''
	# 	content = main.find(class_='shicineirong')
	# 	shangxi = main.find(class_='shangxi')
	# 	if shangxi and shangxi.find('h3').getText() == u'作品赏析':
	# 		shangxi = shangxi.getText().strip().replace('\xc2\xa0','')[4:-96]
	# 	else:
	# 		shangxi = u''

	# 	item = PoemSpidersItem()
	# 	item['name'] = main.find('h2').getText()[1:-1]
	# 	item['dynasty'] = jjzz[0].getText()
	# 	item['poet'] = jjzz[1].getText()
	# 	item['category'] = category
	# 	item['content'] = content.getText()
	# 	item['shangxi'] = shangxi
	# 	return item

	# 	# print 'title = ', main.find('h2').getText()[1:-1]
	# 	# print 'dynasty = ', jjzz[0].getText()
	# 	# print 'poet = ', jjzz[1].getText()
	# 	# print 'category = ', category
	# 	# print 'content = ', content.getText()
	# 	# print 'shangxi = ', shangxi.getText()[:-97]
		


