"""Generated from Smithy shape ``com.amazonaws.glue#CloudWatchEncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CloudWatchEncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "SSE-KMS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "SSE-KMS",
    )
)


def serialize_aws_json_1_1(value: CloudWatchEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudWatchEncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloudWatchEncryptionMode value: {data!r}")
    return cast(CloudWatchEncryptionMode, data)
