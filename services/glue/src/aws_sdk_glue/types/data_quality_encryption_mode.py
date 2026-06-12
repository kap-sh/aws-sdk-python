"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DataQualityEncryptionMode: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: DataQualityEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityEncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataQualityEncryptionMode value: {data!r}")
    return cast(DataQualityEncryptionMode, data)
