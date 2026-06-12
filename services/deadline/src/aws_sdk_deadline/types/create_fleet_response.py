"""Generated from Smithy shape ``com.amazonaws.deadline#CreateFleetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fleet_id


class CreateFleetResponse(TypedDict):
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFleetResponse) -> dict:
    out: dict = {}
    out["fleetId"] = value["fleet_id"]
    return out


def deserialize_json(data: dict) -> CreateFleetResponse:
    out: CreateFleetResponse = {}  # type: ignore[typeddict-item]
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("CreateFleetResponse.fleet_id required")
    return out
