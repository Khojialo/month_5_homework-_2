from sqlalchemy import String, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Lesson(Base):
    __tablename__ = "dars"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50))
    themes:Mapped[list["Theme"]] = relationship(back_populates="lesson")

    def __repr__(self):
        return f"Dars id:{self.id}.Dars nomi:{self.name}"

class Theme(Base):
    __tablename__ = "Mavzu"
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(50))
    lesson_id:Mapped[int] = mapped_column(ForeignKey("dars.id"))
    lesson:Mapped["Lesson"] = relationship(back_populates="themes")

    def __repr__(self):
        return f"Mavzu id:{self.id}.Mavzu title:{self.title}"

engine = create_engine("sqlite:///./lesson.db")
Base.metadata.create_all(engine)



