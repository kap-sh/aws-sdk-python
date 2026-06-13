"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineLabelVerticalPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ReferenceLineLabelVerticalPosition: TypeAlias = Literal[
    "ABOVE",
    "BELOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ABOVE",
        "BELOW",
    )
)


def serialize_json(value: ReferenceLineLabelVerticalPosition) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLineLabelVerticalPosition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReferenceLineLabelVerticalPosition value: {data!r}"
        )
    return cast(ReferenceLineLabelVerticalPosition, data)
