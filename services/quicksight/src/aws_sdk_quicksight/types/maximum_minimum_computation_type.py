"""Generated from Smithy shape ``com.amazonaws.quicksight#MaximumMinimumComputationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

MaximumMinimumComputationType: TypeAlias = Literal[
    "MAXIMUM",
    "MINIMUM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAXIMUM",
        "MINIMUM",
    )
)


def serialize_json(value: MaximumMinimumComputationType) -> str:
    return value


def deserialize_json(data: str) -> MaximumMinimumComputationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MaximumMinimumComputationType value: {data!r}"
        )
    return cast(MaximumMinimumComputationType, data)
