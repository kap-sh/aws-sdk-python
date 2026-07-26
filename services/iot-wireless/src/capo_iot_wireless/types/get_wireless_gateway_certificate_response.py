"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.iot_certificate_id


class GetWirelessGatewayCertificateResponse(TypedDict, closed=True):
    iot_certificate_id: NotRequired[
        "capo_iot_wireless.types.iot_certificate_id.IotCertificateId"
    ]
    """<p>The ID of the certificate associated with the wireless gateway.</p>"""
    lo_ra_wan_network_server_certificate_id: NotRequired[
        "capo_iot_wireless.types.iot_certificate_id.IotCertificateId"
    ]
    """<p>The ID of the certificate that is associated with the wireless gateway and used for the LoRaWANNetworkServer endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayCertificateResponse) -> dict:
    out: dict = {}
    if "iot_certificate_id" in value:
        out["IotCertificateId"] = value["iot_certificate_id"]
    if "lo_ra_wan_network_server_certificate_id" in value:
        out["LoRaWANNetworkServerCertificateId"] = value[
            "lo_ra_wan_network_server_certificate_id"
        ]
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayCertificateResponse:
    out: GetWirelessGatewayCertificateResponse = {}  # type: ignore[typeddict-item]
    if "IotCertificateId" in data:
        out["iot_certificate_id"] = data["IotCertificateId"]
    if "LoRaWANNetworkServerCertificateId" in data:
        out["lo_ra_wan_network_server_certificate_id"] = data[
            "LoRaWANNetworkServerCertificateId"
        ]
    return out
