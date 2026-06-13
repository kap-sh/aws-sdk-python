"""Generated from Smithy shape ``com.amazonaws.quicksight#IngestionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

"""This defines the type of ingestion user wants to trigger. This is part of create ingestion request."""
IngestionType: TypeAlias = Literal[
    "INCREMENTAL_REFRESH",
    "FULL_REFRESH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCREMENTAL_REFRESH",
        "FULL_REFRESH",
    )
)


def serialize_json(value: IngestionType) -> str:
    return value


def deserialize_json(data: str) -> IngestionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionType value: {data!r}")
    return cast(IngestionType, data)
