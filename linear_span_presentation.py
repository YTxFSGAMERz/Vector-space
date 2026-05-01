from manim import *
from manim_slides import Slide

# ==========================================
# PRESENTATION CONFIGURATION
# ==========================================
config.background_color = "#F8F9FA"  # Light clean academic background
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

# Typography & Color Palette
TEXT_COLOR = "#212529"     # Dark text for high contrast
ACCENT_COLOR = "#0366D6"   # Elegant academic blue
MUTED_COLOR = "#6C757D"    # Gray for secondary elements
GRID_COLOR = "#DEE2E6"     # Light grid

TITLE_SIZE = 64
HEADING_SIZE = 48
BULLET_SIZE = 36
MATH_SIZE = 44

class LinearSpanPresentation(Slide):
    def construct(self):
        self.slide_1_title()
        self.slide_2_definition()
        self.slide_3_example()
        self.slide_4_importance()
        self.slide_5_conclusion()

    def slide_1_title(self):
        # Background geometric elements (faint grid)
        plane = NumberPlane(
            x_range=[-10, 10, 1], y_range=[-6, 6, 1],
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1, "stroke_opacity": 0.5}
        )
        self.play(FadeIn(plane), run_time=1.5)

        # Text Elements
        title = Text("Linear Span", font_size=TITLE_SIZE + 10, color=TEXT_COLOR, weight=BOLD)
        subtitle = Text("Mathematics-II Presentation", font_size=HEADING_SIZE - 8, color=MUTED_COLOR)
        sub_subtitle = Text("Vector Space Concept", font_size=HEADING_SIZE - 12, color=MUTED_COLOR)
        
        VGroup(title, subtitle, sub_subtitle).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        presenter_text = Text(
            "Name: [Your Name]\nRoll No: [Your Roll No]\nClass: [Your Class]\nCollege: [Your College]",
            font_size=24, color=TEXT_COLOR, line_spacing=1.2
        )
        # Rounded box near the lower part
        presenter_box = RoundedRectangle(
            height=presenter_text.height + 0.5, width=presenter_text.width + 0.8,
            corner_radius=0.2, color=GRID_COLOR, fill_color=WHITE, fill_opacity=0.8, stroke_width=2
        )
        presenter_group = VGroup(presenter_box, presenter_text).to_corner(DR, buff=0.6)
        presenter_text.move_to(presenter_box.get_center())

        # Faint vectors for visual accent, pushed far away
        v1 = Arrow(ORIGIN, [3, 1.5, 0], buff=0, color=ACCENT_COLOR, stroke_width=5, stroke_opacity=0.08).shift(RIGHT*4 + UP*2)
        v2 = Arrow(ORIGIN, [-2, 2.5, 0], buff=0, color=ACCENT_COLOR, stroke_width=5, stroke_opacity=0.08).shift(LEFT*4.5 + UP*2.5)
        v3 = Arrow(ORIGIN, [-1.5, -2, 0], buff=0, color=ACCENT_COLOR, stroke_width=5, stroke_opacity=0.08).shift(LEFT*3.5 + DOWN*2.5)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP*0.3), FadeIn(sub_subtitle, shift=UP*0.3))
        self.play(FadeIn(presenter_group, shift=LEFT*0.3))
        self.play(GrowArrow(v1), GrowArrow(v2), GrowArrow(v3))
        
        self.next_slide()
        self.play(FadeOut(Group(*self.mobjects)))

    def slide_2_definition(self):
        heading = Text("What is Linear Span?", font_size=HEADING_SIZE, color=TEXT_COLOR, weight=BOLD)
        heading.to_edge(UP, buff=0.6)
        self.play(Write(heading))

        bullets = VGroup(
            Text("• The set of all vectors formed by linear combinations.", font_size=BULLET_SIZE, color=TEXT_COLOR, t2c={"linear combinations": ACCENT_COLOR}),
            Text("• Often simply called the span of those vectors.", font_size=BULLET_SIZE, color=TEXT_COLOR)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(heading, DOWN, buff=0.6)
        bullets.set_x(0)

        formula = MathTex(
            r"\text{Span}(v_1, v_2, \dots, v_n) = \{ a_1v_1 + a_2v_2 + \dots + a_nv_n \}",
            color=ACCENT_COLOR, font_size=MATH_SIZE + 4
        ).next_to(bullets, DOWN, buff=0.6).shift(LEFT*1.0)
        
        scalar_note = Text("where coefficients a₁, a₂, ... can be any scalars.", font_size=28, color=MUTED_COLOR)
        scalar_note.next_to(formula, DOWN, buff=0.3)

        memorable = Text("“Linear span means all possible results\nyou can make from the given vectors.”", 
                         font_size=28, color=TEXT_COLOR, slant=ITALIC, weight=BOLD)
        memorable.next_to(scalar_note, DOWN, buff=0.8)

        # Tiny visual metaphor
        axes = Axes(x_range=[-2, 2, 1], y_range=[-2, 2, 1], x_length=2.5, y_length=2.5)
        axes.set_color(GRID_COLOR)
        
        v_main1 = Arrow(axes.c2p(0,0), axes.c2p(1,0.5), buff=0, color=ACCENT_COLOR, stroke_width=4)
        v_main2 = Arrow(axes.c2p(0,0), axes.c2p(-0.5,1), buff=0, color=ACCENT_COLOR, stroke_width=4)
        v_comb1 = Arrow(axes.c2p(0,0), axes.c2p(1.5,1.5), buff=0, color=ACCENT_COLOR, stroke_width=4, stroke_opacity=0.3)
        v_comb2 = Arrow(axes.c2p(0,0), axes.c2p(0.5, -0.5), buff=0, color=ACCENT_COLOR, stroke_width=4, stroke_opacity=0.3)
        diag_group = VGroup(axes, v_main1, v_main2, v_comb1, v_comb2).to_corner(DR, buff=0.5).scale(0.8)

        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT*0.3))
        self.next_slide()
        
        self.play(Write(formula), run_time=1.5)
        self.play(FadeIn(scalar_note))
        self.next_slide()
        
        # Bring in the visual metaphor
        self.play(FadeIn(diag_group))
        self.next_slide()

        self.play(FadeIn(memorable, scale=0.9))
        self.next_slide()

        self.play(FadeOut(Group(*self.mobjects)))

    def slide_3_example(self):
        heading = Text("Example in R²", font_size=HEADING_SIZE, color=TEXT_COLOR, weight=BOLD)
        heading.to_edge(UP, buff=0.6)
        self.play(Write(heading))

        left_group = VGroup()
        
        basis_text = Tex(
            r"\textbf{Standard basis vectors:}\\",
            r"$v_1 = (1, 0)$ \\",
            r"$v_2 = (0, 1)$",
            color=TEXT_COLOR, font_size=BULLET_SIZE
        )
        
        formula = MathTex(
            r"a(1, 0) + b(0, 1) = (a, b)",
            color=ACCENT_COLOR, font_size=MATH_SIZE
        )
        
        left_group.add(basis_text, formula).arrange(DOWN, buff=1.2).to_edge(LEFT, buff=1.5).shift(UP*0.5)

        axes = NumberPlane(
            x_range=[-1, 5, 1], y_range=[-1, 5, 1],
            x_length=4.5, y_length=4.5,
            background_line_style={"stroke_color": GRID_COLOR, "stroke_opacity": 0.5},
            axis_config={"color": TEXT_COLOR}
        ).to_edge(RIGHT, buff=1.0).shift(UP*0.5)

        e1 = Arrow(axes.c2p(0,0), axes.c2p(1,0), buff=0, color=ACCENT_COLOR, stroke_width=5)
        e2 = Arrow(axes.c2p(0,0), axes.c2p(0,1), buff=0, color=ACCENT_COLOR, stroke_width=5)
        
        e1_label = MathTex("e_1", color=ACCENT_COLOR, font_size=36).next_to(e1, DOWN)
        e2_label = MathTex("e_2", color=ACCENT_COLOR, font_size=36).next_to(e2, LEFT)
        
        target_coords = (3, 4)
        dot = Dot(axes.c2p(0,0), color=TEXT_COLOR, radius=0.1)
        
        sample_point = axes.c2p(*target_coords)
        sample_vector = Arrow(axes.c2p(0,0), sample_point, buff=0, color=TEXT_COLOR)
        sample_label = MathTex("(a, b)", color=TEXT_COLOR, font_size=36).next_to(sample_point, UR, buff=0.1)
        
        h_vec = Arrow(axes.c2p(0,0), axes.c2p(target_coords[0],0), buff=0, color=ACCENT_COLOR, stroke_opacity=0.6)
        v_vec = Arrow(axes.c2p(target_coords[0],0), sample_point, buff=0, color=ACCENT_COLOR, stroke_opacity=0.6)
        
        h_line = DashedLine(axes.c2p(target_coords[0],0), sample_point, color=MUTED_COLOR)
        v_line = DashedLine(axes.c2p(0,target_coords[1]), sample_point, color=MUTED_COLOR)

        conclusion = Text("Span{(1,0), (0,1)} = R²", font_size=36, color=TEXT_COLOR, weight=BOLD)
        conclusion.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(basis_text), FadeIn(axes))
        self.play(GrowArrow(e1), GrowArrow(e2), FadeIn(e1_label), FadeIn(e2_label))
        
        self.next_slide()
        
        self.play(FadeIn(formula))
        self.next_slide()
        
        # Moving dot animation to show reachability
        self.play(FadeIn(dot))
        self.play(dot.animate.move_to(axes.c2p(target_coords[0], 0)), GrowArrow(h_vec), run_time=1.5)
        self.play(dot.animate.move_to(sample_point), GrowArrow(v_vec), run_time=1.5)
        self.play(GrowArrow(sample_vector), FadeIn(sample_label), FadeIn(h_line), FadeIn(v_line))
        
        self.next_slide()
        
        self.play(Write(conclusion))
        
        self.next_slide()
        self.play(FadeOut(Group(*self.mobjects)))

    def slide_4_importance(self):
        heading = Text("Why is Linear Span Important?", font_size=HEADING_SIZE, color=TEXT_COLOR, weight=BOLD)
        heading.to_edge(UP, buff=0.5)
        self.play(Write(heading))

        takeaway = Text("“Span is all the places you can reach\nusing the given vectors.”", 
                        font_size=32, color=ACCENT_COLOR, weight=BOLD, slant=ITALIC)
        takeaway.next_to(heading, DOWN, buff=0.5)
        self.play(FadeIn(takeaway, shift=UP*0.3))
        self.next_slide()

        # 3 Panels
        panels = VGroup()
        
        ax1 = Axes(x_range=[-2,2,1], y_range=[-2,2,1], x_length=2.5, y_length=2.5, axis_config={"color": GRID_COLOR})
        v1 = Arrow(ax1.c2p(0,0), ax1.c2p(1,1), buff=0, color=ACCENT_COLOR)
        line1 = Line(ax1.c2p(-2,-2), ax1.c2p(2,2), color=ACCENT_COLOR, stroke_opacity=0.3, stroke_width=15)
        label1 = Text("1 vector\n→ line", font_size=20, color=TEXT_COLOR, weight=BOLD, t2c={"line": ACCENT_COLOR}).next_to(ax1, DOWN, buff=0.3)
        panel1 = VGroup(ax1, line1, v1, label1)

        ax2 = Axes(x_range=[-2,2,1], y_range=[-2,2,1], x_length=2.5, y_length=2.5, axis_config={"color": GRID_COLOR})
        v2_1 = Arrow(ax2.c2p(0,0), ax2.c2p(1,1), buff=0, color=ACCENT_COLOR)
        v2_2 = Arrow(ax2.c2p(0,0), ax2.c2p(1.5,1.5), buff=0, color=ACCENT_COLOR)
        line2 = Line(ax2.c2p(-2,-2), ax2.c2p(2,2), color=ACCENT_COLOR, stroke_opacity=0.3, stroke_width=15)
        label2 = Text("dependent vectors\n→ same span", font_size=20, color=TEXT_COLOR, weight=BOLD, t2c={"dependent": ACCENT_COLOR, "span": ACCENT_COLOR}).next_to(ax2, DOWN, buff=0.3)
        panel2 = VGroup(ax2, line2, v2_1, v2_2, label2)

        ax3 = Axes(x_range=[-2,2,1], y_range=[-2,2,1], x_length=2.5, y_length=2.5, axis_config={"color": GRID_COLOR})
        v3_1 = Arrow(ax3.c2p(0,0), ax3.c2p(1,0.5), buff=0, color=ACCENT_COLOR)
        v3_2 = Arrow(ax3.c2p(0,0), ax3.c2p(0.5,1.5), buff=0, color=ACCENT_COLOR)
        plane = Rectangle(width=2.5, height=2.5, fill_color=ACCENT_COLOR, fill_opacity=0.15, stroke_opacity=0).move_to(ax3.c2p(0,0))
        label3 = Text("independent vectors\n→ plane", font_size=20, color=TEXT_COLOR, weight=BOLD, t2c={"independent": ACCENT_COLOR, "plane": ACCENT_COLOR}).next_to(ax3, DOWN, buff=0.3)
        panel3 = VGroup(ax3, plane, v3_1, v3_2, label3)

        panels.add(panel1, panel2, panel3).arrange(RIGHT, buff=0.8).next_to(takeaway, DOWN, buff=0.6)

        bullets = VGroup(
            Text("• Span tells us the space generated by vectors.", font_size=28, color=TEXT_COLOR),
            Text("• One vector gives a line.", font_size=28, color=TEXT_COLOR, t2c={"line": ACCENT_COLOR}),
            Text("• Independent vectors can give a plane.", font_size=28, color=TEXT_COLOR, t2c={"Independent": ACCENT_COLOR, "plane": ACCENT_COLOR}),
            Text("• Foundational for basis and dimension.", font_size=28, color=TEXT_COLOR, t2c={"basis": ACCENT_COLOR, "dimension": ACCENT_COLOR})
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(panels, DOWN, buff=0.6)
        
        self.play(FadeIn(ax1))
        self.play(GrowArrow(v1))
        self.play(FadeIn(line1), FadeIn(label1))
        self.next_slide()

        self.play(FadeIn(ax2))
        self.play(GrowArrow(v2_1), GrowArrow(v2_2))
        self.play(FadeIn(line2), FadeIn(label2))
        self.next_slide()

        self.play(FadeIn(ax3))
        self.play(GrowArrow(v3_1), GrowArrow(v3_2))
        self.play(FadeIn(plane), FadeIn(label3))
        self.next_slide()

        for bullet in bullets:
            self.play(FadeIn(bullet, shift=UP*0.2))
            self.wait(0.2)
        
        self.next_slide()
        self.play(FadeOut(Group(*self.mobjects)))

    def slide_5_conclusion(self):
        heading = Text("Conclusion", font_size=HEADING_SIZE, color=TEXT_COLOR, weight=BOLD)
        heading.to_edge(UP, buff=0.8)
        self.play(Write(heading))

        bullets = VGroup(
            Text("• Linear span is the set of all linear combinations of given vectors.", font_size=28, color=TEXT_COLOR),
            Text("• It shows the space generated by those vectors.", font_size=28, color=TEXT_COLOR),
            Text("• It helps us understand lines, planes, and higher-dimensional spaces.", font_size=28, color=TEXT_COLOR),
            Text("• It is a fundamental idea in vector space theory.", font_size=28, color=TEXT_COLOR)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        
        bullets.next_to(heading, DOWN, buff=1.0)
        bullets.set_x(0)

        for bullet in bullets:
            self.play(FadeIn(bullet, shift=UP*0.3))
            self.wait(0.5)
            
        thank_you = Text("Thank You", font_size=TITLE_SIZE, color=ACCENT_COLOR, weight=BOLD)
        thank_you.next_to(bullets, DOWN, buff=1.0)
        
        self.next_slide()
        self.play(FadeIn(thank_you, scale=0.8))
        self.next_slide()
