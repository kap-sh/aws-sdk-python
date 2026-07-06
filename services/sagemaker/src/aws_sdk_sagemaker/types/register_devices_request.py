"""Generated from Smithy shape ``com.amazonaws.sagemaker#RegisterDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.devices
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.tag_list


class RegisterDevicesRequest(TypedDict, closed=True):
    device_fleet_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet.</p>"""
    devices: NotRequired["aws_sdk_sagemaker.types.devices.Devices"]
    """<p>A list of devices to register with SageMaker Edge Manager.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>The tags associated with devices.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDevicesRequest) -> dict:
    out: dict = {}
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "devices" in value:
        import aws_sdk_sagemaker.types.devices

        out["Devices"] = aws_sdk_sagemaker.types.devices.serialize_aws_json_1_1(
            value["devices"]
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDevicesRequest:
    out: RegisterDevicesRequest = {}  # type: ignore[typeddict-item]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "Devices" in data:
        import aws_sdk_sagemaker.types.devices

        out["devices"] = aws_sdk_sagemaker.types.devices.deserialize_aws_json_1_1(
            data["Devices"]
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
