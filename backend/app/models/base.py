
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Column, Field
from sqlalchemy import DateTime, func


def todays_date_str():
    return str(datetime.now().date())


class DateMixin(SQLModel):
    # Does not work !!
    # Error: sqlalchemy.exc.ArgumentError: Column object 'updated_at' already assigned to Table 'feedback'
    created_at: datetime = Field(default_factory=func.now)
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(), onupdate=func.now)
    )
