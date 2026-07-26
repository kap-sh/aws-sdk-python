"""Generated from Smithy shape ``com.amazonaws.pcs#ComputeNodeGroupConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.compute_node_group_configuration

ComputeNodeGroupConfigurationList: TypeAlias = list[
    "capo_pcs.types.compute_node_group_configuration.ComputeNodeGroupConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeNodeGroupConfigurationList) -> list:
    import capo_pcs.types.compute_node_group_configuration

    out: list = []
    for item in value:
        out.append(
            capo_pcs.types.compute_node_group_configuration.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ComputeNodeGroupConfigurationList:
    import capo_pcs.types.compute_node_group_configuration

    out: ComputeNodeGroupConfigurationList = []
    for item in data:
        out.append(
            capo_pcs.types.compute_node_group_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out
