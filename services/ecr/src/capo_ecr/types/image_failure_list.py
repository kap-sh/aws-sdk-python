"""Generated from Smithy shape ``com.amazonaws.ecr#ImageFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.image_failure

ImageFailureList: TypeAlias = list["capo_ecr.types.image_failure.ImageFailure"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageFailureList) -> list:
    import capo_ecr.types.image_failure

    out: list = []
    for item in value:
        out.append(capo_ecr.types.image_failure.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageFailureList:
    import capo_ecr.types.image_failure

    out: ImageFailureList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecr.types.image_failure.deserialize_aws_json_1_1(item))
    return out
