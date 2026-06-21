"""Generated from Smithy shape ``com.amazonaws.xray#TraceFormatType``."""

from typing import Literal, TypeAlias, cast

TraceFormatType: TypeAlias = Literal[
    "XRAY",
    "OTEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TraceFormatType) -> str:
    return value


def deserialize_json(data: str) -> TraceFormatType:
    return cast(TraceFormatType, data)
