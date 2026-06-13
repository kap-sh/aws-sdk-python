"""Generated from Smithy shape ``com.amazonaws.quicksight#IngestionRequestType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

"""This defines the type of ingestion request. This is returned as part of create ingestion response."""
IngestionRequestType: TypeAlias = Literal[
    "INITIAL_INGESTION",
    "EDIT",
    "INCREMENTAL_REFRESH",
    "FULL_REFRESH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIAL_INGESTION",
        "EDIT",
        "INCREMENTAL_REFRESH",
        "FULL_REFRESH",
    )
)


def serialize_json(value: IngestionRequestType) -> str:
    return value


def deserialize_json(data: str) -> IngestionRequestType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionRequestType value: {data!r}")
    return cast(IngestionRequestType, data)
