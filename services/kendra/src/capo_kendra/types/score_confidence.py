"""Generated from Smithy shape ``com.amazonaws.kendra#ScoreConfidence``."""

from typing import Literal, TypeAlias, cast

"""Enumeration for query score confidence."""
ScoreConfidence: TypeAlias = Literal[
    "VERY_HIGH",
    "HIGH",
    "MEDIUM",
    "LOW",
    "NOT_AVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScoreConfidence) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScoreConfidence:
    return cast(ScoreConfidence, data)
