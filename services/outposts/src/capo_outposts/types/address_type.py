"""Generated from Smithy shape ``com.amazonaws.outposts#AddressType``."""

from typing import Literal, TypeAlias, cast

AddressType: TypeAlias = Literal[
    "SHIPPING_ADDRESS",
    "OPERATING_ADDRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AddressType) -> str:
    return value


def deserialize_json(data: str) -> AddressType:
    return cast(AddressType, data)
