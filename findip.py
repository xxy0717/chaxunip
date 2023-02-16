import requests
import streamlit as st

def get_location(ip):
    """
    通过查询接口获取ip地址所属省份和城市信息
    """
    url = f'http://whois.pconline.com.cn/ipJson.jsp?json=true&ip={ip}'
    r = requests.get(url)
    r.encoding = 'gbk'  # 设置编码格式为 gbk
    data = r.json()
    province = data.get('pro')
    province_code = data.get('proCode')
    city = data.get('city')
    city_code = data.get('cityCode')
    return province, province_code, city, city_code

st.title('IP地址查询应用')
st.write('请输入要查询的ip地址，多个地址用空格隔开')
ips = st.text_input('输入ip地址')
ips = ips.split(' ')
if ips:
    for ip in ips:
        if ip:
            province, province_code, city, city_code = get_location(ip)
            st.write(f'{ip}|{province}|{province_code}|{city}|{city_code}')
