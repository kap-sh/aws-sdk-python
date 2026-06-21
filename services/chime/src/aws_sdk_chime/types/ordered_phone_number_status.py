"""Generated from Smithy shape ``com.amazonaws.chime#OrderedPhoneNumberStatus``."""

from typing import Literal, TypeAlias, cast

OrderedPhoneNumberStatus: TypeAlias = Literal[
    "Processing",
    "Acquired",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderedPhoneNumberStatus) -> str:
    return value


def deserialize_json(data: str) -> OrderedPhoneNumberStatus:
    return cast(OrderedPhoneNumberStatus, data)
