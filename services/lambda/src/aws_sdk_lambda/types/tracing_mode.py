"""Generated from Smithy shape ``com.amazonaws.lambda#TracingMode``."""

from typing import Literal, TypeAlias, cast

TracingMode: TypeAlias = Literal[
    "Active",
    "PassThrough",
]


# --- restJson1 ser/de ---
def serialize_json(value: TracingMode) -> str:
    return value


def deserialize_json(data: str) -> TracingMode:
    return cast(TracingMode, data)
