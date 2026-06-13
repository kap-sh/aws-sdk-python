"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopBottomSortOrder: TypeAlias = Literal[
    "PERCENT_DIFFERENCE",
    "ABSOLUTE_DIFFERENCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERCENT_DIFFERENCE",
        "ABSOLUTE_DIFFERENCE",
    )
)


def serialize_json(value: TopBottomSortOrder) -> str:
    return value


def deserialize_json(data: str) -> TopBottomSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopBottomSortOrder value: {data!r}")
    return cast(TopBottomSortOrder, data)
