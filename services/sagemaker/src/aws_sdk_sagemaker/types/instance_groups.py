"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.instance_group

InstanceGroups: TypeAlias = list["aws_sdk_sagemaker.types.instance_group.InstanceGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroups) -> list:
    import aws_sdk_sagemaker.types.instance_group

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.instance_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceGroups:
    import aws_sdk_sagemaker.types.instance_group

    out: InstanceGroups = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.instance_group.deserialize_aws_json_1_1(item)
        )
    return out
