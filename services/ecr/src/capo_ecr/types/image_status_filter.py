"""Generated from Smithy shape ``com.amazonaws.ecr#ImageStatusFilter``."""

from typing import Literal, TypeAlias, cast

ImageStatusFilter: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ACTIVATING",
    "ANY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageStatusFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageStatusFilter:
    return cast(ImageStatusFilter, data)
