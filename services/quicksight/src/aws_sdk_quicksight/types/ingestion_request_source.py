"""Generated from Smithy shape ``com.amazonaws.quicksight#IngestionRequestSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

IngestionRequestSource: TypeAlias = Literal[
    "MANUAL",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANUAL",
        "SCHEDULED",
    )
)


def serialize_json(value: IngestionRequestSource) -> str:
    return value


def deserialize_json(data: str) -> IngestionRequestSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionRequestSource value: {data!r}")
    return cast(IngestionRequestSource, data)
