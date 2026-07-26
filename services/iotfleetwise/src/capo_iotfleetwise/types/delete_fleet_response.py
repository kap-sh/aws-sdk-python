"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DeleteFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.fleet_id


class DeleteFleetResponse(TypedDict, closed=True):
    id: NotRequired["capo_iotfleetwise.types.fleet_id.fleetId"]
    """<p>The ID of the deleted fleet.</p>"""
    arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the deleted fleet.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFleetResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFleetResponse:
    out: DeleteFleetResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
