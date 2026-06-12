"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.flow_filter

FlowFilters: TypeAlias = list["aws_sdk_network_firewall.types.flow_filter.FlowFilter"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowFilters) -> list:
    import aws_sdk_network_firewall.types.flow_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.flow_filter.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FlowFilters:
    import aws_sdk_network_firewall.types.flow_filter

    out: FlowFilters = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.flow_filter.deserialize_aws_json_1_0(item)
        )
    return out
