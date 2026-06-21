"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageStatus``."""

from typing import Literal, TypeAlias, cast

ImageStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageStatus:
    return cast(ImageStatus, data)
