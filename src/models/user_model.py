import datetime

from src.core.db import Model

from sqlalchemy import DateTime, ForeignKey, func, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), index=True)
    role: Mapped["Role"] = relationship(backref="users")
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=False), server_default=func.now()
    )
    updated_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=False),
    )
    last_login: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=False))


class Role(Model):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(40))
    permissions: Mapped[str] = mapped_column(String(100))
    users: Mapped[list["User"]] = relationship(backref="role")
