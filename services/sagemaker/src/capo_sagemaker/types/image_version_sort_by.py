"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageVersionSortBy``."""

from typing import Literal, TypeAlias, cast

ImageVersionSortBy: TypeAlias = Literal[
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
    "VERSION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageVersionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageVersionSortBy:
    return cast(ImageVersionSortBy, data)
