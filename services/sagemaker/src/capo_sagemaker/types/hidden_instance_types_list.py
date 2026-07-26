"""Generated from Smithy shape ``com.amazonaws.sagemaker#HiddenInstanceTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.app_instance_type

HiddenInstanceTypesList: TypeAlias = list[
    "capo_sagemaker.types.app_instance_type.AppInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HiddenInstanceTypesList) -> list:
    import capo_sagemaker.types.app_instance_type

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.app_instance_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HiddenInstanceTypesList:
    import capo_sagemaker.types.app_instance_type

    out: HiddenInstanceTypesList = []
    for item in data:
        out.append(
            capo_sagemaker.types.app_instance_type.deserialize_aws_json_1_1(item)
        )
    return out
