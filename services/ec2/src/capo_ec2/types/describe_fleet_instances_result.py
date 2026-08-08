"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.active_instance_set
    import capo_ec2.types.fleet_id
    import capo_ec2.types.string


class DescribeFleetInstancesResult(TypedDict, closed=True):
    active_instances: NotRequired[
        "capo_ec2.types.active_instance_set.ActiveInstanceSet"
    ]
    """<p>The running instances. This list is refreshed periodically and might be out of date.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    fleet_id: NotRequired["capo_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "active_instances" in value:
        import capo_ec2.types.active_instance_set

        capo_ec2.types.active_instance_set.serialize_ec2_query(
            value["active_instances"], pairs, f"{key_prefix}ActiveInstanceSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "fleet_id" in value:
        pairs.append((f"{key_prefix}FleetId", str(value["fleet_id"])))


def deserialize_ec2_query(el: Element) -> DescribeFleetInstancesResult:
    out: DescribeFleetInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("activeInstanceSet") is not None:
        import capo_ec2.types.active_instance_set

        out["active_instances"] = (
            capo_ec2.types.active_instance_set.deserialize_ec2_query(
                el, "activeInstanceSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_fleet_id = el.find("fleetId")
    if child_fleet_id is not None:
        out["fleet_id"] = str(child_fleet_id.text or "")
    return out
