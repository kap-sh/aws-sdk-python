"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExplainMode``."""

from typing import Literal, TypeAlias, cast

ExplainMode: TypeAlias = Literal[
    "STATIC",
    "DETAILS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExplainMode) -> str:
    return value


def deserialize_json(data: str) -> ExplainMode:
    return cast(ExplainMode, data)
