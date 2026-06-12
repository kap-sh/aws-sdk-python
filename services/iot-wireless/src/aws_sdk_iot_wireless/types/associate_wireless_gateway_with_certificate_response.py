"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateWirelessGatewayWithCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.iot_certificate_id


class AssociateWirelessGatewayWithCertificateResponse(TypedDict):
    iot_certificate_id: NotRequired[
        "aws_sdk_iot_wireless.types.iot_certificate_id.IotCertificateId"
    ]
    """<p>The ID of the certificate associated with the wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWirelessGatewayWithCertificateResponse) -> dict:
    out: dict = {}
    if "iot_certificate_id" in value:
        out["IotCertificateId"] = value["iot_certificate_id"]
    return out


def deserialize_json(data: dict) -> AssociateWirelessGatewayWithCertificateResponse:
    out: AssociateWirelessGatewayWithCertificateResponse = {}  # type: ignore[typeddict-item]
    if "IotCertificateId" in data:
        out["iot_certificate_id"] = data["IotCertificateId"]
    return out
