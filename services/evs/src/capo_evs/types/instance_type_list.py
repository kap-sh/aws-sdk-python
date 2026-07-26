"""Generated from Smithy shape ``com.amazonaws.evs#InstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.instance_type

InstanceTypeList: TypeAlias = list["capo_evs.types.instance_type.InstanceType"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceTypeList) -> list:
    import capo_evs.types.instance_type

    out: list = []
    for item in value:
        out.append(capo_evs.types.instance_type.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceTypeList:
    import capo_evs.types.instance_type

    out: InstanceTypeList = []
    for item in data:
        out.append(capo_evs.types.instance_type.deserialize_aws_json_1_0(item))
    return out
