"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_group

InstanceGroupList: TypeAlias = list["aws_sdk_emr.types.instance_group.InstanceGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupList) -> list:
    import aws_sdk_emr.types.instance_group

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.instance_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceGroupList:
    import aws_sdk_emr.types.instance_group

    out: InstanceGroupList = []
    for item in data:
        out.append(aws_sdk_emr.types.instance_group.deserialize_aws_json_1_1(item))
    return out
