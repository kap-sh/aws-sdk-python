"""Generated from Smithy shape ``com.amazonaws.iotwireless#DisassociateWirelessDeviceFromFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_id
    import capo_iot_wireless.types.wireless_device_id


class DisassociateWirelessDeviceFromFuotaTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId"
    wireless_device_id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateWirelessDeviceFromFuotaTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateWirelessDeviceFromFuotaTaskRequest:
    out: DisassociateWirelessDeviceFromFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    return out
