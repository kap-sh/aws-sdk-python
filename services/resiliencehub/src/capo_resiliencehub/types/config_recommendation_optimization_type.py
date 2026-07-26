"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ConfigRecommendationOptimizationType``."""

from typing import Literal, TypeAlias, cast

ConfigRecommendationOptimizationType: TypeAlias = Literal[
    "LeastCost",
    "LeastChange",
    "BestAZRecovery",
    "LeastErrors",
    "BestAttainable",
    "BestRegionRecovery",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigRecommendationOptimizationType) -> str:
    return value


def deserialize_json(data: str) -> ConfigRecommendationOptimizationType:
    return cast(ConfigRecommendationOptimizationType, data)
