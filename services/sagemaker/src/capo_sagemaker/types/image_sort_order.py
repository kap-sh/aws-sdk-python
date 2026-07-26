"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageSortOrder``."""

from typing import Literal, TypeAlias, cast

ImageSortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageSortOrder:
    return cast(ImageSortOrder, data)
