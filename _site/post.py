import os
os.chdir('/home/rohan/RohanMishra97.github.io/_posts')
date = raw_input('Input Date in form of mm-dd- ')
title = raw_input('Input Title- ')
category = raw_input('Input category- ')
writer=raw_input('Input Writer- ')
time = raw_input('Input reading time- ')
filename = '2016-'+date+'-'+title.replace(' ','-')+'.md'
page = open(filename.lower(),'wb')
page.write('---\n')
page.write('layout: post\n')
page.write('title: ' + title+'\n')
page.write('date: 2016-'+ date + ' 20:30:00'+'\n')
page.write('category: '+category+'\n')
page.write('tags: '+category.lower()+'\n')
page.write('image: /assets/article_images/'+title.replace(' ','-').lower()+'.jpg\n')
page.write('image2: /assets/article_images/'+title.replace(' ','-').lower()+'.jpg\n')
page.write('author: "'+writer+'"\n')
page.write('---\n')
page.write('<h3>'+title+'</h3>\n')
page.write('(<i>'+category+','+time+' minute read</i>)\n')



