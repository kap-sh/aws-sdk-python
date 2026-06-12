"""Generated from Smithy shape ``com.amazonaws.sagemaker#Framework``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "TENSORFLOW",
        "KERAS",
        "MXNET",
        "ONNX",
        "PYTORCH",
        "XGBOOST",
        "TFLITE",
        "DARKNET",
        "SKLEARN",
    )
)


def serialize_aws_json_1_1(value: Framework) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Framework:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Framework value: {data!r}")
    return cast(Framework, data)
