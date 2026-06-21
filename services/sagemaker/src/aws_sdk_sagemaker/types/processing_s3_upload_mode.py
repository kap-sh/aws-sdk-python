"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3UploadMode``."""

from typing import Literal, TypeAlias, cast

ProcessingS3UploadMode: TypeAlias = Literal[
    "Continuous",
    "EndOfJob",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingS3UploadMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3UploadMode:
    return cast(ProcessingS3UploadMode, data)
