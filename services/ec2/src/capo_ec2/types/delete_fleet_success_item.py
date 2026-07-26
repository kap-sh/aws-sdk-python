"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetSuccessItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_id
    import capo_ec2.types.fleet_state_code


class DeleteFleetSuccessItem(TypedDict, closed=True):
    current_fleet_state: NotRequired["capo_ec2.types.fleet_state_code.FleetStateCode"]
    """<p>The current state of the EC2 Fleet.</p>"""
    previous_fleet_state: NotRequired["capo_ec2.types.fleet_state_code.FleetStateCode"]
    """<p>The previous state of the EC2 Fleet.</p>"""
    fleet_id: NotRequired["capo_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteFleetSuccessItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "current_fleet_state" in value:
        import capo_ec2.types.fleet_state_code

        capo_ec2.types.fleet_state_code.serialize_ec2_query(
            value["current_fleet_state"], pairs, f"{prefix}.CurrentFleetState"
        )
    if "previous_fleet_state" in value:
        import capo_ec2.types.fleet_state_code

        capo_ec2.types.fleet_state_code.serialize_ec2_query(
            value["previous_fleet_state"], pairs, f"{prefix}.PreviousFleetState"
        )
    if "fleet_id" in value:
        pairs.append((f"{prefix}.FleetId", str(value["fleet_id"])))


def deserialize_ec2_query(el: Element) -> DeleteFleetSuccessItem:
    out: DeleteFleetSuccessItem = {}  # type: ignore[typeddict-item]
    child_current_fleet_state = el.find("CurrentFleetState")
    if child_current_fleet_state is not None:
        import capo_ec2.types.fleet_state_code

        out["current_fleet_state"] = (
            capo_ec2.types.fleet_state_code.deserialize_ec2_query(
                child_current_fleet_state
            )
        )
    child_previous_fleet_state = el.find("PreviousFleetState")
    if child_previous_fleet_state is not None:
        import capo_ec2.types.fleet_state_code

        out["previous_fleet_state"] = (
            capo_ec2.types.fleet_state_code.deserialize_ec2_query(
                child_previous_fleet_state
            )
        )
    child_fleet_id = el.find("FleetId")
    if child_fleet_id is not None:
        out["fleet_id"] = str(child_fleet_id.text or "")
    return out
