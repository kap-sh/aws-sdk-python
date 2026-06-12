"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.campaign_name
    import aws_sdk_iotfleetwise.types.vehicle_name
    import aws_sdk_iotfleetwise.types.vehicle_state


class VehicleStatus(TypedDict):
    campaign_name: NotRequired["aws_sdk_iotfleetwise.types.campaign_name.campaignName"]
    """<p>The name of a campaign.</p>"""
    vehicle_name: NotRequired["aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"]
    """<p>The unique ID of the vehicle.</p>"""
    status: NotRequired["aws_sdk_iotfleetwise.types.vehicle_state.VehicleState"]
    """<p>The status of a campaign, which can be one of the following:</p> <ul> <li> <p> <code>CREATED</code> - The campaign exists but is not yet approved.</p> </li> <li> <p> <code>READY</code> - The campaign is approved but has not been deployed to the vehicle. Data has not arrived at the vehicle yet.</p> </li> <li> <p> <code>HEALTHY</code> - The campaign is deployed to the vehicle.</p> </li> <li> <p> <code>SUSPENDED</code> - The campaign is suspended and data collection is paused.</p> </li> <li> <p> <code>DELETING</code> - The campaign is being removed from the vehicle.</p> </li> <li> <p> <code>READY_FOR_CHECKIN</code> - The campaign is approved and waiting for vehicle check-in before deployment.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VehicleStatus) -> dict:
    out: dict = {}
    if "campaign_name" in value:
        out["campaignName"] = value["campaign_name"]
    if "vehicle_name" in value:
        out["vehicleName"] = value["vehicle_name"]
    if "status" in value:
        import aws_sdk_iotfleetwise.types.vehicle_state

        out["status"] = aws_sdk_iotfleetwise.types.vehicle_state.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VehicleStatus:
    out: VehicleStatus = {}  # type: ignore[typeddict-item]
    if "campaignName" in data:
        out["campaign_name"] = data["campaignName"]
    if "vehicleName" in data:
        out["vehicle_name"] = data["vehicleName"]
    if "status" in data:
        import aws_sdk_iotfleetwise.types.vehicle_state

        out["status"] = (
            aws_sdk_iotfleetwise.types.vehicle_state.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
