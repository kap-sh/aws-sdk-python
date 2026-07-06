"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.fleet_id


class CreateFleetResponse(TypedDict, closed=True):
    id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of the created fleet. </p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The ARN of the created fleet. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFleetResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFleetResponse:
    out: CreateFleetResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateFleetResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateFleetResponse.arn required")
    return out
