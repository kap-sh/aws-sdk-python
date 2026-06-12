"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterClusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.matter_cluster

MatterClusters: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.matter_cluster.MatterCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterClusters) -> list:
    import aws_sdk_iot_managed_integrations.types.matter_cluster

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.matter_cluster.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MatterClusters:
    import aws_sdk_iot_managed_integrations.types.matter_cluster

    out: MatterClusters = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.matter_cluster.deserialize_json(item)
        )
    return out
