"""Generated from Smithy shape ``com.amazonaws.codepipeline#SourceRevisionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

SourceRevisionType: TypeAlias = Literal[
    "COMMIT_ID",
    "IMAGE_DIGEST",
    "S3_OBJECT_VERSION_ID",
    "S3_OBJECT_KEY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMMIT_ID",
        "IMAGE_DIGEST",
        "S3_OBJECT_VERSION_ID",
        "S3_OBJECT_KEY",
    )
)


def serialize_aws_json_1_1(value: SourceRevisionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceRevisionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceRevisionType value: {data!r}")
    return cast(SourceRevisionType, data)
