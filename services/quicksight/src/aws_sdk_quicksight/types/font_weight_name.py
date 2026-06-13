"""Generated from Smithy shape ``com.amazonaws.quicksight#FontWeightName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FontWeightName: TypeAlias = Literal[
    "NORMAL",
    "BOLD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NORMAL",
        "BOLD",
    )
)


def serialize_json(value: FontWeightName) -> str:
    return value


def deserialize_json(data: str) -> FontWeightName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FontWeightName value: {data!r}")
    return cast(FontWeightName, data)
