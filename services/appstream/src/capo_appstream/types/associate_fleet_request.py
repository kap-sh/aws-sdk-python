"""Generated from Smithy shape ``com.amazonaws.appstream#AssociateFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string


class AssociateFleetRequest(TypedDict, closed=True):
    fleet_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the fleet. </p>"""
    stack_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFleetRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFleetRequest:
    out: AssociateFleetRequest = {}  # type: ignore[typeddict-item]
    if "FleetName" in data:
        out["fleet_name"] = data["FleetName"]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    return out
