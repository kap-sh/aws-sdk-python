"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANFuotaTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.supported_rf_region


class LoRaWANFuotaTask(TypedDict, closed=True):
    rf_region: NotRequired[
        "capo_iot_wireless.types.supported_rf_region.SupportedRfRegion"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANFuotaTask) -> dict:
    out: dict = {}
    if "rf_region" in value:
        import capo_iot_wireless.types.supported_rf_region

        out["RfRegion"] = capo_iot_wireless.types.supported_rf_region.serialize_json(
            value["rf_region"]
        )
    return out


def deserialize_json(data: dict) -> LoRaWANFuotaTask:
    out: LoRaWANFuotaTask = {}  # type: ignore[typeddict-item]
    if "RfRegion" in data:
        import capo_iot_wireless.types.supported_rf_region

        out["rf_region"] = capo_iot_wireless.types.supported_rf_region.deserialize_json(
            data["RfRegion"]
        )
    return out
