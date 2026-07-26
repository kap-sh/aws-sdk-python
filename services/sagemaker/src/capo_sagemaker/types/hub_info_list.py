"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_info

HubInfoList: TypeAlias = list["capo_sagemaker.types.hub_info.HubInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubInfoList) -> list:
    import capo_sagemaker.types.hub_info

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.hub_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HubInfoList:
    import capo_sagemaker.types.hub_info

    out: HubInfoList = []
    for item in data:
        out.append(capo_sagemaker.types.hub_info.deserialize_aws_json_1_1(item))
    return out
