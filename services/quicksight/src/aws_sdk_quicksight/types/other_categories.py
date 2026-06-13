"""Generated from Smithy shape ``com.amazonaws.quicksight#OtherCategories``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

OtherCategories: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: OtherCategories) -> str:
    return value


def deserialize_json(data: str) -> OtherCategories:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OtherCategories value: {data!r}")
    return cast(OtherCategories, data)
