"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AnswerReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

AnswerReason: TypeAlias = Literal[
    "OUT_OF_SCOPE",
    "BUSINESS_PRIORITIES",
    "ARCHITECTURE_CONSTRAINTS",
    "OTHER",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OUT_OF_SCOPE",
        "BUSINESS_PRIORITIES",
        "ARCHITECTURE_CONSTRAINTS",
        "OTHER",
        "NONE",
    )
)


def serialize_json(value: AnswerReason) -> str:
    return value


def deserialize_json(data: str) -> AnswerReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnswerReason value: {data!r}")
    return cast(AnswerReason, data)
