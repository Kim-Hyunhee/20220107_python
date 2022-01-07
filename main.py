# FCM 서버에 -> 파이썬 프로그램으로 -> API 호출 (기기 푸시알림 전송 요청)
import requests

# 함수 제작 : 보내줄 문구 / 본문 내용을 받아서 전송

def send_fcm_notification(title, body):
    
    # FCM 서버에 요청
    # 1. 호스트 주소 / 기능 주소 => 실제 기능 URL
    url = 'https://fcm.googleapis.com/fcm/send'
    
    # 2. 첨부해야할 파라미터 (보내줄 데이터)
    
    # 헤더에 인증키 (token 같은 개념) 를 담아서 전달
    headers = {
        'Authorization':'key=AAAAKp25SY4:APA91bFVOL75dK5QVwQibpLBNk4hpdv6YgO0ZKuNG8dYTB4RW8YGMzTgZ1JL0e8Pbhi74pG-Oovkr8Iz3oIxZcKJv7kKGYNQNPMUB5n_7cNPUkOA7nYpgNDorskk7jp_Zz2pGuuoOMy5',
        'Content-Type': 'application/json; UTF-8',
    }
    
    content = {
        'registration_ids' : 'dBsUZVgVQYWVIr61MWqgi_:APA91bGJ13vGfE8Furd8oTywcUgpSKiyFCIvV8m5Xa3gi7vpo6Cy7mcVYLL1FlxOi6RSaEMrpLo5hMc7aRd81hho3jStaGAXNsq8_z-jHNaEiEXj_0fIu-60-1ZHO_NsOS-Hy4coflqf', # 어느 기기에 보낼건지 디바이스 토큰 cf) 리스트로 넣으면 여러 기기에 동시 전송
        'notification' : {
            
            'title' : title,
            'body' : body,
            
            }, # 기본 양식의 알림.  data-message로 보내면 : 커스터마이징 지원 알림
    }
    
    # 3. 어떤 방식