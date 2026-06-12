"""Generated from Smithy shape ``com.amazonaws.devicefarm#UploadStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

UploadStatus: TypeAlias = Literal[
    "INITIALIZED",
    "PROCESSING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZED",
        "PROCESSING",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: UploadStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UploadStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UploadStatus value: {data!r}")
    return cast(UploadStatus, data)
