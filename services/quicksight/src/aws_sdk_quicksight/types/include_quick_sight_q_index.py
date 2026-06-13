"""Generated from Smithy shape ``com.amazonaws.quicksight#IncludeQuickSightQIndex``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

IncludeQuickSightQIndex: TypeAlias = Literal[
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


def serialize_json(value: IncludeQuickSightQIndex) -> str:
    return value


def deserialize_json(data: str) -> IncludeQuickSightQIndex:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludeQuickSightQIndex value: {data!r}")
    return cast(IncludeQuickSightQIndex, data)
