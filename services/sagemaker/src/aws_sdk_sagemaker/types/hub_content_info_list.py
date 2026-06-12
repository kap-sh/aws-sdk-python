"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_content_info

HubContentInfoList: TypeAlias = list[
    "aws_sdk_sagemaker.types.hub_content_info.HubContentInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentInfoList) -> list:
    import aws_sdk_sagemaker.types.hub_content_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.hub_content_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HubContentInfoList:
    import aws_sdk_sagemaker.types.hub_content_info

    out: HubContentInfoList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.hub_content_info.deserialize_aws_json_1_1(item)
        )
    return out
