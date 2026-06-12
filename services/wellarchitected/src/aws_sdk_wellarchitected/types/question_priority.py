"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionPriority``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

QuestionPriority: TypeAlias = Literal[
    "PRIORITIZED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIORITIZED",
        "NONE",
    )
)


def serialize_json(value: QuestionPriority) -> str:
    return value


def deserialize_json(data: str) -> QuestionPriority:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuestionPriority value: {data!r}")
    return cast(QuestionPriority, data)
