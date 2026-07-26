"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteFleetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn


class DeleteFleetInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to be deleted. You can use either the fleet ID or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetInput:
    out: DeleteFleetInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    return out
