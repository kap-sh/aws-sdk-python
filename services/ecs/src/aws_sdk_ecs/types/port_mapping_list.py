"""Generated from Smithy shape ``com.amazonaws.ecs#PortMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.port_mapping

PortMappingList: TypeAlias = list["aws_sdk_ecs.types.port_mapping.PortMapping"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortMappingList) -> list:
    import aws_sdk_ecs.types.port_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.port_mapping.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PortMappingList:
    import aws_sdk_ecs.types.port_mapping

    out: PortMappingList = []
    for item in data:
        out.append(aws_sdk_ecs.types.port_mapping.deserialize_aws_json_1_1(item))
    return out
