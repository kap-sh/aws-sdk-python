"""Generated from Smithy shape ``com.amazonaws.drs#DataReplicationInfoReplicatedDisks``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_drs.types.data_replication_info_replicated_disk

DataReplicationInfoReplicatedDisks: TypeAlias = list["aws_sdk_drs.types.data_replication_info_replicated_disk.DataReplicationInfoReplicatedDisk"]


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInfoReplicatedDisks) -> list:
    import aws_sdk_drs.types.data_replication_info_replicated_disk
    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.data_replication_info_replicated_disk.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataReplicationInfoReplicatedDisks:
    import aws_sdk_drs.types.data_replication_info_replicated_disk
    out: DataReplicationInfoReplicatedDisks = []
    for item in data:
        out.append(aws_sdk_drs.types.data_replication_info_replicated_disk.deserialize_json(item))
    return out