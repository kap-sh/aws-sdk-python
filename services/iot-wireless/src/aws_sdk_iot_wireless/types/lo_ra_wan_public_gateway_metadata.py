"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANPublicGatewayMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.dl_allowed
    import aws_sdk_iot_wireless.types.double
    import aws_sdk_iot_wireless.types.id
    import aws_sdk_iot_wireless.types.provider_net_id
    import aws_sdk_iot_wireless.types.rf_region


class LoRaWANPublicGatewayMetadata(TypedDict):
    provider_net_id: NotRequired[
        "aws_sdk_iot_wireless.types.provider_net_id.ProviderNetId"
    ]
    """<p>The ID of the LoRaWAN public network provider.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.id.Id"]
    """<p>The ID of the gateways that are operated by the network provider.</p>"""
    rssi: NotRequired["aws_sdk_iot_wireless.types.double.Double"]
    """<p>The RSSI (received signal strength indicator) value.</p>"""
    snr: NotRequired["aws_sdk_iot_wireless.types.double.Double"]
    """<p>The SNR (signal to noise ratio) value.</p>"""
    rf_region: NotRequired["aws_sdk_iot_wireless.types.rf_region.RfRegion"]
    dl_allowed: NotRequired["aws_sdk_iot_wireless.types.dl_allowed.DlAllowed"]
    """<p>Boolean that indicates whether downlink is allowed using the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANPublicGatewayMetadata) -> dict:
    out: dict = {}
    if "provider_net_id" in value:
        out["ProviderNetId"] = value["provider_net_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "rssi" in value:
        out["Rssi"] = value["rssi"]
    if "snr" in value:
        out["Snr"] = value["snr"]
    if "rf_region" in value:
        out["RfRegion"] = value["rf_region"]
    if "dl_allowed" in value:
        out["DlAllowed"] = value["dl_allowed"]
    return out


def deserialize_json(data: dict) -> LoRaWANPublicGatewayMetadata:
    out: LoRaWANPublicGatewayMetadata = {}  # type: ignore[typeddict-item]
    if "ProviderNetId" in data:
        out["provider_net_id"] = data["ProviderNetId"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Rssi" in data:
        out["rssi"] = data["Rssi"]
    if "Snr" in data:
        out["snr"] = data["Snr"]
    if "RfRegion" in data:
        out["rf_region"] = data["RfRegion"]
    if "DlAllowed" in data:
        out["dl_allowed"] = data["DlAllowed"]
    return out
