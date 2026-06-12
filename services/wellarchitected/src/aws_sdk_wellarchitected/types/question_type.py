"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

QuestionType: TypeAlias = Literal[
    "PRIORITIZED",
    "NON_PRIORITIZED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIORITIZED",
        "NON_PRIORITIZED",
    )
)


def serialize_json(value: QuestionType) -> str:
    return value


def deserialize_json(data: str) -> QuestionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuestionType value: {data!r}")
    return cast(QuestionType, data)
