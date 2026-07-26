"""Generated from Smithy shape ``com.amazonaws.ecs#PortMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.port_mapping

PortMappingList: TypeAlias = list["capo_ecs.types.port_mapping.PortMapping"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortMappingList) -> list:
    import capo_ecs.types.port_mapping

    out: list = []
    for item in value:
        out.append(capo_ecs.types.port_mapping.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PortMappingList:
    import capo_ecs.types.port_mapping

    out: PortMappingList = []
    for item in data:
        out.append(capo_ecs.types.port_mapping.deserialize_aws_json_1_1(item))
    return out
