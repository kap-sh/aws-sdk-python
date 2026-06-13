"""Generated from Smithy shape ``com.amazonaws.devopsagent#RecommendationPriority``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Priority level of a recommendation</p>"""
RecommendationPriority: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "MEDIUM",
        "LOW",
    )
)


def serialize_json(value: RecommendationPriority) -> str:
    return value


def deserialize_json(data: str) -> RecommendationPriority:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationPriority value: {data!r}")
    return cast(RecommendationPriority, data)
