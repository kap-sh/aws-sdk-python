"""Generated from Smithy shape ``com.amazonaws.kendra#ScoreConfidence``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

"""Enumeration for query score confidence."""
ScoreConfidence: TypeAlias = Literal[
    "VERY_HIGH",
    "HIGH",
    "MEDIUM",
    "LOW",
    "NOT_AVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERY_HIGH",
        "HIGH",
        "MEDIUM",
        "LOW",
        "NOT_AVAILABLE",
    )
)


def serialize_aws_json_1_1(value: ScoreConfidence) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScoreConfidence:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScoreConfidence value: {data!r}")
    return cast(ScoreConfidence, data)
