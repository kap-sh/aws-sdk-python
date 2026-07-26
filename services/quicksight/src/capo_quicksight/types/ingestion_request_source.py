"""Generated from Smithy shape ``com.amazonaws.quicksight#IngestionRequestSource``."""

from typing import Literal, TypeAlias, cast

IngestionRequestSource: TypeAlias = Literal[
    "MANUAL",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionRequestSource) -> str:
    return value


def deserialize_json(data: str) -> IngestionRequestSource:
    return cast(IngestionRequestSource, data)
