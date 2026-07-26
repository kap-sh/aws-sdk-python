"""Generated from Smithy shape ``com.amazonaws.drs#DataReplicationInfoReplicatedDisks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.data_replication_info_replicated_disk

DataReplicationInfoReplicatedDisks: TypeAlias = list[
    "capo_drs.types.data_replication_info_replicated_disk.DataReplicationInfoReplicatedDisk"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInfoReplicatedDisks) -> list:
    import capo_drs.types.data_replication_info_replicated_disk

    out: list = []
    for item in value:
        out.append(
            capo_drs.types.data_replication_info_replicated_disk.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataReplicationInfoReplicatedDisks:
    import capo_drs.types.data_replication_info_replicated_disk

    out: DataReplicationInfoReplicatedDisks = []
    for item in data:
        out.append(
            capo_drs.types.data_replication_info_replicated_disk.deserialize_json(item)
        )
    return out
