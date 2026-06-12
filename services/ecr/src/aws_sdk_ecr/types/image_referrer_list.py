"""Generated from Smithy shape ``com.amazonaws.ecr#ImageReferrerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_referrer

ImageReferrerList: TypeAlias = list["aws_sdk_ecr.types.image_referrer.ImageReferrer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageReferrerList) -> list:
    import aws_sdk_ecr.types.image_referrer

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.image_referrer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageReferrerList:
    import aws_sdk_ecr.types.image_referrer

    out: ImageReferrerList = []
    for item in data:
        out.append(aws_sdk_ecr.types.image_referrer.deserialize_aws_json_1_1(item))
    return out
