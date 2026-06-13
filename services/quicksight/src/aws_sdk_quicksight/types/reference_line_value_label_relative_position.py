"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineValueLabelRelativePosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ReferenceLineValueLabelRelativePosition: TypeAlias = Literal[
    "BEFORE_CUSTOM_LABEL",
    "AFTER_CUSTOM_LABEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEFORE_CUSTOM_LABEL",
        "AFTER_CUSTOM_LABEL",
    )
)


def serialize_json(value: ReferenceLineValueLabelRelativePosition) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLineValueLabelRelativePosition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReferenceLineValueLabelRelativePosition value: {data!r}"
        )
    return cast(ReferenceLineValueLabelRelativePosition, data)
