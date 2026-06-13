"""Generated from Smithy shape ``com.amazonaws.mgn#DataReplicationInfoReplicatedDisk``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.positive_integer


class DataReplicationInfoReplicatedDisk(TypedDict):
    device_name: NotRequired["aws_sdk_mgn.types.bounded_string.BoundedString"]
    """<p>Request to query device name.</p>"""
    total_storage_bytes: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Request to query total amount of data replicated in bytes.</p>"""
    replicated_storage_bytes: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Request to query amount of data replicated in bytes.</p>"""
    rescanned_storage_bytes: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Request to query amount of data rescanned in bytes.</p>"""
    backlogged_storage_bytes: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Request to query data replication backlog size in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInfoReplicatedDisk) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    out["totalStorageBytes"] = value.get("total_storage_bytes", 0)
    out["replicatedStorageBytes"] = value.get("replicated_storage_bytes", 0)
    out["rescannedStorageBytes"] = value.get("rescanned_storage_bytes", 0)
    out["backloggedStorageBytes"] = value.get("backlogged_storage_bytes", 0)
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
    return out
