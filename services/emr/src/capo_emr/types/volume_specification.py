"""Generated from Smithy shape ``com.amazonaws.emr#VolumeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.integer
    import capo_emr.types.string
    import capo_emr.types.throughput_val


class VolumeSpecification(TypedDict, closed=True):
    volume_type: NotRequired["capo_emr.types.string.String"]
    """<p>The volume type. Volume types supported are gp3, gp2, io1, st1, sc1, and standard.</p>"""
    iops: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) that the volume supports.</p>"""
    size_in_gb: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.</p>"""
    throughput: NotRequired["capo_emr.types.throughput_val.ThroughputVal"]
    """<p>The throughput, in mebibyte per second (MiB/s). This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeSpecification) -> dict:
    out: dict = {}
    if "volume_type" in value:
        out["VolumeType"] = value["volume_type"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "size_in_gb" in value:
        out["SizeInGB"] = value["size_in_gb"]
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VolumeSpecification:
    out: VolumeSpecification = {}  # type: ignore[typeddict-item]
    if "VolumeType" in data:
        out["volume_type"] = data["VolumeType"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "SizeInGB" in data:
        out["size_in_gb"] = data["SizeInGB"]
    if "Throughput" in data:
        out["throughput"] = data["Throughput"]
    return out
