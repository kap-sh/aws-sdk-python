"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3DataType``."""

from typing import Literal, TypeAlias, cast

ProcessingS3DataType: TypeAlias = Literal[
    "ManifestFile",
    "S3Prefix",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingS3DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3DataType:
    return cast(ProcessingS3DataType, data)
