"""Generated from Smithy shape ``com.amazonaws.eks#NodeRepairConfigOverridesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.node_repair_config_overrides

NodeRepairConfigOverridesList: TypeAlias = list[
    "aws_sdk_eks.types.node_repair_config_overrides.NodeRepairConfigOverrides"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeRepairConfigOverridesList) -> list:
    import aws_sdk_eks.types.node_repair_config_overrides

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.node_repair_config_overrides.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeRepairConfigOverridesList:
    import aws_sdk_eks.types.node_repair_config_overrides

    out: NodeRepairConfigOverridesList = []
    for item in data:
        out.append(
            aws_sdk_eks.types.node_repair_config_overrides.deserialize_json(item)
        )
    return out
