"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageVersionSortOrder``."""

from typing import Literal, TypeAlias, cast

ImageVersionSortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageVersionSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageVersionSortOrder:
    return cast(ImageVersionSortOrder, data)
