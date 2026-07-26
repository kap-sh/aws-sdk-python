"""Generated from Smithy shape ``com.amazonaws.iotwireless#DisassociateMulticastGroupFromFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_id
    import capo_iot_wireless.types.multicast_group_id


class DisassociateMulticastGroupFromFuotaTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId"
    multicast_group_id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMulticastGroupFromFuotaTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMulticastGroupFromFuotaTaskRequest:
    out: DisassociateMulticastGroupFromFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    return out
