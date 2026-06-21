"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalyFeedbackType``."""

from typing import Literal, TypeAlias, cast

AnomalyFeedbackType: TypeAlias = Literal[
    "YES",
    "NO",
    "PLANNED_ACTIVITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyFeedbackType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnomalyFeedbackType:
    return cast(AnomalyFeedbackType, data)
