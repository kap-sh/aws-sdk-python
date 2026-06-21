"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringType``."""

from typing import Literal, TypeAlias, cast

MonitoringType: TypeAlias = Literal[
    "DataQuality",
    "ModelQuality",
    "ModelBias",
    "ModelExplainability",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringType:
    return cast(MonitoringType, data)
