"""Generated from Smithy shape ``com.amazonaws.ecr#ImageSigningStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.image_signing_status

ImageSigningStatusList: TypeAlias = list[
    "capo_ecr.types.image_signing_status.ImageSigningStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageSigningStatusList) -> list:
    import capo_ecr.types.image_signing_status

    out: list = []
    for item in value:
        out.append(capo_ecr.types.image_signing_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageSigningStatusList:
    import capo_ecr.types.image_signing_status

    out: ImageSigningStatusList = []
    for item in data:
        out.append(capo_ecr.types.image_signing_status.deserialize_aws_json_1_1(item))
    return out
