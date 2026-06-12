"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateWirelessGatewayWithCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.iot_certificate_id
    import aws_sdk_iot_wireless.types.wireless_gateway_id


class AssociateWirelessGatewayWithCertificateRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to update.</p>"""
    iot_certificate_id: "aws_sdk_iot_wireless.types.iot_certificate_id.IotCertificateId"
    """<p>The ID of the certificate to associate with the wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWirelessGatewayWithCertificateRequest) -> dict:
    out: dict = {}
    out["IotCertificateId"] = value["iot_certificate_id"]
    return out


def deserialize_json(data: dict) -> AssociateWirelessGatewayWithCertificateRequest:
    out: AssociateWirelessGatewayWithCertificateRequest = {}  # type: ignore[typeddict-item]
    if "IotCertificateId" in data:
        out["iot_certificate_id"] = data["IotCertificateId"]
    else:
        raise DeserializationError(
            "AssociateWirelessGatewayWithCertificateRequest.iot_certificate_id required"
        )
    return out
