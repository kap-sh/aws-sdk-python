"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.fleet_id


class UpdateFleetRequest(TypedDict, closed=True):
    fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of the fleet to update. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p> An updated description of the fleet. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateFleetRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateFleetRequest:
    out: UpdateFleetRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
