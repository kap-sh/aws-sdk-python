"""Generated from Smithy shape ``com.amazonaws.ecr#ImageStatus``."""

from typing import Literal, TypeAlias, cast

ImageStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ACTIVATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageStatus:
    return cast(ImageStatus, data)
