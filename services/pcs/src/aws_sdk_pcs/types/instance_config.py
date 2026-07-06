"""Generated from Smithy shape ``com.amazonaws.pcs#InstanceConfig``."""

from typing_extensions import NotRequired, TypedDict


class InstanceConfig(TypedDict, closed=True):
    instance_type: NotRequired["str"]
    """<p>The EC2 instance type that PCS can provision in the compute node group.</p> <p> Example: <code>t2.xlarge</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceConfig) -> dict:
    out: dict = {}
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceConfig:
    out: InstanceConfig = {}  # type: ignore[typeddict-item]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    return out
