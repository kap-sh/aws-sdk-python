"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EbsVolumeConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class EbsVolumeConfiguration(TypedDict):
    type: NotRequired["str"]
    """<p>The EBS volume type, such as gp2, gp3, io1, io2, st1, or sc1.</p>"""
    size_in_gib: NotRequired["int"]
    """<p>The size of the EBS volume in gibibytes (GiB).</p>"""
    iops: NotRequired["int"]
    """<p>The number of I/O operations per second (IOPS) provisioned for the volume.</p>"""
    throughput: NotRequired["int"]
    """<p>The throughput in MiB/s provisioned for the volume (applicable to gp3, io1, and io2bx volumes).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EbsVolumeConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "size_in_gib" in value:
        out["sizeInGib"] = value["size_in_gib"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EbsVolumeConfiguration:
    out: EbsVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "sizeInGib" in data:
        out["size_in_gib"] = data["sizeInGib"]
    if "iops" in data:
        out["iops"] = data["iops"]
    if "throughput" in data:
        out["throughput"] = data["throughput"]
    return out
