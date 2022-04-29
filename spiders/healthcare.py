# -*- coding: utf-8 -*-
from gc import callbacks
import imp
# from lib2to3.pgen2 import driver
from urllib import response
import scrapy
import json
from ..items import HealthcareVacancyItem
# from selenium import webdriver
import requests


class HealthcareSpider(scrapy.Spider):
    # driver = webdriver.Chrome(executable_path=(r"C:\Users\mayur\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe"))
    name = 'healthcare'
    pno = 361
    # allowed_domains = ['https://serpapi.com/search.json?engine']
    
    start_urls = [
        'https://www.shine.com/job-search/google-jobs-in-medical-healthcar'
        ]
    
    # def healthcare_jobs(self,response, count, prev_pno):
    #     items = HealthcareVacancyItem()
    #     jobs =response.css("li.JobsListStyles__newJobListItem")
        
    #     for job in jobs:
    #         company_name = job.xpath("//div[@class='d-flex justify-content-between'/span[@class='d-block mb-xxsm'/text()")
    #         title = job.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "JobDetailsStyles__jobTitle", " " ))]/text()')
    #         location = job.css("span.JobDetailsStyles__newLocationGrey::text").extract()

    #         items['title'] = title
    #         items['company_name'] =company_name
    #         items['location'] = location
            
    #         yield items
            

    #     next_pno=response.xpath(" //ul[@class='css-1ff5hnt']/li/a["+str(count)+"]/text()")
        
    #     if prev_pno == next_pno:   
    #         count+=1
        
    #     next_page = response.xpath(("//ul[@class='css-1ff5hnt']/li/a["+str(count)+"]/@href"))
        
        
    #     if next_page is not None:
    #         yield response.follow(next_page , callback = self.healthcare_jobs) 
        
                

    # def job_details(self,response):
    #     get_url = driver.current_url
    #     added_part = '&filter.SGOCid=0&filter.jobTitleFTS=healthcare'
    #     url = get_url+added_part
    #     count =1
    #     prev_pno=1
    #     yield response.follow(url ,callback = self.healthcare_jobs)
    
    def hospital(self , response):

        items = HealthcareVacancyItem()
        
        company_name = response.css("div.JobDetailWidget_jobCard_cName__qvsdW span::text").extract()
        title = response.css('div.JobDetailWidget_jobDetail_blue__JDzC6 h2::text').extract()
        location = response.css("div.JobDetailWidget_locationIcon__u85a7::text").extract()

        items['title'] = title
        items['company_name'] =company_name
        items['location'] = location
            
        yield items
           
            
        
        
        
        
    def parse(self, response):
    
        # for i in range(31):
        #     if(i == 0):
        #         url = 'https://www.glassdoor.co.in/Job/india-healthcare-jobs-SRCH_IL.0,5_IN115_KO6,16.htm'
        #         yield response.follow(url ,callback = self.healthcare_jobs)
        
        # items = HealthcareVacancyItem()
        # all_companies = response.css("div.css-errlgf")
        
        # for company in all_companies :
            
        #     jobs_page = company.xpath('//div[@class="col-12 col-lg-4 mt-lg-0 mt-std d-flex justify-content-between justify-content-lg-end order-6 order-lg-1"]/a[3]/@href')
        #     yield response.follow(jobs_page , callback = self.job_details)
        items = HealthcareVacancyItem()
        jobs =response.css("div.jobCard_jobCard__jjUmu")
 
        
        for job in jobs:
            
            url = job.css("meta::attr(content)").extract()
            url_str = ''.join(map(str, url))
            length = len(url_str)
            new_url = url_str[:length-2]
            yield response.follow(new_url , callback = self.hospital)
            
        next_page = "https://www.shine.com/job-search/google-jobs-in-medical-healthcar-"+str(HealthcareSpider.pno)
        
        
        if HealthcareSpider.pno <= 400:
            HealthcareSpider.pno +=1
            yield response.follow(next_page , callback =self.parse)  
        
        
            
            
            # company_name = job.css("h2::text").extract()
            # title = job.css('span.screen-reader-text::text').extract()
            # location = job.css("div.jobCard_locationIcon__zrWt2::text").extract()

            # items['title'] = title
            # items['company_name'] =company_name
            # items['location'] = location
            
            # yield items
        
        # next_page = 'https://www.glassdoor.co.in/Job/india-healthcare-jobs-SRCH_IL.0,5_IN115_KO6,16_IP'+ str(HealthcareSpider.pno) + '.htm?includeNoSalaryJobs=true&pgc=AB4AAoEAPAAAAAAAAAAAAAAAAdAFh7UAdgEDAQoWBxAGbIUMRA10LFTcj4vCAiAVpVdNy7rIc7gyop4cwV7zn7XGabujATOEDPVOWgw6VPAfOlN8tYJt2HSlnFR4%2FZI1JneWABi1EoBBUXMKQFD33AFVJ32pjTzh%2B6AbcBZU9NRfz976Gn4t117PhiisoTUAAA%3D%3D'   
         
        # if HealthcareSpider.pno <= 30:
        #     HealthcareSpider.pno +=1
        #     yield response.follow(next_page , callback =self.parse)    
        # next_page = response.xpath("//div[@class=") 
