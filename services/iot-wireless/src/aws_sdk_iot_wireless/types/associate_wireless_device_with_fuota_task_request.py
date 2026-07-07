"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateWirelessDeviceWithFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.fuota_task_id
    import aws_sdk_iot_wireless.types.wireless_device_id


class AssociateWirelessDeviceWithFuotaTaskRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId"
    wireless_device_id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWirelessDeviceWithFuotaTaskRequest) -> dict:
    out: dict = {}
    out["WirelessDeviceId"] = value["wireless_device_id"]
    return out


def deserialize_json(data: dict) -> AssociateWirelessDeviceWithFuotaTaskRequest:
    out: AssociateWirelessDeviceWithFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    if "WirelessDeviceId" in data:
        out["wireless_device_id"] = data["WirelessDeviceId"]
    else:
        raise DeserializationError(
            "AssociateWirelessDeviceWithFuotaTaskRequest.wireless_device_id required"
        )
    return out
