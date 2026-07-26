"""Generated from Smithy shape ``com.amazonaws.sagemaker#Framework``."""

from typing import Literal, TypeAlias, cast

Framework: TypeAlias = Literal[
    "TENSORFLOW",
    "KERAS",
    "MXNET",
    "ONNX",
    "PYTORCH",
    "XGBOOST",
    "TFLITE",
    "DARKNET",
    "SKLEARN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Framework) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Framework:
    return cast(Framework, data)
