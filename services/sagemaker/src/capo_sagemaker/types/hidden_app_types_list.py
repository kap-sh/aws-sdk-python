"""Generated from Smithy shape ``com.amazonaws.sagemaker#HiddenAppTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.app_type

HiddenAppTypesList: TypeAlias = list["capo_sagemaker.types.app_type.AppType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HiddenAppTypesList) -> list:
    import capo_sagemaker.types.app_type

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.app_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HiddenAppTypesList:
    import capo_sagemaker.types.app_type

    out: HiddenAppTypesList = []
    for item in data:
        out.append(capo_sagemaker.types.app_type.deserialize_aws_json_1_1(item))
    return out
