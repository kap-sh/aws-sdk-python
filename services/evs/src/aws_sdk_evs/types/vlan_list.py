"""Generated from Smithy shape ``com.amazonaws.evs#VlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.vlan

VlanList: TypeAlias = list["aws_sdk_evs.types.vlan.Vlan"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VlanList) -> list:
    import aws_sdk_evs.types.vlan

    out: list = []
    for item in value:
        out.append(aws_sdk_evs.types.vlan.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VlanList:
    import aws_sdk_evs.types.vlan

    out: VlanList = []
    for item in data:
        out.append(aws_sdk_evs.types.vlan.deserialize_aws_json_1_0(item))
    return out
