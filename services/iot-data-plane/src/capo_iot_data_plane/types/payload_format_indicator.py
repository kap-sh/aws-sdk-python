"""Generated from Smithy shape ``com.amazonaws.iotdataplane#PayloadFormatIndicator``."""

from typing import Literal, TypeAlias, cast

PayloadFormatIndicator: TypeAlias = Literal[
    "UNSPECIFIED_BYTES",
    "UTF8_DATA",
]


# --- restJson1 ser/de ---
def serialize_json(value: PayloadFormatIndicator) -> str:
    return value


def deserialize_json(data: str) -> PayloadFormatIndicator:
    return cast(PayloadFormatIndicator, data)
