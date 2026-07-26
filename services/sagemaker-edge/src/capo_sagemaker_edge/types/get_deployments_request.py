"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#GetDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.device_fleet_name
    import capo_sagemaker_edge.types.device_name


class GetDeploymentsRequest(TypedDict, closed=True):
    device_name: NotRequired["capo_sagemaker_edge.types.device_name.DeviceName"]
    """<p>The unique name of the device you want to get the configuration of active deployments from.</p>"""
    device_fleet_name: NotRequired[
        "capo_sagemaker_edge.types.device_fleet_name.DeviceFleetName"
    ]
    """<p>The name of the fleet that the device belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentsRequest) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    return out


def deserialize_json(data: dict) -> GetDeploymentsRequest:
    out: GetDeploymentsRequest = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    return out
