"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInfoReplicatedDisks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_instance_data_replication_info_replicated_disk

RecoveryInstanceDataReplicationInfoReplicatedDisks: TypeAlias = list[
    "capo_drs.types.recovery_instance_data_replication_info_replicated_disk.RecoveryInstanceDataReplicationInfoReplicatedDisk"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInfoReplicatedDisks) -> list:
    import capo_drs.types.recovery_instance_data_replication_info_replicated_disk

    out: list = []
    for item in value:
        out.append(
            capo_drs.types.recovery_instance_data_replication_info_replicated_disk.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecoveryInstanceDataReplicationInfoReplicatedDisks:
    import capo_drs.types.recovery_instance_data_replication_info_replicated_disk

    out: RecoveryInstanceDataReplicationInfoReplicatedDisks = []
    for item in data:
        out.append(
            capo_drs.types.recovery_instance_data_replication_info_replicated_disk.deserialize_json(
                item
            )
        )
    return out
