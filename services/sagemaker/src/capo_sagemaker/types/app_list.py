"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.app_details

AppList: TypeAlias = list["capo_sagemaker.types.app_details.AppDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppList) -> list:
    import capo_sagemaker.types.app_details

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.app_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppList:
    import capo_sagemaker.types.app_details

    out: AppList = []
    for item in data:
        out.append(capo_sagemaker.types.app_details.deserialize_aws_json_1_1(item))
    return out
