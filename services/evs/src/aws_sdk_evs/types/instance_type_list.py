"""Generated from Smithy shape ``com.amazonaws.evs#InstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.instance_type

InstanceTypeList: TypeAlias = list["aws_sdk_evs.types.instance_type.InstanceType"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceTypeList) -> list:
    import aws_sdk_evs.types.instance_type

    out: list = []
    for item in value:
        out.append(aws_sdk_evs.types.instance_type.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceTypeList:
    import aws_sdk_evs.types.instance_type

    out: InstanceTypeList = []
    for item in data:
        out.append(aws_sdk_evs.types.instance_type.deserialize_aws_json_1_0(item))
    return out
