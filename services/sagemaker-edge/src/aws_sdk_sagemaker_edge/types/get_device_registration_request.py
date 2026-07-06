"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#GetDeviceRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_edge.types.device_fleet_name
    import aws_sdk_sagemaker_edge.types.device_name


class GetDeviceRegistrationRequest(TypedDict, closed=True):
    device_name: NotRequired["aws_sdk_sagemaker_edge.types.device_name.DeviceName"]
    """<p>The unique name of the device you want to get the registration status from.</p>"""
    device_fleet_name: NotRequired[
        "aws_sdk_sagemaker_edge.types.device_fleet_name.DeviceFleetName"
    ]
    """<p>The name of the fleet that the device belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceRegistrationRequest) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    return out


def deserialize_json(data: dict) -> GetDeviceRegistrationRequest:
    out: GetDeviceRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    return out
