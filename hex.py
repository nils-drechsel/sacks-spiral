import math
import svgwrite
import copy

class hex_histogram:

    """
    A hex histogram to bin points
    """

    def __init__(self, width, height, maxHexagons):
        self.bins = {}
        self.width = width
        self.height = height

        l = max(width, height)
        self.radius = l / maxHexagons
        self.maxHexagons = maxHexagons

        self.dx = self.radius * 2 * math.sin(math.pi / 3)
        self.dy = self.radius * 1.5

    def is_odd(self, n):
        if abs(n % 2) == 1:
            return True
        else:
            return False

    def bin(self, point):
        x = point[0]
        y = point[1]

        py = y / self.dy
        pj = int(round(py))

        offset = 0
        if self.is_odd(pj):
            offset = 0.5

        px = x / self.dx - offset
        pi = int(round(px))
        py1 = py - pj

        if abs(py1) * 3 > 1:
            px1 = px - pi

            if px < pi:
                s = -1
            else:
                s = 1

            pi2 = int(pi + s / 2)

            if py < pj:
                s = -1
            else:
                s = 1

            pj2 = pj + s
            px2 = px - pi2
            py2 = py - pj2
            if px1 * px1 + py1 * py1 > px2 * px2 + py2 * py2:
                sign = -1
                if self.is_odd(pj):
                    sign = 1;
                pi = int(pi2 + sign / 2)
                pj = int(pj2)

        bid = str(pi) + "-" + str(pj)

        if bid in self.bins:
            self.bins[bid][2] += 1
        else:

            offset = 0
            if self.is_odd(pj):
                offset = 0.5

            sx = (pi + offset) * self.dx
            sy = pj * self.dy

            self.bins[bid] = [sx, sy, 1]

    def hex_points(self, radius, x_centre, y_centre):
        result = []

        for i in range(0, 7):
            angle = (math.pi / 3.0) * i

            x = math.sin(angle) * radius
            y = -math.cos(angle) * radius
            result.append([x + x_centre, y + y_centre])

        return result

    def max_count(self):
        m = 0
        for key in self.bins.keys():
            p = self.bins[key]
            m = max(m, p[2])
        return m * m

    def make_svg(self, name):
        m = self.max_count()
        svg = svgwrite.Drawing(name)
        for key in self.bins.keys():
            p = self.bins[key]
            h = self.hex_points(self.radius, p[0], p[1])
            opacity = (float(p[2]) * float(p[2])) / float(m)
            svg.add(svgwrite.shapes.Polygon(h, fill='purple', opacity=opacity))
            svg.add(svgwrite.shapes.Polyline(h, stroke='black', fill='none', stroke_width = '0.1'))

        svg.save()
