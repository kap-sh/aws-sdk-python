"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageComputeType``."""

from typing import Literal, TypeAlias, cast

ImageComputeType: TypeAlias = Literal[
    "BASE",
    "GRAPHICS_G4DN",
    "GRAPHICS_G6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageComputeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageComputeType:
    return cast(ImageComputeType, data)
