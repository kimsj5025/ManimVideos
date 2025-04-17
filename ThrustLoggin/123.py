from manim import *

class MyScene(Scene):
    def construct(self):
        self.camera.background_color = color_to_int_rgb("#555555")  # 배경을 흰색으로 설정
        text = Text("어떻게 추력을 측정할까?", font="Apple SD Gothic Neo")
        self.add(text)
        self.play(Write(text), run_time=4)
        self.wait(2)

        title = Text("고려해야 할 사항들", color=WHITE, font="Apple SD Gothic Neo")
        title.scale(0.75)
        title.to_edge(UL)
        self.play(Transform(text, title), run_time=2)

        t1 = Text("1. 보드 선택", font="Apple SD Gothic Neo").set_color(WHITE)
        t2 = Text("2. 센서 선택", font="Apple SD Gothic Neo").set_color(WHITE)
        t3 = Text("3. 데이터 분석 및 시각화", font="Apple SD Gothic Neo").set_color(WHITE)

        x = VGroup(t1, t2, t3).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).to_edge(DL)
        x.set_opacity(0.5)
        x.submobjects[0].set_opacity(1)
        self.play(Write(x))
        self.play(x.animate.scale(0.5).to_edge(DL), run_time=2)
        
        self.wait(1)

        t0 = Table([["nRF52840", "ATMEGA328p","ATMEGA328p"],["작음","무난함","Wifi지원"]],row_labels=[Text("MUC"), Text("Features")],col_labels=[Text("Nano 33 ble"), Text("Uno Mrina"), Text("Uno Wifi")],top_left_entry=Text("Name"))
        t0.scale(0.5)
        self.play(Write(t0))
        self.wait(1)
        columns = t0.get_columns()

        for col in columns:
            box = SurroundingRectangle(col, color=BLUE)
            self.play(Create(box))
            self.wait(0.5)
            self.play(Flash(box))
            self.wait(0.5)
            self.play(FadeOut(box))
        self.wait(1)
        self.play(FadeOut(t0))
        
        #목차 2번 선택
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.play(Indicate(x.submobjects[1]))

        t1 = Table(
            [["2 wire", "디지털","Serial"],
             ["300kg","선 1개로 제어가능","15km 통신가능"]],
             row_labels=[Text("Connention"), Text("Feature")],
             col_labels=[Text("Load cell"), Text("relay"), Text("Telemetry")],top_left_entry=Text("Name")
            )
        t1.scale(0.5)
        self.play(Write(t1))
        self.wait(1)
        columns = t1.get_columns()

        for col in columns:
            box = SurroundingRectangle(col, color=BLUE)
            self.play(Create(box))
            self.wait(0.5)            
            self.play(Flash(box))
            self.wait(0.5)
            self.play(FadeOut(box))
        
        #3번 칼럼
        self.wait(2)
        self.play(FadeOut(t1))
        x.set_opacity(0.5)
        x.submobjects[2].set_opacity(1)
        self.play(Indicate(x.submobjects[2]))


        tx = Text("하지만 데이터는 무게(kg)의 형태 이므로\n중력가속도를 곱해서 힘(N)으로 바꿔줘야 한다", font="Apple SD Gothic Neo")
        self.play(Write(tx),run_tiem = 3)
        self.wait(2)
        self.play(FadeOut(tx))


        data = [
            -0.000, -0.000, -0.000, 0.000, 0.000, 0.000, 0.000, 0.339, 1.084, 2.069,
            3.748, 6.737, 11.79, 17.857, 23.905, 27.061, 26.503, 23.597, 20.624, 17.473,
            12.672, 8.144, 4.232, 1.348, 0.387, 0.000, -0.000, -0.000, -0.000, -0.000, -0.000
        ]
        time = [i * 0.1 for i in range(len(data))]


        yMaxData = ValueTracker(max(data))
        # 축 생성
        axes = always_redraw(
            lambda:
            Axes(
            x_range=[0, len(data)*0.1, 1],      # x축: 시간
            y_range=[-1, yMaxData.get_value() + 5, yMaxData.get_value()//5],     # y축: 값
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True}
        ).to_edge(DOWN))

        # 라벨 추가
        labels = axes.get_axis_labels(x_label="s", y_label="kg")

        # 그래프 포인트로 변환
        points = [axes.coords_to_point(t, v) for t, v in zip(time, data)]

        # 선형 연결
        graph_line = VMobject(color=BLUE)
        graph_line.set_points_smoothly(points)
        
        g_label = always_redraw(lambda: Text(
            f"g = {yMaxData.get_value()/max(data):.2f}", font_size=32
        ).next_to(axes, UP + RIGHT))
        # 애니메이션
        self.play(Create(axes), Write(labels), run_time = 3)
        self.play(Create(graph_line), run_time=3)
        self.wait(2)
        self.play(Write(g_label), run_time = 0.3)
        self.play(yMaxData.animate.set_value(yMaxData.get_value()*9.81), run_time=3)
        self.wait(0.2)
        new_labels = axes.get_axis_labels(x_label="s", y_label="N")
        self.play(Transform(labels, new_labels))
        self.wait(3)

        fill_points = [axes.coords_to_point(time[0], 0)] + points + [axes.coords_to_point(time[-1], 0)]
        fill = Polygon(*fill_points[6:-5], color=BLUE, fill_opacity=0.75, stroke_width=0)
        self.play(FadeIn(fill),FadeOut(g_label))

        s1 = MathTex("S_1").move_to(fill)
        self.play(Write(s1))
        self.wait()
        self.play(s1.animate.move_to(g_label.get_left()))
        self.wait(2)
        new_s1 = MathTex(r"S_1 = 204.8Ns")
        new_s1.move_to(s1)  # 기존 위치 유지
        self.play(Transform(s1,new_s1))
        self.wait(3)

class outro(Scene):
    def construct(self):

        logo = Text("g'(x)")
        self.play(SpiralIn(logo))
        tx = Text("지금까지 추력을 측정하는 방법을 알아봤습니다.\n 끝까지 봐 주셔서 감사합니다.", font="Apple SD Gothic Neo")
        self.play(Write(tx), run_time = 5)