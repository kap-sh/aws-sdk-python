"""Generated from Smithy shape ``com.amazonaws.sagemaker#CaptureStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CaptureStatus: TypeAlias = Literal[
    "Started",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Started",
        "Stopped",
    )
)


def serialize_aws_json_1_1(value: CaptureStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CaptureStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CaptureStatus value: {data!r}")
    return cast(CaptureStatus, data)
