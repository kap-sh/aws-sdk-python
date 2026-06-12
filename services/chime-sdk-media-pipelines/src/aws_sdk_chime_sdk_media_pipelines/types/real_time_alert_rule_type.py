"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RealTimeAlertRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

RealTimeAlertRuleType: TypeAlias = Literal[
    "KeywordMatch",
    "Sentiment",
    "IssueDetection",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KeywordMatch",
        "Sentiment",
        "IssueDetection",
    )
)


def serialize_json(value: RealTimeAlertRuleType) -> str:
    return value


def deserialize_json(data: str) -> RealTimeAlertRuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RealTimeAlertRuleType value: {data!r}")
    return cast(RealTimeAlertRuleType, data)
