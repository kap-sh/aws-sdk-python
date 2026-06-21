"""Generated from Smithy shape ``com.amazonaws.quicksight#IngestionType``."""

from typing import Literal, TypeAlias, cast

"""This defines the type of ingestion user wants to trigger. This is part of create ingestion request."""
IngestionType: TypeAlias = Literal[
    "INCREMENTAL_REFRESH",
    "FULL_REFRESH",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionType) -> str:
    return value


def deserialize_json(data: str) -> IngestionType:
    return cast(IngestionType, data)
