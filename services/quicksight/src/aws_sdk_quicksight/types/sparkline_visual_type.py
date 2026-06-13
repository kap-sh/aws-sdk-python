"""Generated from Smithy shape ``com.amazonaws.quicksight#SparklineVisualType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SparklineVisualType: TypeAlias = Literal[
    "LINE",
    "AREA_LINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINE",
        "AREA_LINE",
    )
)


def serialize_json(value: SparklineVisualType) -> str:
    return value


def deserialize_json(data: str) -> SparklineVisualType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SparklineVisualType value: {data!r}")
    return cast(SparklineVisualType, data)
