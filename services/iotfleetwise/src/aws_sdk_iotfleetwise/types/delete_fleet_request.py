"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DeleteFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.fleet_id


class DeleteFleetRequest(TypedDict, closed=True):
    fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of the fleet to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFleetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFleetRequest:
    out: DeleteFleetRequest = {}  # type: ignore[typeddict-item]
    return out
