"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberType``."""

from typing import Literal, TypeAlias, cast

PhoneNumberType: TypeAlias = Literal[
    "Local",
    "TollFree",
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberType) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberType:
    return cast(PhoneNumberType, data)
