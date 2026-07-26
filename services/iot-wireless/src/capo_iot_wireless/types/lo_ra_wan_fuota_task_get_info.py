"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANFuotaTaskGetInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.rf_region
    import capo_iot_wireless.types.start_time


class LoRaWANFuotaTaskGetInfo(TypedDict, closed=True):
    rf_region: NotRequired["capo_iot_wireless.types.rf_region.RfRegion"]
    start_time: NotRequired["capo_iot_wireless.types.start_time.StartTime"]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANFuotaTaskGetInfo) -> dict:
    out: dict = {}
    if "rf_region" in value:
        out["RfRegion"] = value["rf_region"]
    if "start_time" in value:
        import capo_iot_wireless.types.start_time

        out["StartTime"] = capo_iot_wireless.types.start_time.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> LoRaWANFuotaTaskGetInfo:
    out: LoRaWANFuotaTaskGetInfo = {}  # type: ignore[typeddict-item]
    if "RfRegion" in data:
        out["rf_region"] = data["RfRegion"]
    if "StartTime" in data:
        import capo_iot_wireless.types.start_time

        out["start_time"] = capo_iot_wireless.types.start_time.deserialize_json(
            data["StartTime"]
        )
    return out
