from flask import Flask ,render_template , url_for ,request
# from flask_sqlalchemy import SQLAlchemy
import requests
import bs4
import re

app=Flask('__name__')
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
# db=SQLAlchemy(app)

# class Todo(db.Mode1):
#     id=db.col

@app.route('/',methods=['POST','GET'])
def index():
    news=[]

    if request.method=='POST':
        topic=request.form['topic']
        if topic=="all":
            res = requests.get('https://inshorts.com/en/read/')
        else:
            res = requests.get('https://inshorts.com/en/read/' + topic)

        soup = bs4.BeautifulSoup(res.text, 'lxml')

        head = soup.find_all(itemprop="headline")

        url = soup.select(".source")

        image=soup.select(".news-card-image")




        for i in range(16):
            print(re.search('(?P<url>https?://[^\s]+)',image[i].get("style") ).group("url"))

            item=dict(title=head[i].getText(),source =url[i].get("href"),image_url=re.search('(?P<url>https?://[^\s]+)',image[i].get("style") ).group("url"))
            news.append(item)
            # news_title.append(head[i].getText())
            # news_url.append(url[i].get("href"))
            # print("\n")
        # return (news_title[2])
        try:
            return render_template('news4u.html',news_topic=topic,all_news=news)
        except:
            return render_template('news4u.html')

    else:
        return render_template('news4u.html')


if __name__=="__main__":
    app.run(debug=True)