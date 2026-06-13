"""Generated from Smithy shape ``com.amazonaws.qbusiness#ScoreConfidence``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ScoreConfidence: TypeAlias = Literal[
    "VERY_HIGH",
    "HIGH",
    "MEDIUM",
    "LOW",
    "NOT_AVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERY_HIGH",
        "HIGH",
        "MEDIUM",
        "LOW",
        "NOT_AVAILABLE",
    )
)


def serialize_json(value: ScoreConfidence) -> str:
    return value


def deserialize_json(data: str) -> ScoreConfidence:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScoreConfidence value: {data!r}")
    return cast(ScoreConfidence, data)
