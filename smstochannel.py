import requests

def sms(msg):
    heidarbot_id = '6390218017:AAEOMIF8wdTfRWBt65CRZem_0IGVboDiZx4'
    heidar_channel_id ='-1001943048766'  #heidar_channel
    url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(heidarbot_id,heidar_channel_id,msg)
    return requests.get(url)


if __name__ == '__main__':
    
    sms('my name is heidar')






