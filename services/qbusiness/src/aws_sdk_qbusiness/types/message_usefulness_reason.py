"""Generated from Smithy shape ``com.amazonaws.qbusiness#MessageUsefulnessReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

MessageUsefulnessReason: TypeAlias = Literal[
    "NOT_FACTUALLY_CORRECT",
    "HARMFUL_OR_UNSAFE",
    "INCORRECT_OR_MISSING_SOURCES",
    "NOT_HELPFUL",
    "FACTUALLY_CORRECT",
    "COMPLETE",
    "RELEVANT_SOURCES",
    "HELPFUL",
    "NOT_BASED_ON_DOCUMENTS",
    "NOT_COMPLETE",
    "NOT_CONCISE",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_FACTUALLY_CORRECT",
        "HARMFUL_OR_UNSAFE",
        "INCORRECT_OR_MISSING_SOURCES",
        "NOT_HELPFUL",
        "FACTUALLY_CORRECT",
        "COMPLETE",
        "RELEVANT_SOURCES",
        "HELPFUL",
        "NOT_BASED_ON_DOCUMENTS",
        "NOT_COMPLETE",
        "NOT_CONCISE",
        "OTHER",
    )
)


def serialize_json(value: MessageUsefulnessReason) -> str:
    return value


def deserialize_json(data: str) -> MessageUsefulnessReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageUsefulnessReason value: {data!r}")
    return cast(MessageUsefulnessReason, data)
