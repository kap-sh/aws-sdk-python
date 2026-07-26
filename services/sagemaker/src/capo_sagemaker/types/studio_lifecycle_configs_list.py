"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioLifecycleConfigsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.studio_lifecycle_config_details

StudioLifecycleConfigsList: TypeAlias = list[
    "capo_sagemaker.types.studio_lifecycle_config_details.StudioLifecycleConfigDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StudioLifecycleConfigsList) -> list:
    import capo_sagemaker.types.studio_lifecycle_config_details

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.studio_lifecycle_config_details.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StudioLifecycleConfigsList:
    import capo_sagemaker.types.studio_lifecycle_config_details

    out: StudioLifecycleConfigsList = []
    for item in data:
        out.append(
            capo_sagemaker.types.studio_lifecycle_config_details.deserialize_aws_json_1_1(
                item
            )
        )
    return out
