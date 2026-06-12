"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteFleetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id


class DeleteFleetRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to remove from the fleet.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the fleet to delete.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFleetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFleetRequest:
    out: DeleteFleetRequest = {}  # type: ignore[typeddict-item]
    return out
