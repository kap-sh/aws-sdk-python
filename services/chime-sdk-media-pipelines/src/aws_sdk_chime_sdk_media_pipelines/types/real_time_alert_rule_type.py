"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RealTimeAlertRuleType``."""

from typing import Literal, TypeAlias, cast

RealTimeAlertRuleType: TypeAlias = Literal[
    "KeywordMatch",
    "Sentiment",
    "IssueDetection",
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeAlertRuleType) -> str:
    return value


def deserialize_json(data: str) -> RealTimeAlertRuleType:
    return cast(RealTimeAlertRuleType, data)
