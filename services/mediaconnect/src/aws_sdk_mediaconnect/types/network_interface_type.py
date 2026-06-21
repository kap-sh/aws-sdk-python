"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NetworkInterfaceType``."""

from typing import Literal, TypeAlias, cast

NetworkInterfaceType: TypeAlias = Literal[
    "ena",
    "efa",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaceType) -> str:
    return value


def deserialize_json(data: str) -> NetworkInterfaceType:
    return cast(NetworkInterfaceType, data)
