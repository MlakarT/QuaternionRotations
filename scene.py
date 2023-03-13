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
        t = MathTex(r'\int xe^{inx}dx=x\dfrac{e^{inx}}{in}-\dfrac{1}{in}\int e^{in}x_{dx}')
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

class ComplexRotation(Scene):
    """Demonstrates rotation in $\mathbb{C}$ with unit complex number multiplication."""
    def construct(self):
        # make a plane
        plane = ComplexPlane()
        self.play(FadeIn(plane))

        # add some points
        a = Dot([3,2,0], radius=0.1, stroke_width=0.05, color=WHITE)
        a_text = Text('(3,2)', font_size=DEFAULT_FONT_SIZE * 0.5).next_to(a,RIGHT * 0.6).shift(UP * 0.2)
        o = Dot(ORIGIN, radius=0.1, stroke_width=0.05, color=WHITE)
        point_group = Group(a, a_text, o)
        self.play(FadeIn(point_group))

        #add unit circle
        unitCircle = Circle(radius=1, color=WHITE)
        self.play(FadeIn(unitCircle))

        #wait a little
        self.wait(duration=1 * DEFAULT_WAIT_TIME)

        #add a point on unit circle at pi/6 degrees 
        rotatorPoint = Dot([sqrt(3)/2, 1/2, 0], radius=0.1, color=ORANGE)
        rotatingLine = Line(start=ORIGIN, end=rotatorPoint.get_center())
        self.play(Create(rotatingLine), FadeIn(rotatorPoint))

        #wait a little more
        self.wait(duration=1 * DEFAULT_WAIT_TIME)

        self.play(rotatorPoint.animate.move_to([1/2, sqrt(3)/2, 0]),rotatingLine.animate.rotate_about_origin(PI/6))
        

        self.wait()




        
#followed then by

class VectorQuaternionRepresentation(Scene):
    """Shows how we represent quaternions uniquely with $\mathbb{R} \oplus \mathbb{R}^3 \subseteq \mathbb{H}$"""
    pass

class VersorSpace(Scene):
    """Shows the representation of versors"""
    pass

class EulerVersorRepresentation(Scene):
    """Formulates the euler formula version of versor representation, derives the formula"""
    pass

class CTransformation(Scene):
    """Defines the C transformation in the space $\mathbb{H}$ and subsequent rotations in su subspaces of $\mathbb{H}$"""
    pass

#i think thats it for now

class Animate():
    ComplexRotation()
    VectorQuaternionRepresentation()
    VersorSpace()
    EulerVersorRepresentation()
    CTransformation()