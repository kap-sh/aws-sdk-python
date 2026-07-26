"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageVersionStatus``."""

from typing import Literal, TypeAlias, cast

ImageVersionStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "CREATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageVersionStatus:
    return cast(ImageVersionStatus, data)
