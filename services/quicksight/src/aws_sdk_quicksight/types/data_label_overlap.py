"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelOverlap``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataLabelOverlap: TypeAlias = Literal[
    "DISABLE_OVERLAP",
    "ENABLE_OVERLAP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLE_OVERLAP",
        "ENABLE_OVERLAP",
    )
)


def serialize_json(value: DataLabelOverlap) -> str:
    return value


def deserialize_json(data: str) -> DataLabelOverlap:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataLabelOverlap value: {data!r}")
    return cast(DataLabelOverlap, data)
