"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteDevicePositionHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_location.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_location.types.device_ids_list
    import aws_sdk_location.types.resource_name

class BatchDeleteDevicePositionHistoryRequest(TypedDict):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to delete the device position history from.</p>"""
    device_ids: "aws_sdk_location.types.device_ids_list.DeviceIdsList"
    """<p>Devices whose position history you want to delete.</p> <ul> <li> <p>For example, for two devices: <code>“DeviceIds” : [DeviceId1,DeviceId2]</code> </p> </li> </ul>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDevicePositionHistoryRequest) -> dict:
    out: dict = {}
    import aws_sdk_location.types.device_ids_list
    out["DeviceIds"] = aws_sdk_location.types.device_ids_list.serialize_json(value["device_ids"])
    return out


def deserialize_json(data: dict) -> BatchDeleteDevicePositionHistoryRequest:
    out: BatchDeleteDevicePositionHistoryRequest = {}  # type: ignore[typeddict-item]
    if "DeviceIds" in data:
        import aws_sdk_location.types.device_ids_list
        out["device_ids"] = aws_sdk_location.types.device_ids_list.deserialize_json(data["DeviceIds"])
    else:
        raise DeserializationError("BatchDeleteDevicePositionHistoryRequest.device_ids required")
    return out