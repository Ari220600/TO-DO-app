from flet import *
from custom_checkbox import CustomCheckBox
def main(page: Page):
    BG = "#A1302C"
    FWG = "#F1A8A6"
    FG = "#E1706C"
    COL = "#87F0B9"
    
    task_counts = {
        "Business": 1,
        "Family": 1,
        "Friends": 1
    }
    
    def update_category_cards():
        categories_card.controls.clear()
        categories = ['Business', 'Family', 'Friends']
        for i, category in enumerate(categories):
            categories_card.controls.append(
                Container(
                    bgcolor=BG,
                    height=110,
                    width=170,
                    padding=15,
                    border_radius=20,
                    margin=margin.only(bottom=20),
                    content=Column(
                        controls=[
                            Text(f'{task_counts[category]} Tasks'),
                            Text(category),
                            Container(
                                width=160,
                                height=5,
                                bgcolor='white12',
                                border_radius=10,
                                padding=padding.only(right=(i + 1) * 30),
                                content=Container(
                                    bgcolor=COL,
                                ),
                            )
                        ]
                    )
                )
            )
        page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.route = route_change('/')
        page.go('/')
    clr=["PINK","#87F0B9","#FFCA7B"]
    
    def submit_form(e):
        name = name_input.value
        task = task_input.value
        task_type = type_input.value
        if task_type=="Business":
            n=0
        elif task_type=="Family":
            n=1
        elif task_type=="Friends":
            n=2
        tasks.controls.append(
            Container(
                height=50,
                width=300,
                bgcolor=BG,
                border_radius=10,
                margin=margin.only(right=20),
                padding=padding.only(left=10, top=12),
                content=CustomCheckBox(
                    color=clr[n],
                    size=20,
                    font_size=15,
                    label=f"Task: {task}"
                )
            )
        )
        

        if task_type in task_counts:
            task_counts[task_type] += 1
            update_category_cards()

        page.update()

        page.dialog = AlertDialog(
            title=Text("Form Submitted"),
            content=Text(f"Name: {name}\nTask: {task}\nType: {task_type}"),
            actions=[
                TextButton("OK", on_click=lambda e: close_dialog(e))
            ]
        )
        page.dialog.open = True
        page.update()

    submit_button = ElevatedButton(
        text="Submit",
        width=150,
        height=50,
        color="White",
        bgcolor=BG,
        on_click=submit_form,
    )

    name_input = TextField(
        label="Name",
        width=300,
        height=60,
        border_radius=10,
        bgcolor=BG,
        border_color="White12",
    )
    type_input = Dropdown(
        label="Type",
        width=400,
        height=60,
        bgcolor=BG,
        options=[
            dropdown.Option("Business"),
            dropdown.Option("Family"),
            dropdown.Option("Friends")
        ],
        border_radius=10,
        border_color="White12",
    )
    task_input = TextField(
        label="Task Description",
        bgcolor=BG,
        multiline=True,
        width=400,
        height=60,
        border_radius=10,
        border_color="White12",
    )

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', "PINK"],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                    alignment='center',
                    controls=[
                        Container(
                            padding=padding.all(5),
                            bgcolor=BG,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=Container(
                                bgcolor=FG,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_src="https://th.bing.com/th/id/OIP.dsiC7a1xQd-CPZpBuMeCDgAAAA?rs=1&pid=ImgDetMain"
                                )
                            )
                        )
                    ],
                ),
            ),
        ]
    )

    def Shrinks(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        page_2.controls[0].border_radius = border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 320
        page_2.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right
        )
        page_2.update()

    categories_card = Row(
        scroll='auto'
    )

    create_task_view = Container(
        width=320,
        height=680,
        bgcolor=FG,
        border_radius=35,
        padding=padding.only(top=60, left=50, right=100),
        content=Column(
            controls=[
                Container(
                    content=Container(
                        on_click=lambda _: page.go('/'),
                        height=40,
                        width=40,
                        border=border.all(color="white", width=1),
                        border_radius=50,
                        margin=margin.only(bottom=10),
                        padding=padding.only(top=9, left=15),
                        content=Text('x', weight="bold",)
                    )
                ),
                name_input,
                type_input,
                task_input,
                Container(
                    submit_button,
                    alignment=alignment.center,
                )
            ]
        )
    )

    tasks = Column(
        height=300,
        scroll='auto',
    )

    demo_tasks = ["Task 1", "Task 2", "Task 3"]
    num=0
    for task in demo_tasks:
        tasks.controls.append(
            Container(
                height=50,
                width=300,
                bgcolor=BG,
                border_radius=10,
                margin=margin.only(right=20),
                padding=padding.only(left=10, top=12),
                content=CustomCheckBox(
                    color=clr[num%3],
                    size=20,
                    font_size=15,
                    label=f"Task: {task}"
                )
            )
        )
        num=num+1

    update_category_cards()

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(
                            on_click=lambda e: Shrinks(e),
                            content=Icon(
                                icons.MENU
                            )
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                Text(
                    value='What\'s up, Leo!',
                    size=30
                ),
                Text(
                    value='CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card
                ),
                Text("Today's Tasks"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            icon=icons.ADD,
                            on_click=lambda _: page.go('/create_task'),
                            bgcolor=FWG,
                            bottom=0,  # Ensure it is within visible area
                            right=20,  # Ensure it is within visible area
                        ),
                    ]
                )
            ]
        )
    )

    page_1 = Container(
        width=320,
        height=680,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(top=60, left=50, right=100),
        content=Column(
            controls=[
                Row(
                    alignment='end',
                    controls=[
                        Container(
                            on_click=lambda e: restore(e),
                            height=30,
                            width=30,
                            border_radius=25,
                            padding=padding.only(top=3, left=8),
                            border=border.all(color="white", width=1),
                            content=Text("<")
                        )
                    ]
                ),
                Container(height=20),
                circle,
                Text('Arindam\nChakraborty', size=20, weight='bold'),
                Container(height=25),
                Row(
                    controls=[
                        Icon(icons.FAVORITE_BORDER_SHARP, color='white60'),
                        Text('Unmarried', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CARD_TRAVEL, color='white60'),
                        Text('Software Engineer', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CALCULATE_OUTLINED, color='white60'),
                        Text('B.Tech Graduate', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                    ]
                ),
                Image(
                    src="images\\1.png",
                    width=300,
                    height=200,
                ),
                Text('Good', color=FG, font_family='poppins',),
                Text('Consistency', size=22,)
            ]
        )
    )

    page_2 = Row(
        alignment='end',
        controls=[
            Container(
                width=320,
                height=680,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.EASE),
                animate_scale=animation.Animation(400, curve='ease'),
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width=320,
        height=680,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )

    pages = {
        '/': View(
            "/",
            [
                container
            ],
        ),
        '/create_task': View(
            "/create_task",
            [
                create_task_view
            ],
        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.route = route_change('/')
    page.go('/')
    page.on_route_change = route_change
    page.go(page.route)

app(target=main)
