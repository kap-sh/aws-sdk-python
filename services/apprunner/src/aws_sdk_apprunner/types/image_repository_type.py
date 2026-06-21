"""Generated from Smithy shape ``com.amazonaws.apprunner#ImageRepositoryType``."""

from typing import Literal, TypeAlias, cast

ImageRepositoryType: TypeAlias = Literal[
    "ECR",
    "ECR_PUBLIC",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImageRepositoryType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImageRepositoryType:
    return cast(ImageRepositoryType, data)
