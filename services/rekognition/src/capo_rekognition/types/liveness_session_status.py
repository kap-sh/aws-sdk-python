"""Generated from Smithy shape ``com.amazonaws.rekognition#LivenessSessionStatus``."""

from typing import Literal, TypeAlias, cast

LivenessSessionStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LivenessSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LivenessSessionStatus:
    return cast(LivenessSessionStatus, data)
