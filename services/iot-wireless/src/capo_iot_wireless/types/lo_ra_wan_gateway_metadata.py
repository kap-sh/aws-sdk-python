"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANGatewayMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.double
    import capo_iot_wireless.types.gateway_eui


class LoRaWANGatewayMetadata(TypedDict, closed=True):
    gateway_eui: NotRequired["capo_iot_wireless.types.gateway_eui.GatewayEui"]
    """<p>The gateway's EUI value.</p>"""
    snr: NotRequired["capo_iot_wireless.types.double.Double"]
    """<p>The SNR value.</p>"""
    rssi: NotRequired["capo_iot_wireless.types.double.Double"]
    """<p>The RSSI value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANGatewayMetadata) -> dict:
    out: dict = {}
    if "gateway_eui" in value:
        out["GatewayEui"] = value["gateway_eui"]
    if "snr" in value:
        out["Snr"] = value["snr"]
    if "rssi" in value:
        out["Rssi"] = value["rssi"]
    return out


def deserialize_json(data: dict) -> LoRaWANGatewayMetadata:
    out: LoRaWANGatewayMetadata = {}  # type: ignore[typeddict-item]
    if "GatewayEui" in data:
        out["gateway_eui"] = data["GatewayEui"]
    if "Snr" in data:
        out["snr"] = data["Snr"]
    if "Rssi" in data:
        out["rssi"] = data["Rssi"]
    return out
