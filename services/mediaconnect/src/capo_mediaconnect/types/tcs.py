"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Tcs``."""

from typing import Literal, TypeAlias, cast

Tcs: TypeAlias = Literal[
    "SDR",
    "PQ",
    "HLG",
    "LINEAR",
    "BT2100LINPQ",
    "BT2100LINHLG",
    "ST2065-1",
    "ST428-1",
    "DENSITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: Tcs) -> str:
    return value


def deserialize_json(data: str) -> Tcs:
    return cast(Tcs, data)
