"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceSearchOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SpaceSearchOperator: TypeAlias = Literal[
    "STRING_EQUALS",
    "STRING_LIKE",
    "NUMBER_RANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING_EQUALS",
        "STRING_LIKE",
        "NUMBER_RANGE",
    )
)


def serialize_json(value: SpaceSearchOperator) -> str:
    return value


def deserialize_json(data: str) -> SpaceSearchOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SpaceSearchOperator value: {data!r}")
    return cast(SpaceSearchOperator, data)
