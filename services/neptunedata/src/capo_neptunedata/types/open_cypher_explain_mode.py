"""Generated from Smithy shape ``com.amazonaws.neptunedata#OpenCypherExplainMode``."""

from typing import Literal, TypeAlias, cast

OpenCypherExplainMode: TypeAlias = Literal[
    "static",
    "dynamic",
    "details",
]


# --- restJson1 ser/de ---
def serialize_json(value: OpenCypherExplainMode) -> str:
    return value


def deserialize_json(data: str) -> OpenCypherExplainMode:
    return cast(OpenCypherExplainMode, data)
