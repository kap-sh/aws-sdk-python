"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.flow_operation_metadata

FlowOperations: TypeAlias = list[
    "capo_network_firewall.types.flow_operation_metadata.FlowOperationMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowOperations) -> list:
    import capo_network_firewall.types.flow_operation_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.flow_operation_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FlowOperations:
    import capo_network_firewall.types.flow_operation_metadata

    out: FlowOperations = []
    for item in data:
        out.append(
            capo_network_firewall.types.flow_operation_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
