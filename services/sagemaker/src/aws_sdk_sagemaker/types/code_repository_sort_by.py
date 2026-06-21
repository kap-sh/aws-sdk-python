"""Generated from Smithy shape ``com.amazonaws.sagemaker#CodeRepositorySortBy``."""

from typing import Literal, TypeAlias, cast

CodeRepositorySortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "LastModifiedTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeRepositorySortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CodeRepositorySortBy:
    return cast(CodeRepositorySortBy, data)
