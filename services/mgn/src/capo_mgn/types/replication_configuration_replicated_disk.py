"""Generated from Smithy shape ``com.amazonaws.mgn#ReplicationConfigurationReplicatedDisk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.bounded_string
    import capo_mgn.types.positive_integer
    import capo_mgn.types.replication_configuration_replicated_disk_staging_disk_type


class ReplicationConfigurationReplicatedDisk(TypedDict, closed=True):
    device_name: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Replication Configuration replicated disk device name.</p>"""
    is_boot_disk: NotRequired["bool"]
    """<p>Replication Configuration replicated disk boot disk.</p>"""
    staging_disk_type: NotRequired[
        "capo_mgn.types.replication_configuration_replicated_disk_staging_disk_type.ReplicationConfigurationReplicatedDiskStagingDiskType"
    ]
    """<p>Replication Configuration replicated disk staging disk type.</p>"""
    iops: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Replication Configuration replicated disk IOPs.</p>"""
    throughput: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Replication Configuration replicated disk throughput.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationReplicatedDisk) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    if "is_boot_disk" in value:
        out["isBootDisk"] = value["is_boot_disk"]
    if "staging_disk_type" in value:
        out["stagingDiskType"] = value["staging_disk_type"]
    out["iops"] = value.get("iops", 0)
    out["throughput"] = value.get("throughput", 0)
    return out


def deserialize_json(data: dict) -> ReplicationConfigurationReplicatedDisk:
    out: ReplicationConfigurationReplicatedDisk = {}  # type: ignore[typeddict-item]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    if "isBootDisk" in data:
        out["is_boot_disk"] = data["isBootDisk"]
    if "stagingDiskType" in data:
        out["staging_disk_type"] = data["stagingDiskType"]
    if "iops" in data:
        out["iops"] = data["iops"]
    else:
        out["iops"] = 0
    if "throughput" in data:
        out["throughput"] = data["throughput"]
    else:
        out["throughput"] = 0
    return out
