"""Generated from Smithy shape ``com.amazonaws.mgn#LaunchTemplateDiskConf``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.iops
    import capo_mgn.types.throughput
    import capo_mgn.types.volume_type


class LaunchTemplateDiskConf(TypedDict, closed=True):
    volume_type: NotRequired["capo_mgn.types.volume_type.VolumeType"]
    """<p>Launch template disk volume type configuration.</p>"""
    iops: NotRequired["capo_mgn.types.iops.Iops"]
    """<p>Launch template disk iops configuration.</p>"""
    throughput: NotRequired["capo_mgn.types.throughput.Throughput"]
    """<p>Launch template disk throughput configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateDiskConf) -> dict:
    out: dict = {}
    if "volume_type" in value:
        out["volumeType"] = value["volume_type"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    return out


def deserialize_json(data: dict) -> LaunchTemplateDiskConf:
    out: LaunchTemplateDiskConf = {}  # type: ignore[typeddict-item]
    if "volumeType" in data:
        out["volume_type"] = data["volumeType"]
    if "iops" in data:
        out["iops"] = data["iops"]
    if "throughput" in data:
        out["throughput"] = data["throughput"]
    return out
