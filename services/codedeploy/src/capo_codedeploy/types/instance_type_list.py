"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_type

InstanceTypeList: TypeAlias = list["capo_codedeploy.types.instance_type.InstanceType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceTypeList) -> list:
    import capo_codedeploy.types.instance_type

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.instance_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceTypeList:
    import capo_codedeploy.types.instance_type

    out: InstanceTypeList = []
    for item in data:
        out.append(capo_codedeploy.types.instance_type.deserialize_aws_json_1_1(item))
    return out
