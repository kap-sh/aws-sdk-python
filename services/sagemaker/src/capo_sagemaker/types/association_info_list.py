"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssociationInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.association_info

AssociationInfoList: TypeAlias = list[
    "capo_sagemaker.types.association_info.AssociationInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationInfoList) -> list:
    import capo_sagemaker.types.association_info

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.association_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationInfoList:
    import capo_sagemaker.types.association_info

    out: AssociationInfoList = []
    for item in data:
        out.append(capo_sagemaker.types.association_info.deserialize_aws_json_1_1(item))
    return out
