"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringProblemType``."""

from typing import Literal, TypeAlias, cast

MonitoringProblemType: TypeAlias = Literal[
    "BinaryClassification",
    "MulticlassClassification",
    "Regression",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringProblemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringProblemType:
    return cast(MonitoringProblemType, data)
