"""Generated from Smithy shape ``com.amazonaws.connect#PhoneType``."""

from typing import Literal, TypeAlias, cast

PhoneType: TypeAlias = Literal[
    "SOFT_PHONE",
    "DESK_PHONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneType) -> str:
    return value


def deserialize_json(data: str) -> PhoneType:
    return cast(PhoneType, data)
