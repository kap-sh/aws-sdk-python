"""Generated from Smithy shape ``com.amazonaws.neptunedata#GraphSummaryType``."""

from typing import Literal, TypeAlias, cast

GraphSummaryType: TypeAlias = Literal[
    "basic",
    "detailed",
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphSummaryType) -> str:
    return value


def deserialize_json(data: str) -> GraphSummaryType:
    return cast(GraphSummaryType, data)
