from typing import Optional,List
from sqlalchemy import  select
from sqlalchemy.orm import Session

from database import Theme, engine, Lesson


def insert_lesson_themes(lesson_name:str,themes:Optional[List[Theme]]=None):
    with Session(engine) as ss:
        ss.query(Lesson).delete()
        ss.query(Theme).delete()
        less = Lesson(name=lesson_name)
        if themes:
            for t in themes:
                t.lesson = less
            less.themes = themes
        ss.add(less)
        ss.commit()


# insert_lesson_themes("Python",[
#     Theme(title ="Database"),
#     Theme(title ="Sqlalchemy"),
#     Theme(title = "Github")
# ])

def show_all_lessons():
    with Session(engine) as ss:
        stmt = select(Lesson)
        lessons = ss.scalars(stmt)
        for lesson in lessons:
            print(lesson)
            for theme in lesson.themes:
                print(f"Mavzu id:{theme.id} Mavzu nomi:{theme.title}")

show_all_lessons()


def update_info_themes(theme_id:int,new_theme_title:str) -> Theme:
    with Session(engine) as ss:
        stmt = select(Theme).where(Theme.id ==theme_id)
        theme = ss.scalar(stmt)
        theme.title = new_theme_title
        ss.commit()
        ss.refresh(theme)
        return theme

# update_info_themes(1,"Database.sql")


