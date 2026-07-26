"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3DataType``."""

from typing import Literal, TypeAlias, cast

S3DataType: TypeAlias = Literal[
    "ManifestFile",
    "S3Prefix",
    "AugmentedManifestFile",
    "Converse",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3DataType:
    return cast(S3DataType, data)
