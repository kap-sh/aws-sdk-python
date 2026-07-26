"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3ModelDataType``."""

from typing import Literal, TypeAlias, cast

S3ModelDataType: TypeAlias = Literal[
    "S3Prefix",
    "S3Object",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ModelDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3ModelDataType:
    return cast(S3ModelDataType, data)
