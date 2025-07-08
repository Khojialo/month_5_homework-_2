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


insert_lesson_themes("Python",[
    Theme(title ="Database"),
    Theme(title ="Sqlalchemy"),
    Theme(title = "Github")
])

