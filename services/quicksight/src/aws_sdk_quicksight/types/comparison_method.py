"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparisonMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ComparisonMethod: TypeAlias = Literal[
    "DIFFERENCE",
    "PERCENT_DIFFERENCE",
    "PERCENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIFFERENCE",
        "PERCENT_DIFFERENCE",
        "PERCENT",
    )
)


def serialize_json(value: ComparisonMethod) -> str:
    return value


def deserialize_json(data: str) -> ComparisonMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonMethod value: {data!r}")
    return cast(ComparisonMethod, data)
