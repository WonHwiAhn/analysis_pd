import collection
import pandas as pd
import urllib
import os
import json
from urllib.request import Request, urlopen
from .api import api

RESULT_DIRECTORY = '__results__/crawling'

def preprocess_tourspot_visitor(item):
    print('####################', type(item))
    # count_locas
    if 'csNatCnt' not in item:
        item['count_locals'] = 0
    else:
        item['count_locals'] = item['csNatCnt']
        del item['csNatCnt']

    # count_foreigner
    if 'csForCnt' not in item:
        item['count_foriegner'] = 0
    else:
        item['count_foriegner'] = item['csForCnt']
        del item['csForCnt']

    # tourist_spot
    if 'resNm' not in item:
        item['tourisr_spot'] = ''
    else:
        item['tourisr_spot'] = item['resNm']
        del item['resNm']

    # date
    if 'ym' not in item:
        item['sido'] = ''
    else:
        item['date'] = item['ym']
        del item['ym']

    # restrict1
    if 'sido' not in item:
        item['date'] = ''
    else:
        item['restrict1'] = item['sido']
        del item['sido']

    # restrict2
    if 'gungu' not in item:
        item['restrict2'] = ''
    else:
        item['restrict2'] = item['gungu']
        del item['gungu']
    if 'addrCd' in item:
        del item['addrCd']
    if 'rnum' in item:
        del item['rnum']

def preprocess_foreign_visitor(data):
    print('&&&&&&&&&&&&&', type(data))
    # country_code
    if 'natCd' not in data:
        data['country_code'] = 0
    else:
        data['country_code'] = data['natCd']
        del data['natCd']

    # country_name
    if 'natKorNm' not in data:
        data['country_name'] = ''
    else:
        data['country_name'] = data['natKorNm']
        del data['natKorNm']

    # date
    if 'ym' not in data:
        data['date'] = ''
    else:
        data['date'] = data['ym']
        del data['ym']

    # visit_count
    if 'num' not in data:
        data['visit_count'] = 0
    else:
        data['visit_count'] = data['num']
        del data['num']

    if 'ed' in data:
        del data['ed']

    if 'edCd' in data:
        del data['edCd']

    if 'rnum' in data:
        del data['rnum']


def crawling_foreign_visitor(country, start_year, end_year):
    print('12846y3rhc0238rnc2038c0238rcn0283')
    filename = '%s/%s_foreignvisitor_2017_2017.json' % (RESULT_DIRECTORY, country)
    results = []

    for j in range(0, end_year-start_year+1):
        for i in range(1, 13):
            # 날짜 만들기 (근데 api이용하는거라 필요없었음.)
            # YM = str(start_year+j) + ("%02d" % i)
            # print(j, i, YM)

            item = api.pd_fetch_foreign_visitor(country[1], year=start_year + j, month="%02d" % i)
            preprocess_foreign_visitor(item)

            results.append(item)


            # for infos in api.pd_fetch_foreign_visitor(country[1], year=start_year+j, month="%02d" % i):
            #     print('###########', type(infos))
            #     # preprocess_foreign_visitor(infos)
            #     for info in infos:
            #         preprocess_foreign_visitor(info)
            #
            #     results += infos

            # for infos in api.pd_fetch_foreign_visitor(country[1], year=start_year+j, month="%02d" % i):
            #     print('=======================')
            #     print(infos)
            #     print('=======================')
            #     #for info in infos:
            #     preprocess_foreign_visitor(infos)
            #
            #     results += infos

    # save results to file
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

    return filename


def crawling_tourspot_visitor(district, start_year, end_year):
    filename = '%s/tourspot_visit.json' % (RESULT_DIRECTORY)
    results = []

    print('====')
    count = (end_year-start_year+1) * 12
    # print(count)
    # if count == 0:
    #    count = 12

    for j in range(0, end_year-start_year+1):
        for i in range(1, 13):
            # 날짜 만들기 (근데 api이용하는거라 필요없었음.)
            # YM = str(start_year+j) + ("%02d" % i)
            # print(j, i, YM)

            for infos in api.pd_fetch_tourspot_visitor(district, year=start_year+j, month="%02d" % i):
                print('=======================')
                print(infos)
                print('=======================')
                for info in infos:
                    preprocess_tourspot_visitor(info)

                results += infos

    # save results to file
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

    return filename

    # url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList?' \
    #       'serviceKey={0}&YM={1}&SIDO={2}&GUNGU={3}&RES_NM={4}&_type={5}'.format('%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D',
    #                                                          YM,
    #                                                          urllib.parse.quote(district),
    #                                                          '',
    #                                                          '',
    #                                                          'json')
    #
    # print(url)
    # print(url)
    # request = Request(url)
    # print(request)
    # response = urlopen(request)
    #
    # response_body = response.read().decode('utf-8')
    # print(response_body, type(response_body))
    # json_result = json.loads(response_body)
    # print(json_result, type(json_result))


# crawling_tourspot_visitor('서울', 2017, 2017)

# 운영체제에 폴더 존재 여부 확인.
if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)