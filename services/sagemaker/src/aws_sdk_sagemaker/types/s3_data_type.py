"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3DataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

S3DataType: TypeAlias = Literal[
    "ManifestFile",
    "S3Prefix",
    "AugmentedManifestFile",
    "Converse",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ManifestFile",
        "S3Prefix",
        "AugmentedManifestFile",
        "Converse",
    )
)


def serialize_aws_json_1_1(value: S3DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3DataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3DataType value: {data!r}")
    return cast(S3DataType, data)
