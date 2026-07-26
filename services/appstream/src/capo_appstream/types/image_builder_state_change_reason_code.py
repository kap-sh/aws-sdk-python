"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

ImageBuilderStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "IMAGE_UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageBuilderStateChangeReasonCode:
    return cast(ImageBuilderStateChangeReasonCode, data)
