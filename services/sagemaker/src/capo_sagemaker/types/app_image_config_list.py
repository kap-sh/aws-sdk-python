"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppImageConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.app_image_config_details

AppImageConfigList: TypeAlias = list[
    "capo_sagemaker.types.app_image_config_details.AppImageConfigDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppImageConfigList) -> list:
    import capo_sagemaker.types.app_image_config_details

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.app_image_config_details.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AppImageConfigList:
    import capo_sagemaker.types.app_image_config_details

    out: AppImageConfigList = []
    for item in data:
        out.append(
            capo_sagemaker.types.app_image_config_details.deserialize_aws_json_1_1(item)
        )
    return out
