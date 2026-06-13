"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

JoinType: TypeAlias = Literal[
    "INNER",
    "OUTER",
    "LEFT",
    "RIGHT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INNER",
        "OUTER",
        "LEFT",
        "RIGHT",
    )
)


def serialize_json(value: JoinType) -> str:
    return value


def deserialize_json(data: str) -> JoinType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JoinType value: {data!r}")
    return cast(JoinType, data)
