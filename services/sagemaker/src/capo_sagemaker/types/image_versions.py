"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.image_version

ImageVersions: TypeAlias = list["capo_sagemaker.types.image_version.ImageVersion"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageVersions) -> list:
    import capo_sagemaker.types.image_version

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.image_version.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageVersions:
    import capo_sagemaker.types.image_version

    out: ImageVersions = []
    for item in data:
        out.append(capo_sagemaker.types.image_version.deserialize_aws_json_1_1(item))
    return out
