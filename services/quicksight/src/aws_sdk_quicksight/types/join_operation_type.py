"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

JoinOperationType: TypeAlias = Literal[
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


def serialize_json(value: JoinOperationType) -> str:
    return value


def deserialize_json(data: str) -> JoinOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JoinOperationType value: {data!r}")
    return cast(JoinOperationType, data)
