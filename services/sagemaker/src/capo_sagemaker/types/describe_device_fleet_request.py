"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeDeviceFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name


class DescribeDeviceFleetRequest(TypedDict, closed=True):
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeviceFleetRequest) -> dict:
    out: dict = {}
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeviceFleetRequest:
    out: DescribeDeviceFleetRequest = {}  # type: ignore[typeddict-item]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    return out
