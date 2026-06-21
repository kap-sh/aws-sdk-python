"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#NetworkType``."""

from typing import Literal, TypeAlias, cast

NetworkType: TypeAlias = Literal[
    "IPV4_ONLY",
    "DUAL_STACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkType) -> str:
    return value


def deserialize_json(data: str) -> NetworkType:
    return cast(NetworkType, data)
