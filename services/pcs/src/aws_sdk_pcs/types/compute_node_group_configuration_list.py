"""Generated from Smithy shape ``com.amazonaws.pcs#ComputeNodeGroupConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pcs.types.compute_node_group_configuration

ComputeNodeGroupConfigurationList: TypeAlias = list[
    "aws_sdk_pcs.types.compute_node_group_configuration.ComputeNodeGroupConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeNodeGroupConfigurationList) -> list:
    import aws_sdk_pcs.types.compute_node_group_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pcs.types.compute_node_group_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ComputeNodeGroupConfigurationList:
    import aws_sdk_pcs.types.compute_node_group_configuration

    out: ComputeNodeGroupConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_pcs.types.compute_node_group_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out
