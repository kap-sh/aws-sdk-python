"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightFeedbackOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

InsightFeedbackOption: TypeAlias = Literal[
    "VALID_COLLECTION",
    "RECOMMENDATION_USEFUL",
    "ALERT_TOO_SENSITIVE",
    "DATA_NOISY_ANOMALY",
    "DATA_INCORRECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALID_COLLECTION",
        "RECOMMENDATION_USEFUL",
        "ALERT_TOO_SENSITIVE",
        "DATA_NOISY_ANOMALY",
        "DATA_INCORRECT",
    )
)


def serialize_json(value: InsightFeedbackOption) -> str:
    return value


def deserialize_json(data: str) -> InsightFeedbackOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightFeedbackOption value: {data!r}")
    return cast(InsightFeedbackOption, data)
