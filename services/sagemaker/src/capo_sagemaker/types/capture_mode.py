"""Generated from Smithy shape ``com.amazonaws.sagemaker#CaptureMode``."""

from typing import Literal, TypeAlias, cast

CaptureMode: TypeAlias = Literal[
    "Input",
    "Output",
    "InputAndOutput",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaptureMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CaptureMode:
    return cast(CaptureMode, data)
