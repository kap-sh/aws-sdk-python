"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The lifecycle status of a recommendation.</p>"""
RecommendationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "DELETING",
    )
)


def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationStatus value: {data!r}")
    return cast(RecommendationStatus, data)
