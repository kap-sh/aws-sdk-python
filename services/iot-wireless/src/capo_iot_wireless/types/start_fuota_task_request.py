"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_id
    import capo_iot_wireless.types.lo_ra_wan_start_fuota_task


class StartFuotaTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId"
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_start_fuota_task.LoRaWANStartFuotaTask"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StartFuotaTaskRequest) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_start_fuota_task

        out["LoRaWAN"] = (
            capo_iot_wireless.types.lo_ra_wan_start_fuota_task.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartFuotaTaskRequest:
    out: StartFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_start_fuota_task

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_start_fuota_task.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
