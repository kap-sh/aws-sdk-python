"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteDeviceFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class DeleteDeviceFleetRequest(TypedDict, closed=True):
    device_fleet_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeviceFleetRequest) -> dict:
    out: dict = {}
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeviceFleetRequest:
    out: DeleteDeviceFleetRequest = {}  # type: ignore[typeddict-item]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    return out
