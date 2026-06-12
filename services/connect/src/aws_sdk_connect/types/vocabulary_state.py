"""Generated from Smithy shape ``com.amazonaws.connect#VocabularyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

VocabularyState: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "ACTIVE",
    "CREATION_FAILED",
    "DELETE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_IN_PROGRESS",
        "ACTIVE",
        "CREATION_FAILED",
        "DELETE_IN_PROGRESS",
    )
)


def serialize_json(value: VocabularyState) -> str:
    return value


def deserialize_json(data: str) -> VocabularyState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VocabularyState value: {data!r}")
    return cast(VocabularyState, data)
