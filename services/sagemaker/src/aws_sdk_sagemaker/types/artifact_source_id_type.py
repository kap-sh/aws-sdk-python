"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactSourceIdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ArtifactSourceIdType: TypeAlias = Literal[
    "MD5Hash",
    "S3ETag",
    "S3Version",
    "Custom",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MD5Hash",
        "S3ETag",
        "S3Version",
        "Custom",
    )
)


def serialize_aws_json_1_1(value: ArtifactSourceIdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactSourceIdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactSourceIdType value: {data!r}")
    return cast(ArtifactSourceIdType, data)
