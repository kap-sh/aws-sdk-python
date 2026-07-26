"""Generated from Smithy shape ``com.amazonaws.ecs#HostEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.host_entry

HostEntryList: TypeAlias = list["capo_ecs.types.host_entry.HostEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostEntryList) -> list:
    import capo_ecs.types.host_entry

    out: list = []
    for item in value:
        out.append(capo_ecs.types.host_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HostEntryList:
    import capo_ecs.types.host_entry

    out: HostEntryList = []
    for item in data:
        out.append(capo_ecs.types.host_entry.deserialize_aws_json_1_1(item))
    return out
