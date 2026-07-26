"""Generated from Smithy shape ``com.amazonaws.iotwireless#DisassociateWirelessGatewayFromCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_id


class DisassociateWirelessGatewayFromCertificateRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateWirelessGatewayFromCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateWirelessGatewayFromCertificateRequest:
    out: DisassociateWirelessGatewayFromCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
