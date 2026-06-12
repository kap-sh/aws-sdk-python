"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANFuotaTaskGetInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.rf_region
    import aws_sdk_iot_wireless.types.start_time


class LoRaWANFuotaTaskGetInfo(TypedDict):
    rf_region: NotRequired["aws_sdk_iot_wireless.types.rf_region.RfRegion"]
    start_time: NotRequired["aws_sdk_iot_wireless.types.start_time.StartTime"]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANFuotaTaskGetInfo) -> dict:
    out: dict = {}
    if "rf_region" in value:
        out["RfRegion"] = value["rf_region"]
    if "start_time" in value:
        import aws_sdk_iot_wireless.types.start_time

        out["StartTime"] = aws_sdk_iot_wireless.types.start_time.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> LoRaWANFuotaTaskGetInfo:
    out: LoRaWANFuotaTaskGetInfo = {}  # type: ignore[typeddict-item]
    if "RfRegion" in data:
        out["rf_region"] = data["RfRegion"]
    if "StartTime" in data:
        import aws_sdk_iot_wireless.types.start_time

        out["start_time"] = aws_sdk_iot_wireless.types.start_time.deserialize_json(
            data["StartTime"]
        )
    return out
