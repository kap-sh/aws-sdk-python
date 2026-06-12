"""Generated from Smithy shape ``com.amazonaws.account#AccountCreatedDate``."""

import datetime
from typing import TypeAlias

AccountCreatedDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: AccountCreatedDate) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> AccountCreatedDate:
    return datetime.datetime.fromisoformat(data)
