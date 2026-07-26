"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberOrderType``."""

from typing import Literal, TypeAlias, cast

PhoneNumberOrderType: TypeAlias = Literal[
    "New",
    "Porting",
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberOrderType) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberOrderType:
    return cast(PhoneNumberOrderType, data)
