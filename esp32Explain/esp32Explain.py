from manim import *

class Soge(Scene):
    def construct(self):
        #기존 아두이노(atmega328p)의 스팩
        dan


        #esp32의 스팩



        '''제작 의도
        
        1. wifi를 이용한 원거리 추력측정
        - 기존의 유선, 무선 방식의 단점
        -- 기기가 두개 필요함. 무선의 단점(딜레이 연결불량 등)
        -- esp32의 wifi 호스트 기능으로 해결

        2. 더 좋은 cpu, dual core 280Mhz(maybe)
        - 따라서 기존에는 불가능 했던 복잡한 계산이 가능해짐

        3. 많은 양의 서보모터 제어를 위한 1234개의 pwm핀
        - 전력은 외부에서 끌어다 씀 (SG90 800mA 6개면 4.8A라서 PCB에서 출력하기에는 부담이 됨) 
        
        
        '''