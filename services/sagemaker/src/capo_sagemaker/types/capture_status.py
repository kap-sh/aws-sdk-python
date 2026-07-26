"""Generated from Smithy shape ``com.amazonaws.sagemaker#CaptureStatus``."""

from typing import Literal, TypeAlias, cast

CaptureStatus: TypeAlias = Literal[
    "Started",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaptureStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CaptureStatus:
    return cast(CaptureStatus, data)
