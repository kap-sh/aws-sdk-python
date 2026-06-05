"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_fleet_error
    import aws_sdk_ec2.types.fleet_id


class DeleteFleetErrorItem(TypedDict):
    error: NotRequired["aws_sdk_ec2.types.delete_fleet_error.DeleteFleetError"]
    """<p>The error.</p>"""
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteFleetErrorItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "error" in value:
        import aws_sdk_ec2.types.delete_fleet_error

        aws_sdk_ec2.types.delete_fleet_error.serialize_ec2_query(
            value["error"], pairs, f"{prefix}.Error"
        )
    if "fleet_id" in value:
        pairs.append((f"{prefix}.FleetId", str(value["fleet_id"])))


def deserialize_ec2_query(el: Element) -> DeleteFleetErrorItem:
    out: DeleteFleetErrorItem = {}  # type: ignore[typeddict-item]
    child_error = el.find("Error")
    if child_error is not None:
        import aws_sdk_ec2.types.delete_fleet_error

        out["error"] = aws_sdk_ec2.types.delete_fleet_error.deserialize_ec2_query(
            child_error
        )
    child_fleet_id = el.find("FleetId")
    if child_fleet_id is not None:
        out["fleet_id"] = str(child_fleet_id.text or "")
    return out
