"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstancePoolList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.instance_pool

InstancePoolList: TypeAlias = list["capo_sagemaker.types.instance_pool.InstancePool"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePoolList) -> list:
    import capo_sagemaker.types.instance_pool

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.instance_pool.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePoolList:
    import capo_sagemaker.types.instance_pool

    out: InstancePoolList = []
    for item in data:
        out.append(capo_sagemaker.types.instance_pool.deserialize_aws_json_1_1(item))
    return out
