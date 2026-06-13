"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateRecommendationLifecycleStageReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "non_critical_account",
        "temporary_account",
        "valid_business_case",
        "other_methods_available",
        "low_priority",
        "not_applicable",
        "other",
    )
)


def serialize_json(value: UpdateRecommendationLifecycleStageReasonCode) -> str:
    return value


def deserialize_json(data: str) -> UpdateRecommendationLifecycleStageReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UpdateRecommendationLifecycleStageReasonCode value: {data!r}"
        )
    return cast(UpdateRecommendationLifecycleStageReasonCode, data)
