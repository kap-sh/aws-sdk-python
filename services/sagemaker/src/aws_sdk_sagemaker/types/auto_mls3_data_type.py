"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLS3DataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLS3DataType: TypeAlias = Literal[
    "ManifestFile",
    "S3Prefix",
    "AugmentedManifestFile",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ManifestFile",
        "S3Prefix",
        "AugmentedManifestFile",
    )
)


def serialize_aws_json_1_1(value: AutoMLS3DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLS3DataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLS3DataType value: {data!r}")
    return cast(AutoMLS3DataType, data)
