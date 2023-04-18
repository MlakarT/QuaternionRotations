from manim import *
from math import *
# remember to run /bin/bash ./seminar/project/scene.py

#another remember: run python3 -m mainm
#in the appropriate directory beforehand so we can get videos premade before presentation

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

#Ce se bom tole dejansko ucu je mogoce useful met neke zapiske ish
#as in kaj se dogaja kaj stvari pomenjo
#npr Scene je superclass od ush classov stvari k jh narises

#also **lahko poganjas posamezne odseke v scene.py** ne nujno ceuga

#Test stuff here
#============================================================================================================================

class Formula(Scene):
    def construct(self):
        t = MathTex(r'\int xe^{inx}dx=x\dfrac{e^{inx}}{in}-\dfrac{1}{in}\int e^{inx} {dx}')
        self.add(t)

class PlaneInE3(Scene):
    def construct(self):
        system = ThreeDAxes(tips=False).rotate_sheen_direction(angle=(PI / 4), axis=UP)
        self.play(FadeIn(system))

class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))


# Put actual stuff here 
#============================================================================================================================

#mogoce bi blo tud fajn met nek game plan kako se lott pisanja scen prej
#ampak definitivno bo tkole nekak

class Intro(Scene):
    def construct(self):
        title = Text("Rotacije opisane s kvaternioni")
        self.play(Write(title))
        box = Rectangle(color=RED, height=2, width=10)
        self.play(DrawBorderThenFill(box))
        titleGroup = Group(title, box)
        self.play(titleGroup.animate.shift(2*UP))
        self.wait()
        author = Text("Timotej Mlakar").scale(0.7)
        dept = Text("Fakulteta za matematiko in fiziko").scale(0.4).next_to(author, DOWN)
        dept2 = Text("Oddelek za matematiko").scale(0.4).next_to(dept, DOWN)
        date = Text("18. april 2023").scale(0.7).next_to(dept2, 1.5*DOWN)

        self.play(FadeIn(author), FadeIn(dept),FadeIn(dept2), FadeIn(date))
        
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m).scale(0.3)  # order matters
        logo.to_corner(DR)
        self.play(Write(ds_m), DrawBorderThenFill(square),  DrawBorderThenFill(circle),SpiralIn(triangle))
        self.wait()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Complex(Scene) : 
    def construct(self):
        plane = ComplexPlane().add_coordinates()
        self.add(plane)

        p1 = Dot(plane.n2p(3 + 1j), color=WHITE)
        line = Line(plane.n2p(0+0j), p1.get_center(), color=WHITE)
        a, b = cos(PI/3), sin(PI/3)
        p2 = Dot(plane.n2p(a+ b*1j), color=WHITE)
        p1_text = always_redraw(lambda : MathTex("3+i").next_to(p1,RIGHT, 0.1))
        p2_text = always_redraw(lambda : MathTex("e^{i\\frac{\\pi}{3}}").next_to(p2, UP, 0.1))

        circle = Circle(1,color=RED).move_to(plane.n2p(0+0j))

        cplxGroup = Group(line ,p1, circle, p2)

        self.play(GrowFromPoint(line, plane.n2p(0+0j), line.get_color()) ,GrowFromPoint(p1, p1, p1.get_color()), Write(p1_text))
        self.wait()

        self.play(FadeIn(circle, p2), Write(p2_text))
        self.wait(duration=3*DEFAULT_WAIT_TIME)
        self.wait(2)
        
        self.play(Rotate(cplxGroup, PI/3, axis=OUT, about_point=plane.n2p(0+0j)))
        self.wait()

        p12_text = MathTex("(3+i) \\cdot e^{i\\frac{\\pi}{3}}", color=GREEN).next_to(p1, RIGHT, buff = 0.1)
        p22_text = MathTex("e^{i2\\frac{\\pi}{3}}", color=GREEN).next_to(p2, UL, buff = 0.1)

        self.play(Transform(p1_text, p12_text, replace_mobject_with_target_in_scene=True), Transform(p2_text, p22_text,replace_mobject_with_target_in_scene=True))
        self.wait() 

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class QuaternionMultiplication(Scene) : 
    def construct(self):
        pq1 = MathTex("pq")
        self.add(pq1)
        self.wait()

        pq2 = MathTex("(p_{0} + \\vec{p}) (q_{0} + \\vec{q})")
        self.play(Transform(pq1, pq2, replace_mobject_with_target_in_scene=True))
        self.wait(2)

        pq3 = MathTex("(p_{0} + p_{1}i + p_{2}j + p_{3}k)(q_{0} + q_{1}i + q_{2}j + q_{3}k)")
        self.play(Transform(pq2, pq3, replace_mobject_with_target_in_scene=True))
        self.wait(duration=3*DEFAULT_WAIT_TIME)

        p0q = r"&= p_{0}q_{0} + p_{0}q_{1}i + p_{0}q_{2}j + p_{0}q_{3}k\\"
        p1q = r"&+ p_{1}q_{0}i + p_{1}q_{1}ii + p_{1}q_{2}ij + p_{1}q_{3}ik\\"
        p2q = r"&+ p_{2}q_{0}j + p_{2}q_{1}ji + p_{2}q_{2}jj + p_{2}q_{0}jk\\"
        p3q = r"&+ p_{3}q_{0}k + p_{3}q_{1}ki + p_{3}q_{2}kj + p_{3}q_{0}kk"

        pq4 = MathTex(p0q + p1q + p2q + p3q)

        for i in [10, 28, 34, 35, 41, 48, 62, 89]:
            pq4[0][i].set_color(RED)
        for j in [16, 42, 55, 61, 68, 69, 75, 96]:
            pq4[0][j].set_color(GREEN)
        for k in [22, 49, 76, 82, 88, 95, 102, 103]:
            pq4[0][k].set_color(YELLOW)

        self.play(Transform(pq3, pq4, replace_mobject_with_target_in_scene=True))
        # self.add(index_labels(pq4[0]))
        self.wait(duration=5*DEFAULT_WAIT_TIME)

        p0q = r"&= p_{0}q_{0} + p_{0}q_{1}i + p_{0}q_{2}j + p_{0}q_{3}k\\"
        p1q = r"&+ p_{1}q_{0}i - p_{1}q_{1} + p_{1}q_{2}k - p_{1}q_{3}j\\"
        p2q = r"&+ p_{2}q_{0}j - p_{2}q_{1}k - p_{2}q_{2} + p_{2}q_{0}i\\"
        p3q = r"&+ p_{3}q_{0}k + p_{3}q_{1}j - p_{3}q_{2}i - p_{3}q_{0}"

        pq5 = MathTex(p0q + p1q + p2q + p3q, substrings_to_isolate=["=", "+", "-"])

        self.play(Transform(pq4, pq5, replace_mobject_with_target_in_scene=True))
        #self.add(index_labels(pq5))
        self.wait(5)

        p0q0_surround = pq5[2]
        p0q0_rect = SurroundingRectangle(p0q0_surround, color=RED)
        p1q1_surround = pq5[11:13]
        p1q1_rect = SurroundingRectangle(p1q1_surround, color=RED)
        p2q2_surround = pq5[21:23]
        p2q2_rect = SurroundingRectangle(p2q2_surround, color=RED)
        p3q3_surround = pq5[31:33]
        p3q3_rect = SurroundingRectangle(p3q3_surround, color=RED)

        self.play(
            DrawBorderThenFill(p0q0_rect),
            DrawBorderThenFill(p1q1_rect),
            DrawBorderThenFill(p2q2_rect),
            DrawBorderThenFill(p3q3_rect)
        )
        self.wait(5)

        p0q_rect = SurroundingRectangle(pq5[3:9], color=GREEN)
        q0p_rect = SurroundingRectangle(Group(pq5[9:11], pq5[17:19], pq5[25:27]), color=GREEN)

        self.play(DrawBorderThenFill(p0q_rect), DrawBorderThenFill(q0p_rect))
        self.wait(5)

        self.play(Uncreate(p0q0_rect),
        Uncreate(p1q1_rect),
        Uncreate(p2q2_rect),
        Uncreate(p3q3_rect),
        Uncreate(p0q_rect),
        Uncreate(q0p_rect))

        p0q0 = r"&= p_{0}q_{0}"
        pqdot = r"-\vec{p}\vec{q}\\"
        p0q = r"&+ p_{0}\vec{q}"
        q0p = r" + q_{0}\vec{p}"
        pxq = r" +\vec{p} \times \vec{q}"
    
        pq6 = MathTex(p0q0 + pqdot + p0q + q0p + pxq)

        self.play(Transform(pq5, pq6, replace_mobject_with_target_in_scene=True))
        self.wait()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class EulerRepr(Scene):
    """Formulates the euler formula version of versor representation, derives the formula"""
    def construct(self):
        exp= MathTex(r"e^{{x}}")
        self.add(exp)
        self.wait()

        self.play(exp.animate.shift(4*LEFT))
        expTaylor=MathTex(r"= 1 + {{ x }} + \frac{1}{2} {{ x }}^2 + \frac{1}{6} {{ x }}^3 +\frac{1}{24} {{ x }}^4 + \cdots").next_to(exp)
        self.play(Write(expTaylor))
        self.wait()

        self.play(exp.animate.set_color_by_tex("x", color=YELLOW), expTaylor.animate.set_color_by_tex("x", color=YELLOW))
        self.wait()

        exp2 = MathTex(r"e^{{{u}}\theta}").shift(4*LEFT)
        expQuaternionTaylor = MathTex(r"= 1 + {{ u\theta }} + \frac{1}{2} {{ (u\theta) }}^2 + \frac{1}{6} {{ (u\theta) }}^3 +\frac{1}{24} {{ (u\theta) }}^4 + \cdots").next_to(exp2)
        self.play(TransformMatchingTex(exp, exp2), TransformMatchingTex(expTaylor, expQuaternionTaylor))
        self.wait(3)

        expQuaternionTaylor2 = MathTex(r"= 1 + {{ u\theta }} + \frac{1}{2} {{ u }}^2\theta^2 + \frac{1}{6} {{u}}^3\theta^3 +\frac{1}{24} {{u}}^4\theta^4 + \cdots").next_to(exp)
        expQuaternionTaylor3 = MathTex(r"= 1 + {{u}}\theta - \frac{1}{2} \theta^2 - \frac{1}{6} {{u}}\theta^3 +\frac{1}{24} \theta^4 + \cdots").next_to(exp)

        self.play(TransformMatchingTex(expQuaternionTaylor, expQuaternionTaylor2))
        self.wait(5)
        self.play(TransformMatchingTex(expQuaternionTaylor2, expQuaternionTaylor3))
        self.wait()
        
        self.play(exp2.animate.set_color_by_tex("u", color=YELLOW) ,expQuaternionTaylor3.animate.set_color_by_tex("u", color = YELLOW))
        self.wait()

        group1 = Group(exp2, expQuaternionTaylor3)

        self.play(group1.animate.shift(2*UP))
        self.wait(3)

        brackets1 = MathTex(r"\Big( 1 - \frac{1}{2} \theta^2 +\frac{1}{24} \theta^4 + \cdots \Big) + \Big( {{u}}\theta - \frac{1}{6} {{u}}\theta^3 + \cdots \Big)").set_color_by_tex("u", color=YELLOW).next_to(expQuaternionTaylor3, DOWN, buff=0.3)
        self.play(GrowFromPoint(brackets1, group1.get_center()))
        self.wait(3)

        brackets2 = MathTex(r"\Big( 1 - \frac{1}{2} \theta^2 +\frac{1}{24} \theta^4 + \cdots \Big) + {{u}}\Big( \theta - \frac{1}{6} \theta^3 + \cdots \Big)").set_color_by_tex("u", color=YELLOW).next_to(brackets1, DOWN, buff=0.3)
        self.play(TransformFromCopy(brackets1, brackets2))
        self.wait(3)

        cosAndSin = MathTex(r"\cos\theta + {{u}}\sin\theta").set_color_by_tex("u", color=YELLOW).move_to(brackets2.get_center()).shift(DOWN)
        self.play(TransformFromCopy(brackets2, cosAndSin))
        self.wait()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class CTransformation(Scene):
    """Defines the C transformation in the space $\mathbb{H}$ and subsequent rotations in su subspaces of $\mathbb{H}$"""
    pass
