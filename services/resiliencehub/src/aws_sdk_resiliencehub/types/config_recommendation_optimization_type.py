"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ConfigRecommendationOptimizationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ConfigRecommendationOptimizationType: TypeAlias = Literal[
    "LeastCost",
    "LeastChange",
    "BestAZRecovery",
    "LeastErrors",
    "BestAttainable",
    "BestRegionRecovery",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LeastCost",
        "LeastChange",
        "BestAZRecovery",
        "LeastErrors",
        "BestAttainable",
        "BestRegionRecovery",
    )
)


def serialize_json(value: ConfigRecommendationOptimizationType) -> str:
    return value


def deserialize_json(data: str) -> ConfigRecommendationOptimizationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigRecommendationOptimizationType value: {data!r}"
        )
    return cast(ConfigRecommendationOptimizationType, data)
