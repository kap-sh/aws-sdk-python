"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class InstanceCapacity(TypedDict, closed=True):
    available_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances that can be launched onto the Dedicated Host based on the host's available capacity.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type supported by the Dedicated Host.</p>"""
    total_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The total number of instances that can be launched onto the Dedicated Host if there are no instances running on it.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceCapacity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "available_capacity" in value:
        pairs.append(
            (f"{key_prefix}AvailableCapacity", str(value["available_capacity"]))
        )
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "total_capacity" in value:
        pairs.append((f"{key_prefix}TotalCapacity", str(value["total_capacity"])))


def deserialize_ec2_query(el: Element) -> InstanceCapacity:
    out: InstanceCapacity = {}  # type: ignore[typeddict-item]
    child_available_capacity = el.find("AvailableCapacity")
    if child_available_capacity is not None:
        out["available_capacity"] = int(child_available_capacity.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_total_capacity = el.find("TotalCapacity")
    if child_total_capacity is not None:
        out["total_capacity"] = int(child_total_capacity.text or "")
    return out
