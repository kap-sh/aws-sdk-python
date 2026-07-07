"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.fuota_task_id
    import aws_sdk_iot_wireless.types.lo_ra_wan_start_fuota_task


class StartFuotaTaskRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId"
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_start_fuota_task.LoRaWANStartFuotaTask"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StartFuotaTaskRequest) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_start_fuota_task

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_start_fuota_task.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartFuotaTaskRequest:
    out: StartFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_start_fuota_task

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_start_fuota_task.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
