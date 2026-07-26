"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroupNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.instance_group_name

InstanceGroupNames: TypeAlias = list[
    "capo_sagemaker.types.instance_group_name.InstanceGroupName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceGroupNames:
    return list(data)
