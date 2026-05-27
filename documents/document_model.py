from datetime import date

from pydantic import BaseModel


class NidDocument(BaseModel):
    nid_number: str
    name: str
    dob: date
    province: str
    district: str
    municipality: str
