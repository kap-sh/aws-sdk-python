"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelContent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataLabelContent: TypeAlias = Literal[
    "VALUE",
    "PERCENT",
    "VALUE_AND_PERCENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALUE",
        "PERCENT",
        "VALUE_AND_PERCENT",
    )
)


def serialize_json(value: DataLabelContent) -> str:
    return value


def deserialize_json(data: str) -> DataLabelContent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataLabelContent value: {data!r}")
    return cast(DataLabelContent, data)
