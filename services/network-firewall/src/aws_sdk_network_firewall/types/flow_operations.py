"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.flow_operation_metadata

FlowOperations: TypeAlias = list[
    "aws_sdk_network_firewall.types.flow_operation_metadata.FlowOperationMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowOperations) -> list:
    import aws_sdk_network_firewall.types.flow_operation_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.flow_operation_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FlowOperations:
    import aws_sdk_network_firewall.types.flow_operation_metadata

    out: FlowOperations = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.flow_operation_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
