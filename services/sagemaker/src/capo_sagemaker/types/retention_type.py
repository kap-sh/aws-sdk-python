"""Generated from Smithy shape ``com.amazonaws.sagemaker#RetentionType``."""

from typing import Literal, TypeAlias, cast

RetentionType: TypeAlias = Literal[
    "Retain",
    "Delete",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetentionType:
    return cast(RetentionType, data)
