"""Generated from Smithy shape ``com.amazonaws.deadline#Ec2EbsVolume``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.ebs_iops
    import aws_sdk_deadline.types.ebs_throughput_mi_b
    import aws_sdk_deadline.types.integer


class Ec2EbsVolume(TypedDict):
    size_gi_b: "aws_sdk_deadline.types.integer.Integer"
    """<p>The EBS volume size in GiB.</p>"""
    iops: "aws_sdk_deadline.types.ebs_iops.EbsIops"
    """<p>The IOPS per volume.</p>"""
    throughput_mi_b: "aws_sdk_deadline.types.ebs_throughput_mi_b.EbsThroughputMiB"
    """<p>The throughput per volume in MiB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2EbsVolume) -> dict:
    out: dict = {}
    out["sizeGiB"] = value.get("size_gi_b", 250)
    out["iops"] = value.get("iops", 3000)
    out["throughputMiB"] = value.get("throughput_mi_b", 125)
    return out


def deserialize_json(data: dict) -> Ec2EbsVolume:
    out: Ec2EbsVolume = {}  # type: ignore[typeddict-item]
    if "sizeGiB" in data:
        out["size_gi_b"] = data["sizeGiB"]
    else:
        out["size_gi_b"] = 250
    if "iops" in data:
        out["iops"] = data["iops"]
    else:
        out["iops"] = 3000
    if "throughputMiB" in data:
        out["throughput_mi_b"] = data["throughputMiB"]
    else:
        out["throughput_mi_b"] = 125
    return out
