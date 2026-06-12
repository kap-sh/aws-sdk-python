"""Generated from Smithy shape ``com.amazonaws.datasync#S3StorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

S3StorageClass: TypeAlias = Literal[
    "STANDARD",
    "STANDARD_IA",
    "ONEZONE_IA",
    "INTELLIGENT_TIERING",
    "GLACIER",
    "DEEP_ARCHIVE",
    "OUTPOSTS",
    "GLACIER_INSTANT_RETRIEVAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "STANDARD_IA",
        "ONEZONE_IA",
        "INTELLIGENT_TIERING",
        "GLACIER",
        "DEEP_ARCHIVE",
        "OUTPOSTS",
        "GLACIER_INSTANT_RETRIEVAL",
    )
)


def serialize_aws_json_1_1(value: S3StorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3StorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3StorageClass value: {data!r}")
    return cast(S3StorageClass, data)
