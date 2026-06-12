"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Question``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

Question: TypeAlias = Literal[
    "UNANSWERED",
    "ANSWERED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNANSWERED",
        "ANSWERED",
    )
)


def serialize_json(value: Question) -> str:
    return value


def deserialize_json(data: str) -> Question:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Question value: {data!r}")
    return cast(Question, data)
