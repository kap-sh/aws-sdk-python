"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSpeculativeDecodingS3DataType``."""

from typing import Literal, TypeAlias, cast

ModelSpeculativeDecodingS3DataType: TypeAlias = Literal[
    "S3Prefix",
    "ManifestFile",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSpeculativeDecodingS3DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelSpeculativeDecodingS3DataType:
    return cast(ModelSpeculativeDecodingS3DataType, data)
