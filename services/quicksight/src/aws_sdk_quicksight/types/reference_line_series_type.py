"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineSeriesType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ReferenceLineSeriesType: TypeAlias = Literal[
    "BAR",
    "LINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BAR",
        "LINE",
    )
)


def serialize_json(value: ReferenceLineSeriesType) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLineSeriesType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReferenceLineSeriesType value: {data!r}")
    return cast(ReferenceLineSeriesType, data)
