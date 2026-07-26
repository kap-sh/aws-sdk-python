"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.next_token


class DescribeDeviceRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>Next token of device description.</p>"""
    device_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The unique ID of the device.</p>"""
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet the devices belong to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeviceRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeviceRequest:
    out: DescribeDeviceRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    return out
