"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceEvaluationStatus``."""

from typing import Literal, TypeAlias, cast

ResourceEvaluationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceEvaluationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceEvaluationStatus:
    return cast(ResourceEvaluationStatus, data)
