"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.delete_fleet_error
    import capo_ec2.types.fleet_id


class DeleteFleetErrorItem(TypedDict, closed=True):
    error: NotRequired["capo_ec2.types.delete_fleet_error.DeleteFleetError"]
    """<p>The error.</p>"""
    fleet_id: NotRequired["capo_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteFleetErrorItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "error" in value:
        import capo_ec2.types.delete_fleet_error

        capo_ec2.types.delete_fleet_error.serialize_ec2_query(
            value["error"], pairs, f"{key_prefix}Error"
        )
    if "fleet_id" in value:
        pairs.append((f"{key_prefix}FleetId", str(value["fleet_id"])))


def deserialize_ec2_query(el: Element) -> DeleteFleetErrorItem:
    out: DeleteFleetErrorItem = {}  # type: ignore[typeddict-item]
    child_error = el.find("error")
    if child_error is not None:
        import capo_ec2.types.delete_fleet_error

        out["error"] = capo_ec2.types.delete_fleet_error.deserialize_ec2_query(
            child_error
        )
    child_fleet_id = el.find("fleetId")
    if child_fleet_id is not None:
        out["fleet_id"] = str(child_fleet_id.text or "")
    return out
