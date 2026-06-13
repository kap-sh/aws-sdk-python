"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineLabelHorizontalPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ReferenceLineLabelHorizontalPosition: TypeAlias = Literal[
    "LEFT",
    "CENTER",
    "RIGHT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEFT",
        "CENTER",
        "RIGHT",
    )
)


def serialize_json(value: ReferenceLineLabelHorizontalPosition) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLineLabelHorizontalPosition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReferenceLineLabelHorizontalPosition value: {data!r}"
        )
    return cast(ReferenceLineLabelHorizontalPosition, data)
