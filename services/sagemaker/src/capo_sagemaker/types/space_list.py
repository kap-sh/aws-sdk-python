"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.space_details

SpaceList: TypeAlias = list["capo_sagemaker.types.space_details.SpaceDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceList) -> list:
    import capo_sagemaker.types.space_details

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.space_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SpaceList:
    import capo_sagemaker.types.space_details

    out: SpaceList = []
    for item in data:
        out.append(capo_sagemaker.types.space_details.deserialize_aws_json_1_1(item))
    return out
