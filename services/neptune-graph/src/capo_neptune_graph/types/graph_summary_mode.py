"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphSummaryMode``."""

from typing import Literal, TypeAlias, cast

GraphSummaryMode: TypeAlias = Literal[
    "BASIC",
    "DETAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphSummaryMode) -> str:
    return value


def deserialize_json(data: str) -> GraphSummaryMode:
    return cast(GraphSummaryMode, data)
