"""Generated from Smithy shape ``com.amazonaws.quicksight#GeneratedAnswerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

GeneratedAnswerStatus: TypeAlias = Literal[
    "ANSWER_GENERATED",
    "ANSWER_RETRIEVED",
    "ANSWER_DOWNGRADE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANSWER_GENERATED",
        "ANSWER_RETRIEVED",
        "ANSWER_DOWNGRADE",
    )
)


def serialize_json(value: GeneratedAnswerStatus) -> str:
    return value


def deserialize_json(data: str) -> GeneratedAnswerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeneratedAnswerStatus value: {data!r}")
    return cast(GeneratedAnswerStatus, data)
