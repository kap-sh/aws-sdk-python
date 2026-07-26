"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.instance_entry

InstanceEntryList: TypeAlias = list["capo_lightsail.types.instance_entry.InstanceEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceEntryList) -> list:
    import capo_lightsail.types.instance_entry

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.instance_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceEntryList:
    import capo_lightsail.types.instance_entry

    out: InstanceEntryList = []
    for item in data:
        out.append(capo_lightsail.types.instance_entry.deserialize_aws_json_1_1(item))
    return out
