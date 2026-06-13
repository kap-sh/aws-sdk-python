"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.service

ServiceList: TypeAlias = list["aws_sdk_arc_region_switch.types.service.Service"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceList) -> list:
    import aws_sdk_arc_region_switch.types.service

    out: list = []
    for item in value:
        out.append(aws_sdk_arc_region_switch.types.service.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceList:
    import aws_sdk_arc_region_switch.types.service

    out: ServiceList = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.service.deserialize_aws_json_1_0(item)
        )
    return out
