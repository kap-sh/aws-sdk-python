"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateDevicesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.devices
    import aws_sdk_sagemaker.types.entity_name


class UpdateDevicesRequest(TypedDict):
    device_fleet_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet the devices belong to.</p>"""
    devices: NotRequired["aws_sdk_sagemaker.types.devices.Devices"]
    """<p>List of devices to register with Edge Manager agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDevicesRequest) -> dict:
    out: dict = {}
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "devices" in value:
        import aws_sdk_sagemaker.types.devices

        out["Devices"] = aws_sdk_sagemaker.types.devices.serialize_aws_json_1_1(
            value["devices"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDevicesRequest:
    out: UpdateDevicesRequest = {}  # type: ignore[typeddict-item]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "Devices" in data:
        import aws_sdk_sagemaker.types.devices

        out["devices"] = aws_sdk_sagemaker.types.devices.deserialize_aws_json_1_1(
            data["Devices"]
        )
    return out
