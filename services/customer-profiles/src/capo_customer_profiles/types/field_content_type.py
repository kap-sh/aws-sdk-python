"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FieldContentType``."""

from typing import Literal, TypeAlias, cast

FieldContentType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
    "PHONE_NUMBER",
    "EMAIL_ADDRESS",
    "NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldContentType) -> str:
    return value


def deserialize_json(data: str) -> FieldContentType:
    return cast(FieldContentType, data)
