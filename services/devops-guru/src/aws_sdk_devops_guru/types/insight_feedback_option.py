"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightFeedbackOption``."""

from typing import Literal, TypeAlias, cast

InsightFeedbackOption: TypeAlias = Literal[
    "VALID_COLLECTION",
    "RECOMMENDATION_USEFUL",
    "ALERT_TOO_SENSITIVE",
    "DATA_NOISY_ANOMALY",
    "DATA_INCORRECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightFeedbackOption) -> str:
    return value


def deserialize_json(data: str) -> InsightFeedbackOption:
    return cast(InsightFeedbackOption, data)
