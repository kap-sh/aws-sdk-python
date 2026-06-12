"""Generated from Smithy shape ``com.amazonaws.sagemaker#CaptureMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CaptureMode: TypeAlias = Literal[
    "Input",
    "Output",
    "InputAndOutput",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Input",
        "Output",
        "InputAndOutput",
    )
)


def serialize_aws_json_1_1(value: CaptureMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CaptureMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CaptureMode value: {data!r}")
    return cast(CaptureMode, data)
