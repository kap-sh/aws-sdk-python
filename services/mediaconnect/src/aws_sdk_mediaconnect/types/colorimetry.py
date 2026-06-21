"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Colorimetry``."""

from typing import Literal, TypeAlias, cast

Colorimetry: TypeAlias = Literal[
    "BT601",
    "BT709",
    "BT2020",
    "BT2100",
    "ST2065-1",
    "ST2065-3",
    "XYZ",
]


# --- restJson1 ser/de ---
def serialize_json(value: Colorimetry) -> str:
    return value


def deserialize_json(data: str) -> Colorimetry:
    return cast(Colorimetry, data)
