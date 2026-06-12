"""Generated from Smithy shape ``com.amazonaws.braket#GetDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_braket.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_braket.types.device_arn
    import aws_sdk_braket.types.device_queue_info_list
    import aws_sdk_braket.types.device_status
    import aws_sdk_braket.types.device_type
    import aws_sdk_braket.types.json_value

class GetDeviceResponse(TypedDict):
    device_arn: "aws_sdk_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device.</p>"""
    device_name: "str"
    """<p>The name of the device.</p>"""
    provider_name: "str"
    """<p>The name of the partner company for the device.</p>"""
    device_type: "aws_sdk_braket.types.device_type.DeviceType"
    """<p>The type of the device.</p>"""
    device_status: "aws_sdk_braket.types.device_status.DeviceStatus"
    """<p>The status of the device.</p>"""
    device_capabilities: "aws_sdk_braket.types.json_value.JsonValue"
    """<p>Details about the capabilities of the device.</p>"""
    device_queue_info: NotRequired["aws_sdk_braket.types.device_queue_info_list.DeviceQueueInfoList"]
    """<p>The number of quantum tasks and hybrid jobs currently queued on the device.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceResponse) -> dict:
    out: dict = {}
    out["deviceArn"] = value["device_arn"]
    out["deviceName"] = value["device_name"]
    out["providerName"] = value["provider_name"]
    out["deviceType"] = value["device_type"]
    out["deviceStatus"] = value["device_status"]
    out["deviceCapabilities"] = value["device_capabilities"]
    if "device_queue_info" in value:
        import aws_sdk_braket.types.device_queue_info_list
        out["deviceQueueInfo"] = aws_sdk_braket.types.device_queue_info_list.serialize_json(value["device_queue_info"])
    return out


def deserialize_json(data: dict) -> GetDeviceResponse:
    out: GetDeviceResponse = {}  # type: ignore[typeddict-item]
    if "deviceArn" in data:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError("GetDeviceResponse.device_arn required")
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    else:
        raise DeserializationError("GetDeviceResponse.device_name required")
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    else:
        raise DeserializationError("GetDeviceResponse.provider_name required")
    if "deviceType" in data:
        out["device_type"] = data["deviceType"]
    else:
        raise DeserializationError("GetDeviceResponse.device_type required")
    if "deviceStatus" in data:
        out["device_status"] = data["deviceStatus"]
    else:
        raise DeserializationError("GetDeviceResponse.device_status required")
    if "deviceCapabilities" in data:
        out["device_capabilities"] = data["deviceCapabilities"]
    else:
        raise DeserializationError("GetDeviceResponse.device_capabilities required")
    if "deviceQueueInfo" in data:
        import aws_sdk_braket.types.device_queue_info_list
        out["device_queue_info"] = aws_sdk_braket.types.device_queue_info_list.deserialize_json(data["deviceQueueInfo"])
    return out