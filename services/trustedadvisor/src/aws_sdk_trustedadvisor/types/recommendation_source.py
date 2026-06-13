"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

RecommendationSource: TypeAlias = Literal[
    "aws_config",
    "compute_optimizer",
    "cost_explorer",
    "lse",
    "manual",
    "pse",
    "rds",
    "resilience",
    "resilience_hub",
    "security_hub",
    "stir",
    "ta_check",
    "well_architected",
    "cost_optimization_hub",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "aws_config",
        "compute_optimizer",
        "cost_explorer",
        "lse",
        "manual",
        "pse",
        "rds",
        "resilience",
        "resilience_hub",
        "security_hub",
        "stir",
        "ta_check",
        "well_architected",
        "cost_optimization_hub",
    )
)


def serialize_json(value: RecommendationSource) -> str:
    return value


def deserialize_json(data: str) -> RecommendationSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationSource value: {data!r}")
    return cast(RecommendationSource, data)
