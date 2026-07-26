"""Generated from Smithy shape ``com.amazonaws.drs#DataReplicationInfoReplicatedDisk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.bounded_string
    import capo_drs.types.positive_integer
    import capo_drs.types.volume_status


class DataReplicationInfoReplicatedDisk(TypedDict, closed=True):
    device_name: NotRequired["capo_drs.types.bounded_string.BoundedString"]
    """<p>The name of the device.</p>"""
    total_storage_bytes: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The total amount of data to be replicated in bytes.</p>"""
    replicated_storage_bytes: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of data replicated so far in bytes.</p>"""
    rescanned_storage_bytes: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of data to be rescanned in bytes.</p>"""
    backlogged_storage_bytes: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The size of the replication backlog in bytes.</p>"""
    volume_status: NotRequired["capo_drs.types.volume_status.VolumeStatus"]
    """<p>The status of the volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInfoReplicatedDisk) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    out["totalStorageBytes"] = value.get("total_storage_bytes", 0)
    out["replicatedStorageBytes"] = value.get("replicated_storage_bytes", 0)
    out["rescannedStorageBytes"] = value.get("rescanned_storage_bytes", 0)
    out["backloggedStorageBytes"] = value.get("backlogged_storage_bytes", 0)
    if "volume_status" in value:
        out["volumeStatus"] = value["volume_status"]
    return out


def deserialize_json(data: dict) -> DataReplicationInfoReplicatedDisk:
    out: DataReplicationInfoReplicatedDisk = {}  # type: ignore[typeddict-item]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    if "totalStorageBytes" in data:
        out["total_storage_bytes"] = data["totalStorageBytes"]
    else:
        out["total_storage_bytes"] = 0
    if "replicatedStorageBytes" in data:
        out["replicated_storage_bytes"] = data["replicatedStorageBytes"]
    else:
        out["replicated_storage_bytes"] = 0
    if "rescannedStorageBytes" in data:
        out["rescanned_storage_bytes"] = data["rescannedStorageBytes"]
    else:
        out["rescanned_storage_bytes"] = 0
    if "backloggedStorageBytes" in data:
        out["backlogged_storage_bytes"] = data["backloggedStorageBytes"]
    else:
        out["backlogged_storage_bytes"] = 0
    if "volumeStatus" in data:
        out["volume_status"] = data["volumeStatus"]
    return out
