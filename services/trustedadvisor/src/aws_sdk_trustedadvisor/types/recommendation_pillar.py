"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationPillar``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

RecommendationPillar: TypeAlias = Literal[
    "cost_optimizing",
    "performance",
    "security",
    "service_limits",
    "fault_tolerance",
    "operational_excellence",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cost_optimizing",
        "performance",
        "security",
        "service_limits",
        "fault_tolerance",
        "operational_excellence",
    )
)


def serialize_json(value: RecommendationPillar) -> str:
    return value


def deserialize_json(data: str) -> RecommendationPillar:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationPillar value: {data!r}")
    return cast(RecommendationPillar, data)
