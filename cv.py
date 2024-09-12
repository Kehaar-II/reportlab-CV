from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import Paragraph, Frame

HEIGHT = 2970
WIDTH = 2100
SIDEBAR = int(WIDTH/3)
BODY_WIDTH = WIDTH - SIDEBAR

H1 = 55
H2 = 35
P = 30

TITLE_BOTTOM_MARGIN = 35

GRAY = Color(0.451, 0.451, 0.451)
DARK_BLUE = Color(0.192,0.231,0.302)
WHITE = Color(1, 1, 1)

NAME = "John Doe"
STATUS = "Lorem ipsum"
DESC = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

SIDEBAR_ITEMS = [
    [
        "Details", [
            [None, "Phone", "418-555-8659 "],
            [None, "Email", "john.doe@mail.com"],
            [None, "Adresse", "1600 Amphitheatre Parkway Mountain View, CA"],
            [None, "Github", "https://github.com/Kehaar-II"],
        ],
    ],
    [
        "Lorem ipsum", [
            [None, None, "Lorem"],
            [None, None, "ipsum"],
            [None, None, "dolor"],
            [None, None, "sit"],
            [None, None, "amet"],
        ],
    ],
    [
        "Lorem ipsum", [
            ["Lorem ipsum dolor sit amet", "Lorem ipsum ", "Lorem"],
        ],
    ]
]

EXEPERIENCE = [
    [
        "Lorem ipsum dolor sit amet",
        [
            [
                "1970 - 1980",
                "Lorem ipsum dolor sit amet",
                "Lorem ipsum",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            ],
        ]
    ],
    [
        "Lorem ipsum dolor sit",
        [
            [
                "1995 - 1997",
                "Lorem ipsum dolor",
                "Lorem",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
            ],
            [
                "1980 - 1995",
                "Lorem ipsum dolor",
                "Lorem",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
            ],
        ]
    ],
]

COMPETANCES = [
    "Lorem ipsum dolor",
    [
        [
            "Lorem",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        ],
        [
            "Lorem",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        ],
    ]
]

# MONTSERRAT = "Montserrat"
# MONTSERRAT_BOLD = "Montserrat-Bold"
MONTSERRAT = "Courier"
MONTSERRAT_BOLD = "Courier-Bold"

def draw_text(str, size, color, font, pos, max_width, justify):
    '''str, int, Color, str, (int, int), int -> int'''
    style_sheet = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        'Custom',
        parent=style_sheet['Normal'],
        fontName=font,
        fontSize=size,
        leading=int(size * 1.2),
        alignment=(TA_JUSTIFY if justify else TA_LEFT),
        textColor=color,
    )
    magic_number = 300
    paragraph = Paragraph(str, custom_style)
    width, height = paragraph.wrap(max_width, 600)
    frame = Frame(pos[0], pos[1] - height - magic_number + size * 1.2, max_width, height + magic_number, showBoundary=True)
    frame.addFromList([paragraph], canvas)

    return pos[1] - height


def setup():
    ''' void -> void'''
    canvas.setPageSize((WIDTH, HEIGHT))
    canvas.setStrokeAlpha(0)

def draw_sidebar():
    ''''void -> void'''
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, 0, SIDEBAR, HEIGHT, fill=1)
    canvas.drawInlineImage("./image.png", 100, HEIGHT - SIDEBAR + 100, SIDEBAR - 200, SIDEBAR - 200)
    left = 100
    box_size = int(SIDEBAR - 100)
    current_height = HEIGHT - SIDEBAR
    canvas.setFillColorRGB(1, 1, 1)


    for section in SIDEBAR_ITEMS:
        current_height = draw_text(section[0], H1, WHITE, MONTSERRAT_BOLD, (left, current_height), box_size, False)
        canvas.rect(left, current_height + H1 * 1.2 - 25, BODY_WIDTH, 8, fill=1)
        current_height -= TITLE_BOTTOM_MARGIN

        for item in section[1]:
            if (item[0] != None):
                current_height = draw_text(item[0], P, WHITE, MONTSERRAT, (left, current_height), box_size, False)

            if (item[1] != None):
                current_height = draw_text(item[1], H2, WHITE, MONTSERRAT_BOLD, (left, current_height), box_size, False)

            if (item[2] != None):
                current_height = draw_text(item[2], P, WHITE, MONTSERRAT, (left, current_height), box_size, False)

            current_height -= 40
        current_height -= 35

def draw_body():
    '''void -> void'''
    left = SIDEBAR + 100
    box_size = int(BODY_WIDTH - 200)
    current_height = HEIGHT - 220

    current_height = draw_text(NAME, H1 * 2, DARK_BLUE, MONTSERRAT_BOLD, (left, current_height), box_size, False) + 40
    current_height = draw_text(STATUS, H1, DARK_BLUE, MONTSERRAT, (left, current_height), box_size, True)
    current_height = draw_text(DESC, H2, DARK_BLUE, MONTSERRAT, (left, current_height), box_size, True)

    left = SIDEBAR + 100
    current_height = HEIGHT - SIDEBAR
    magic_number = 22
    canvas.setFillColor(DARK_BLUE)

    for category in EXEPERIENCE:
        current_height = draw_text(category[0], H1, DARK_BLUE, MONTSERRAT_BOLD, (left, current_height), box_size, True)
        canvas.rect(left, current_height + H1 * 1.2 - 25, BODY_WIDTH, 8, fill=1)
        current_height -= TITLE_BOTTOM_MARGIN

        for stage in category[1]:
            if stage[0] != None:
                current_height = draw_text("• " + stage[0], P, GRAY, MONTSERRAT_BOLD, (left, current_height), box_size, True) - 10
            if stage[1] != None:
                current_height = draw_text(stage[1], P, GRAY, MONTSERRAT, (left + magic_number, current_height), int(BODY_WIDTH - 200 - magic_number), True) - 15
            if stage[2] != None:
                current_height = draw_text(stage[2], P*1.2, GRAY, MONTSERRAT_BOLD, (left + magic_number, current_height), int(BODY_WIDTH - 200 - magic_number), True) - 15
            if stage[3] != None:
                current_height = draw_text(stage[3], P, GRAY, MONTSERRAT, (left + magic_number, current_height), int(BODY_WIDTH - 200 - magic_number), True) - 10
            current_height -= 35
        current_height -= H1

    current_height = draw_text(COMPETANCES[0], H1, DARK_BLUE, MONTSERRAT_BOLD, (left, current_height), box_size, True)
    canvas.rect(left, current_height + H1 * 1.2 - 25, BODY_WIDTH, 8, fill=1)
    current_height -= TITLE_BOTTOM_MARGIN

    for competance in COMPETANCES[1]:
        current_height = draw_text("• " + competance[0], P * 1.2, GRAY, MONTSERRAT_BOLD, (left, current_height), box_size, True) - 15
        current_height = draw_text(competance[1], P, GRAY, MONTSERRAT, (left + magic_number, current_height), int(BODY_WIDTH - 200 - magic_number), True) - 10
        current_height -= 35


# pdfmetrics.registerFont(TTFont(MONTSERRAT, 'Montserrat-Regular.ttf'))
# pdfmetrics.registerFont(TTFont(MONTSERRAT_BOLD, 'Montserrat-Bold.ttf'))
canvas = Canvas("cv.pdf")

setup()
draw_sidebar()
draw_body()
canvas.save()
