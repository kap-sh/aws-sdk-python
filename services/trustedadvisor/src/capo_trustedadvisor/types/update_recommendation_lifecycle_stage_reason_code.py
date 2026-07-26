"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateRecommendationLifecycleStageReasonCode``."""

from typing import Literal, TypeAlias, cast

UpdateRecommendationLifecycleStageReasonCode: TypeAlias = Literal[
    "non_critical_account",
    "temporary_account",
    "valid_business_case",
    "other_methods_available",
    "low_priority",
    "not_applicable",
    "other",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationLifecycleStageReasonCode) -> str:
    return value


def deserialize_json(data: str) -> UpdateRecommendationLifecycleStageReasonCode:
    return cast(UpdateRecommendationLifecycleStageReasonCode, data)
