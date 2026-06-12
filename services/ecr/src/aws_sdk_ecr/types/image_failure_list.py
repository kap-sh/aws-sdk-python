"""Generated from Smithy shape ``com.amazonaws.ecr#ImageFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_failure

ImageFailureList: TypeAlias = list["aws_sdk_ecr.types.image_failure.ImageFailure"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageFailureList) -> list:
    import aws_sdk_ecr.types.image_failure

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.image_failure.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageFailureList:
    import aws_sdk_ecr.types.image_failure

    out: ImageFailureList = []
    for item in data:
        out.append(aws_sdk_ecr.types.image_failure.deserialize_aws_json_1_1(item))
    return out
