"""Generated from Smithy shape ``com.amazonaws.sagemaker#RuleEvaluationStatus``."""

from typing import Literal, TypeAlias, cast

RuleEvaluationStatus: TypeAlias = Literal[
    "InProgress",
    "NoIssuesFound",
    "IssuesFound",
    "Error",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleEvaluationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleEvaluationStatus:
    return cast(RuleEvaluationStatus, data)
