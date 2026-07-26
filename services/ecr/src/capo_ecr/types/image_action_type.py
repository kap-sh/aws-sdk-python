"""Generated from Smithy shape ``com.amazonaws.ecr#ImageActionType``."""

from typing import Literal, TypeAlias, cast

ImageActionType: TypeAlias = Literal[
    "EXPIRE",
    "TRANSITION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageActionType:
    return cast(ImageActionType, data)
