"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UploadStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

UploadStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
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
