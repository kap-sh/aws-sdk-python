"""Generated from Smithy shape ``com.amazonaws.mediapackage#UtcTiming``."""

from typing import Literal, TypeAlias, cast

UtcTiming: TypeAlias = Literal[
    "NONE",
    "HTTP-HEAD",
    "HTTP-ISO",
    "HTTP-XSDATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UtcTiming) -> str:
    return value


def deserialize_json(data: str) -> UtcTiming:
    return cast(UtcTiming, data)
