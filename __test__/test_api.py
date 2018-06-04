import collection.api as pdapi

# test for pd_gen_url
# url = pdapi.pd_gen_url(
#     'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
#     service_key='%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D',
#     # 내꺼
#     # service_key='eaDtt2id%2FMeH098ZuosvnqQTUnsoHN69AvMogeEl41PnXGzzcLH3KmoSj%2FyDuUQInxncUvhcSc1EIyYDIaggSQ%3D%3D',
#     YM='{0:04d}{1:02d}'.format(2012, 1),
#     SIDO='부산광역시',
#     GUNGU='해운대구',
#     RES_NM='부산시립미술관',
#     numOfRows=10,
#     _type='json',
#     pageNo=1)
#
# print(url)

# test for pd_fetch_tourspot_visitor

#for items in pdapi.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
#    print(items)

# test
items = pdapi.pd_fetch_foreign_visitor(100, year=2012, month=7)
print(items)