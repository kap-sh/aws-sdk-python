"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetVehicleStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.next_token
    import aws_sdk_iotfleetwise.types.vehicle_status_list


class GetVehicleStatusResponse(TypedDict, closed=True):
    campaigns: NotRequired[
        "aws_sdk_iotfleetwise.types.vehicle_status_list.VehicleStatusList"
    ]
    """<p> Lists information about the state of the vehicle with deployed campaigns. </p>"""
    next_token: NotRequired["aws_sdk_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVehicleStatusResponse) -> dict:
    out: dict = {}
    if "campaigns" in value:
        import aws_sdk_iotfleetwise.types.vehicle_status_list

        out["campaigns"] = (
            aws_sdk_iotfleetwise.types.vehicle_status_list.serialize_aws_json_1_0(
                value["campaigns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVehicleStatusResponse:
    out: GetVehicleStatusResponse = {}  # type: ignore[typeddict-item]
    if "campaigns" in data:
        import aws_sdk_iotfleetwise.types.vehicle_status_list

        out["campaigns"] = (
            aws_sdk_iotfleetwise.types.vehicle_status_list.deserialize_aws_json_1_0(
                data["campaigns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
