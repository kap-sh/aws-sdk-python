"""Generated from Smithy shape ``com.amazonaws.outposts#InstanceTypeItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.instance_type
    import aws_sdk_outposts.types.vcpu_count


class InstanceTypeItem(TypedDict, closed=True):
    instance_type: NotRequired["aws_sdk_outposts.types.instance_type.InstanceType"]
    vcp_us: NotRequired["aws_sdk_outposts.types.vcpu_count.VCPUCount"]
    """<p>The number of default VCPUs in an instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypeItem) -> dict:
    out: dict = {}
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "vcp_us" in value:
        out["VCPUs"] = value["vcp_us"]
    return out


def deserialize_json(data: dict) -> InstanceTypeItem:
    out: InstanceTypeItem = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "VCPUs" in data:
        out["vcp_us"] = data["VCPUs"]
    return out
