"""Generated from Smithy shape ``com.amazonaws.datazone#OpenLineageRunState``."""

from typing import Literal, TypeAlias, cast

OpenLineageRunState: TypeAlias = Literal[
    "START",
    "RUNNING",
    "COMPLETE",
    "ABORT",
    "FAIL",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: OpenLineageRunState) -> str:
    return value


def deserialize_json(data: str) -> OpenLineageRunState:
    return cast(OpenLineageRunState, data)
