import json
import urllib
from .json_request import json_request
from urllib.request import Request, urlopen
from datetime import datetime, date as dt

def pd_gen_url(endpoint, service_key, **params):
    print(endpoint)
    print(service_key)
    print(params.get('YM'))
    url = '{0}?serviceKey={1}&YM={2}&SIDO={3}&GUNGU={4}&RES_NM={5}&_type={6}'.format(endpoint, service_key, params.get('YM'), urllib.parse.quote(params.get('SIDO')), urllib.parse.quote(params.get('GUNGU')), urllib.parse.quote(params.get('RES_NM')), params.get('_type'))
    print(url)
    request = Request(url)
    print(request)
    response = urlopen(request)

    response_body = response.read().decode('utf-8')
    print(response_body, type(response_body))
    json_result = json.loads(response_body)
    print(json_result, type(json_result))

    return json_result

# 이 함수에서 service_key를 넣지 않는걸로 노력.
def pd_fetch_foreign_visitor(country_code=0, year=0, month=0, service_key='iunUk64NxYTOYeC%2BnepieQVg9x0d%2F250%2BjasvKdeU%2FYDLWbvsUCe6njzndVR9E6jAbpMOysRIL77mnXaVXdE5g%3D%3D'):
    # YM = str(year) + ('%02d' % month)
    YM = str(year) + str(month)
    print(YM)
    print(service_key)
    print(country_code)
    url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?' \
          'serviceKey={0}&YM={1}&NAT_CD={2}&_type=json'.format(service_key,
                                                               YM,
                                                               country_code)
    print(url)
    request = Request(url)
    print(request)
    response = urlopen(request)
    response_body = response.read().decode('utf-8')
    print(response_body, type(response_body))

    json_result = json.loads(response_body)

    print(json_result['response']['body']['items']['item'], type(json_result['response']['body']['items']['item']))

    return json_result['response']['body']['items']['item']


def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0,
        service_key='%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D'):
    print(district1)
    print(district2)
    print(tourspot)
    print(year)
    print(month)
    print(service_key)
    print('================')
    YM = str(year) + str(month)
    print(YM)

    url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList?' \
          'serviceKey={0}&YM={1}&SIDO={2}&GUNGU={3}&RES_NM={4}&_type={5}'.format(service_key,
                                                                                 YM,
                                                                                 urllib.parse.quote(district1),
                                                                                 urllib.parse.quote(district2),
                                                                                 urllib.parse.quote(tourspot),
                                                                                 'json')
    print(url)
    request = Request(url)
    print(request)
    response = urlopen(request)
    response_body = response.read().decode('utf-8')
    print(response_body, type(response_body))

    json_result = json.loads(response_body)
    print('!!!!!!!!!!!!!!!!!', json_result, type(json_result))
    print('!!!!!!!!!!!!!!!!!', type(json_result['response']['body']['items']['item']))
    # return json_result['response']['body']['items']['item']
    yield json_result['response']['body']['items']['item']
