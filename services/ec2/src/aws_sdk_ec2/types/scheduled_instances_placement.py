"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesPlacement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.string


class ScheduledInstancesPlacement(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesPlacement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesPlacement:
    out: ScheduledInstancesPlacement = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    return out
