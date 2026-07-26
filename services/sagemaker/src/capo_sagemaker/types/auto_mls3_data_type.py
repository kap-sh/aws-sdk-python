"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLS3DataType``."""

from typing import Literal, TypeAlias, cast

AutoMLS3DataType: TypeAlias = Literal[
    "ManifestFile",
    "S3Prefix",
    "AugmentedManifestFile",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLS3DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLS3DataType:
    return cast(AutoMLS3DataType, data)
