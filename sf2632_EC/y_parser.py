__author__='Shi Fan'
import pandas as pd
from yelpapi import YelpAPI

consumer_key = 'MpAU-Y9CTlU0wZ8Hh4cL7Q'
consumer_secret = '5DDgjxYbL4sko3OgYsdTZHo4xvA'
token = 'A3XLZ2RqoxyQBG8VdIQUV1yJjlCh7i34'
token_secret = 'CVQZYNKKk2uZjrE57rzsp1cCrU0'
yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)

activities = ['restaurants','bars','coffee & tea','health & medical','arts & entertainment','fitness & instruction','grocery','education','haircut','boutique']

data = pd.read_csv('nbhds.csv')
locs_mn = data[data['BoroName']=='Manhattan']['EditName'].tolist()
locs_bk = data[data['BoroName']=='Brooklyn']['EditName'].tolist()

def calculate_biz_results(biz,feature):
	rating = 0
	count = 0
	for k in biz:
		if feature=='restaurants':
			try:
				if k['review_count']>500:
					rating += (k['rating']/float(5))*2.5+2.5
				elif k['review_count']<100:
					rating += (k['rating']/float(5))*2.5+(k['review_count']/float(100))*1
				else:
					rating += (k['rating']/float(5))*2.5+((k['review_count']-100)/float(400))*1.5+1
				count += 1
			except:
				continue
		elif feature=='bars':
			try:
				if k['review_count']>300:
					rating += (k['rating']/float(5))*2.5+2.5
				elif k['review_count']<100:
					rating += (k['rating']/float(5))*2.5+(k['review_count']/float(100))*1
				else:
					rating += (k['rating']/float(5))*2.5+((k['review_count']-100)/float(200))*1.5+1
				count += 1
			except:
				continue
		elif feature=='coffee & tea':
			try:
				if k['review_count']>100:
					rating += (k['rating']/float(5))*2.5+2.5
				else:
					rating += (k['rating']/float(5))*2.5+(k['review_count']/float(100))*2.5
				count += 1
			except:
				continue
		else:
			try:
				if k['review_count']>50:
					rating += (k['rating']/float(5))*2.5+2.5
				else:
					rating += (k['rating']/float(5))*2.5+(k['review_count']/float(100))*2.5
				count += 1
			except:
				continue
	if count==0:
		r_avg = 0
	else:
		r_avg = rating/float(count)
	return r_avg

def main():
	d_mn = {}
	d_qn = {}
	d_bk = {}
	for i in activities:
		# Manhattan
		d_mn.setdefault(i,{})
		for j in locs_mn:
			d_mn[i].setdefault(j,0)
			search_results = yelp_api.search_query(term=i,location=j+', Manhattan, NY',radius_filter=1600)
			businesses = search_results.get('businesses')
			d_mn[i][j] = calculate_biz_results(businesses,i)
		# Brooklyn
		d_bk.setdefault(i,{})
		for j in locs_bk:
			d_bk[i].setdefault(j,0)
			search_results = yelp_api.search_query(term=i,location=j+', Brooklyn, NY',radius_filter=1600)
			businesses = search_results.get('businesses')
			d_bk[i][j] = calculate_biz_results(businesses,i)

	df_mn = pd.DataFrame(data=d_mn, index=locs_mn, columns=activities)
	df_bk = pd.DataFrame(data=d_bk, index=locs_bk, columns=activities)
	frames = [df_mn,df_bk]
	df = pd.concat(frames)
	df['PjAreaCode'] = data['PjAreaCode'].tolist()
	df.to_csv('yelp_data.csv')

if __name__ == '__main__':
    main()