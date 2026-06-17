from __future__ import annotations

import math
import random

from manim import *


config.pixel_width = 1000
config.pixel_height = 300
config.frame_width = 10
config.frame_height = 3
config.background_color = "#f6f6f1"


class OpenAIAsciiBanner(Scene):
    def construct(self):
        ink = ManimColor("#171717")
        muted = ManimColor("#676762")
        faint = ManimColor("#b8b8ad")
        soft = ManimColor("#deded6")

        border = Rectangle(width=8.75, height=1.84, stroke_color=ink, stroke_width=2)
        border.move_to(ORIGIN + 0.02 * DOWN)
        border.set_z_index(4)

        ticks = VGroup()
        for i in range(43):
            x = -4.375 + i * (8.75 / 42)
            tick_len = 0.07 if i % 3 == 0 else 0.045
            ticks.add(Line([x, 0.94, 0], [x, 0.94 + tick_len, 0], color=ink, stroke_width=1))
            ticks.add(Line([x, -0.90, 0], [x, -0.90 - tick_len, 0], color=ink, stroke_width=1))

        rng = random.Random(20260617)
        ascii_field = VGroup()
        chars = " .:-=+*#"
        for row in range(9):
            for col in range(41):
                x = -4.1 + col * 0.205
                y = 0.62 - row * 0.18
                if -2.95 < x < 2.95 and -0.70 < y < 0.70:
                    continue
                dx = x / 5
                dy = y / 1.5
                density = max(0, 1 - math.sqrt(dx * dx * 2.2 + dy * dy * 2.8)) + rng.random() * 0.15
                if density < 0.45:
                    continue
                char = chars[min(len(chars) - 1, int(density * len(chars)))]
                glyph = Text(char, font="JetBrains Mono", font_size=14, color=faint)
                glyph.set_opacity(0.45)
                glyph.move_to([x, y, 0])
                ascii_field.add(glyph)

        title = Text("Waya / ArcRaven", font="JetBrains Mono", weight=BOLD, font_size=48, color=ink)
        title.move_to([0, 0.30, 0])
        title.set_z_index(3)

        subtitle = Text(
            "CTO  ·  embedded systems  ·  AI agents  ·  robotics",
            font="JetBrains Mono",
            font_size=18,
            color=muted,
        )
        subtitle.move_to([0, -0.08, 0])
        subtitle.set_z_index(3)

        tags = Text("Rust    Flutter    STM32C5    Linux", font="JetBrains Mono", weight=BOLD, font_size=20, color=ink)
        tags.move_to([0, -0.48, 0])
        tags.set_z_index(3)

        footer = Text(
            "build small systems that become real products",
            font="JetBrains Mono",
            font_size=10,
            color=muted,
        )
        footer.move_to([0, -1.25, 0])

        left_marks = VGroup(
            Text("[", font="JetBrains Mono", font_size=22, color=muted).move_to([-3.55, 0.30, 0]),
            Text("{", font="JetBrains Mono", font_size=22, color=faint).move_to([-3.27, -0.08, 0]),
        )
        right_marks = VGroup(
            Text("]", font="JetBrains Mono", font_size=22, color=muted).move_to([3.55, 0.30, 0]),
            Text("}", font="JetBrains Mono", font_size=22, color=faint).move_to([3.27, -0.08, 0]),
        )
        center_marks = Text("::", font="JetBrains Mono", font_size=20, color=muted).move_to([0, -0.48, 0])

        scan = Rectangle(width=0.026, height=1.58, fill_color=faint, fill_opacity=0.70, stroke_width=0)
        scan.move_to([-4.22, 0.02, 0])
        ghost_a = Rectangle(width=0.012, height=1.38, fill_color=soft, fill_opacity=1, stroke_width=0)
        ghost_b = ghost_a.copy()
        ghost_a.next_to(scan, LEFT, buff=0.22)
        ghost_b.next_to(scan, RIGHT, buff=0.22)
        scanner = VGroup(ghost_a, scan, ghost_b)
        scanner.set_z_index(1)
        ascii_field.set_z_index(0)
        ticks.set_z_index(4)

        self.add(ascii_field, scanner, border, ticks, left_marks, right_marks, center_marks, footer)
        self.play(
            FadeIn(title, shift=0.08 * UP),
            FadeIn(subtitle, shift=0.06 * UP),
            FadeIn(tags, shift=0.06 * UP),
            run_time=0.7,
        )
        self.play(
            scanner.animate.shift(RIGHT * 8.44),
            ascii_field.animate.shift(0.08 * RIGHT).set_opacity(0.85),
            run_time=2.2,
            rate_func=linear,
        )
        self.play(scanner.animate.shift(LEFT * 8.44), ascii_field.animate.shift(0.08 * LEFT), run_time=0.01)
        self.play(
            scanner.animate.shift(RIGHT * 8.44),
            ascii_field.animate.shift(0.08 * RIGHT).set_opacity(1),
            run_time=2.2,
            rate_func=linear,
        )
        self.wait(0.25)
