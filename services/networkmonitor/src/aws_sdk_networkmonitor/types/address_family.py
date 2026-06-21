"""Generated from Smithy shape ``com.amazonaws.networkmonitor#AddressFamily``."""

from typing import Literal, TypeAlias, cast

AddressFamily: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- restJson1 ser/de ---
def serialize_json(value: AddressFamily) -> str:
    return value


def deserialize_json(data: str) -> AddressFamily:
    return cast(AddressFamily, data)
