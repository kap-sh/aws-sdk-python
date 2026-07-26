"""Generated from Smithy shape ``com.amazonaws.quicksight#IngestionRequestType``."""

from typing import Literal, TypeAlias, cast

"""This defines the type of ingestion request. This is returned as part of create ingestion response."""
IngestionRequestType: TypeAlias = Literal[
    "INITIAL_INGESTION",
    "EDIT",
    "INCREMENTAL_REFRESH",
    "FULL_REFRESH",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionRequestType) -> str:
    return value


def deserialize_json(data: str) -> IngestionRequestType:
    return cast(IngestionRequestType, data)
