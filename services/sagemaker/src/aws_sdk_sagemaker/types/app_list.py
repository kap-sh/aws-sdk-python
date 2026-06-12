"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_details

AppList: TypeAlias = list["aws_sdk_sagemaker.types.app_details.AppDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppList) -> list:
    import aws_sdk_sagemaker.types.app_details

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.app_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppList:
    import aws_sdk_sagemaker.types.app_details

    out: AppList = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.app_details.deserialize_aws_json_1_1(item))
    return out
