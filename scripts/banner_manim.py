from manim import *


class ProfileBanner(Scene):
    def construct(self):
        self.camera.background_color = "#05070d"

        width = 14.222
        height = 4.267

        bg = VGroup()
        colors = ["#05070d", "#07111f", "#0b1f35", "#0e3a4a", "#116149"]
        for index in range(80):
            x = -width / 2 + width * (index + 0.5) / 80
            t = index / 79
            color = interpolate_color(
                ManimColor(colors[min(int(t * (len(colors) - 1)), len(colors) - 2)]),
                ManimColor(colors[min(int(t * (len(colors) - 1)) + 1, len(colors) - 1)]),
                (t * (len(colors) - 1)) % 1,
            )
            stripe = Rectangle(
                width=width / 80 + 0.02,
                height=height,
                stroke_width=0,
                fill_color=color,
                fill_opacity=1,
            )
            stripe.move_to([x, 0, 0])
            bg.add(stripe)

        grid = VGroup()
        for x in [i * 0.5 for i in range(-15, 16)]:
            grid.add(Line([x, -2.2, 0], [x + 0.8, 2.2, 0], stroke_width=0.55, color="#163247"))
        for y in [i * 0.35 for i in range(-7, 8)]:
            grid.add(Line([-7.2, y, 0], [7.2, y + 0.4, 0], stroke_width=0.55, color="#163247"))
        grid.set_opacity(0.36)

        left_trace = VGroup(
            Line([-6.5, -0.9, 0], [-4.7, -0.9, 0]),
            Line([-4.7, -0.9, 0], [-4.2, -0.35, 0]),
            Line([-4.2, -0.35, 0], [-2.4, -0.35, 0]),
            Line([-2.4, -0.35, 0], [-1.9, 0.05, 0]),
        ).set_stroke("#22c55e", width=3.2, opacity=0.86)

        right_trace = VGroup(
            Line([6.5, 0.9, 0], [4.8, 0.9, 0]),
            Line([4.8, 0.9, 0], [4.2, 0.36, 0]),
            Line([4.2, 0.36, 0], [2.3, 0.36, 0]),
            Line([2.3, 0.36, 0], [1.8, -0.04, 0]),
        ).set_stroke("#38bdf8", width=3.2, opacity=0.82)

        nodes = VGroup()
        for point, color in [
            ([-6.5, -0.9, 0], "#22c55e"),
            ([-4.2, -0.35, 0], "#22c55e"),
            ([6.5, 0.9, 0], "#38bdf8"),
            ([4.2, 0.36, 0], "#38bdf8"),
        ]:
            nodes.add(Dot(point, radius=0.055, color=color))

        title_left = Text("Waya", font="DejaVu Sans", weight=BOLD, color="#f8fafc").scale(0.86)
        title_right = Text("ArcRaven", font="DejaVu Sans", weight=BOLD, color="#f8fafc").scale(0.86)
        slash = Text("/", font="DejaVu Sans", weight=BOLD, color="#22c55e").scale(0.9)
        title = VGroup(title_left, slash, title_right).arrange(RIGHT, buff=0.28).move_to([0, 0.55, 0])

        subtitle = Text(
            "CTO  |  Robotics & Intelligent Hardware  |  AI Engineering",
            font="DejaVu Sans",
            color="#cbd5e1",
        ).scale(0.26).next_to(title, DOWN, buff=0.24)

        tags = VGroup(
            Text("Rust", font="DejaVu Sans", color="#a7f3d0"),
            Text("Flutter", font="DejaVu Sans", color="#bfdbfe"),
            Text("STM32C5", font="DejaVu Sans", color="#fde68a"),
            Text("Long-Agent", font="DejaVu Sans", color="#ddd6fe"),
        )
        for tag in tags:
            tag.scale(0.23)
        tags.arrange(RIGHT, buff=0.36).next_to(subtitle, DOWN, buff=0.35)

        underline = Line([-1.55, -0.08, 0], [1.55, -0.08, 0], stroke_width=2.4, color="#22c55e")
        underline.set_opacity(0.78)

        sweep = Line([-7.4, -1.93, 0], [7.4, -1.93, 0], stroke_width=2.5, color="#22c55e")
        sweep.set_opacity(0.0)
        glow = Dot([-7.1, -1.93, 0], radius=0.06, color="#f8fafc").set_opacity(0.0)

        self.add(bg, grid)
        self.play(
            LaggedStart(Create(left_trace), Create(right_trace), FadeIn(nodes), lag_ratio=0.16),
            run_time=0.9,
        )
        self.play(
            FadeIn(title, shift=UP * 0.16),
            Create(underline),
            run_time=0.75,
        )
        self.play(
            FadeIn(subtitle, shift=UP * 0.08),
            LaggedStart(*[FadeIn(tag, shift=UP * 0.08) for tag in tags], lag_ratio=0.12),
            run_time=0.7,
        )
        self.play(
            sweep.animate.set_opacity(0.78),
            glow.animate.set_opacity(1).shift(RIGHT * 14.2),
            run_time=1.35,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.play(glow.animate.set_opacity(0), sweep.animate.set_opacity(0.18), run_time=0.25)
        self.wait(0.5)
