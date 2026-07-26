"""Generated from Smithy shape ``com.amazonaws.mgn#ReplicationConfigurationReplicatedDisks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.replication_configuration_replicated_disk

ReplicationConfigurationReplicatedDisks: TypeAlias = list[
    "capo_mgn.types.replication_configuration_replicated_disk.ReplicationConfigurationReplicatedDisk"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationReplicatedDisks) -> list:
    import capo_mgn.types.replication_configuration_replicated_disk

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.replication_configuration_replicated_disk.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReplicationConfigurationReplicatedDisks:
    import capo_mgn.types.replication_configuration_replicated_disk

    out: ReplicationConfigurationReplicatedDisks = []
    for item in data:
        out.append(
            capo_mgn.types.replication_configuration_replicated_disk.deserialize_json(
                item
            )
        )
    return out
