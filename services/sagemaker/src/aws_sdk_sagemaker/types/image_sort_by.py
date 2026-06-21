"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageSortBy``."""

from typing import Literal, TypeAlias, cast

ImageSortBy: TypeAlias = Literal[
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
    "IMAGE_NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageSortBy:
    return cast(ImageSortBy, data)
