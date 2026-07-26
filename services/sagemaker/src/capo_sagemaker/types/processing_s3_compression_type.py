"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3CompressionType``."""

from typing import Literal, TypeAlias, cast

ProcessingS3CompressionType: TypeAlias = Literal[
    "None",
    "Gzip",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingS3CompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3CompressionType:
    return cast(ProcessingS3CompressionType, data)
