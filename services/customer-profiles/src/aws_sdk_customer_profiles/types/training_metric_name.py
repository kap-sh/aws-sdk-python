"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TrainingMetricName``."""

from typing import Literal, TypeAlias, cast

TrainingMetricName: TypeAlias = Literal[
    "hit",
    "coverage",
    "recall",
    "popularity",
    "freshness",
    "similarity",
    "mean_reciprocal_rank_at_25",
    "normalized_discounted_cumulative_gain_at_5",
    "normalized_discounted_cumulative_gain_at_10",
    "normalized_discounted_cumulative_gain_at_25",
    "precision_at_5",
    "precision_at_10",
    "precision_at_25",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainingMetricName) -> str:
    return value


def deserialize_json(data: str) -> TrainingMetricName:
    return cast(TrainingMetricName, data)
