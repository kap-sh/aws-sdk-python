"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANStartFuotaTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.start_time


class LoRaWANStartFuotaTask(TypedDict, closed=True):
    start_time: NotRequired["capo_iot_wireless.types.start_time.StartTime"]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANStartFuotaTask) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_iot_wireless.types.start_time

        out["StartTime"] = capo_iot_wireless.types.start_time.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> LoRaWANStartFuotaTask:
    out: LoRaWANStartFuotaTask = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_iot_wireless.types.start_time

        out["start_time"] = capo_iot_wireless.types.start_time.deserialize_json(
            data["StartTime"]
        )
    return out
