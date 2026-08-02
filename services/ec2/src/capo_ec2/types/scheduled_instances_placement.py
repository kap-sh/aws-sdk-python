"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesPlacement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.placement_group_name
    import capo_ec2.types.string


class ScheduledInstancesPlacement(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    group_name: NotRequired["capo_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesPlacement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesPlacement:
    out: ScheduledInstancesPlacement = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    return out
