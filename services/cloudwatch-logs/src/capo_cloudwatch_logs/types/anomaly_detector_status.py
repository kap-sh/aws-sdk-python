"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AnomalyDetectorStatus``."""

from typing import Literal, TypeAlias, cast

AnomalyDetectorStatus: TypeAlias = Literal[
    "INITIALIZING",
    "TRAINING",
    "ANALYZING",
    "FAILED",
    "DELETED",
    "PAUSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyDetectorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnomalyDetectorStatus:
    return cast(AnomalyDetectorStatus, data)
