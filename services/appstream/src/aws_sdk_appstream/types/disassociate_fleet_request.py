"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateFleetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string


class DisassociateFleetRequest(TypedDict):
    fleet_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the fleet.</p>"""
    stack_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFleetRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFleetRequest:
    out: DisassociateFleetRequest = {}  # type: ignore[typeddict-item]
    if "FleetName" in data:
        out["fleet_name"] = data["FleetName"]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    return out
