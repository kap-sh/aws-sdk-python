"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomComputationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopBottomComputationType: TypeAlias = Literal[
    "TOP",
    "BOTTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOP",
        "BOTTOM",
    )
)


def serialize_json(value: TopBottomComputationType) -> str:
    return value


def deserialize_json(data: str) -> TopBottomComputationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopBottomComputationType value: {data!r}")
    return cast(TopBottomComputationType, data)
