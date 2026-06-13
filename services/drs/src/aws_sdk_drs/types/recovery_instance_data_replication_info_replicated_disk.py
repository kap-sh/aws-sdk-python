"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInfoReplicatedDisk``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.bounded_string
    import aws_sdk_drs.types.positive_integer


class RecoveryInstanceDataReplicationInfoReplicatedDisk(TypedDict):
    device_name: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>The name of the device.</p>"""
    total_storage_bytes: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>The total amount of data to be replicated in bytes.</p>"""
    replicated_storage_bytes: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of data replicated so far in bytes.</p>"""
    rescanned_storage_bytes: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of data to be rescanned in bytes.</p>"""
    backlogged_storage_bytes: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>The size of the replication backlog in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInfoReplicatedDisk) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    out["totalStorageBytes"] = value.get("total_storage_bytes", 0)
    out["replicatedStorageBytes"] = value.get("replicated_storage_bytes", 0)
    out["rescannedStorageBytes"] = value.get("rescanned_storage_bytes", 0)
    out["backloggedStorageBytes"] = value.get("backlogged_storage_bytes", 0)
    return out


def deserialize_json(data: dict) -> RecoveryInstanceDataReplicationInfoReplicatedDisk:
    out: RecoveryInstanceDataReplicationInfoReplicatedDisk = {}  # type: ignore[typeddict-item]
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
    return out
