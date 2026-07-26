"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3InputMode``."""

from typing import Literal, TypeAlias, cast

ProcessingS3InputMode: TypeAlias = Literal[
    "Pipe",
    "File",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingS3InputMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3InputMode:
    return cast(ProcessingS3InputMode, data)
