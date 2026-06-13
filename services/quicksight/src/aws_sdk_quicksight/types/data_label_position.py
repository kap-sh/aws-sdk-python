"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataLabelPosition: TypeAlias = Literal[
    "INSIDE",
    "OUTSIDE",
    "LEFT",
    "TOP",
    "BOTTOM",
    "RIGHT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSIDE",
        "OUTSIDE",
        "LEFT",
        "TOP",
        "BOTTOM",
        "RIGHT",
    )
)


def serialize_json(value: DataLabelPosition) -> str:
    return value


def deserialize_json(data: str) -> DataLabelPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataLabelPosition value: {data!r}")
    return cast(DataLabelPosition, data)
