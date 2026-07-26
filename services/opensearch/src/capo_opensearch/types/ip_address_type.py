"""Generated from Smithy shape ``com.amazonaws.opensearch#IPAddressType``."""

from typing import Literal, TypeAlias, cast

IPAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
]


# --- restJson1 ser/de ---
def serialize_json(value: IPAddressType) -> str:
    return value


def deserialize_json(data: str) -> IPAddressType:
    return cast(IPAddressType, data)
