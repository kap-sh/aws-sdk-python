"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetServiceEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.certificate_pem
    import capo_iot_wireless.types.end_point
    import capo_iot_wireless.types.wireless_gateway_service_type


class GetServiceEndpointResponse(TypedDict, closed=True):
    service_type: NotRequired[
        "capo_iot_wireless.types.wireless_gateway_service_type.WirelessGatewayServiceType"
    ]
    """<p>The endpoint's service type.</p>"""
    service_endpoint: NotRequired["capo_iot_wireless.types.end_point.EndPoint"]
    """<p>The service endpoint value.</p>"""
    server_trust: NotRequired["capo_iot_wireless.types.certificate_pem.CertificatePEM"]
    """<p>The Root CA of the server trust certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceEndpointResponse) -> dict:
    out: dict = {}
    if "service_type" in value:
        import capo_iot_wireless.types.wireless_gateway_service_type

        out["ServiceType"] = (
            capo_iot_wireless.types.wireless_gateway_service_type.serialize_json(
                value["service_type"]
            )
        )
    if "service_endpoint" in value:
        out["ServiceEndpoint"] = value["service_endpoint"]
    if "server_trust" in value:
        out["ServerTrust"] = value["server_trust"]
    return out


def deserialize_json(data: dict) -> GetServiceEndpointResponse:
    out: GetServiceEndpointResponse = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import capo_iot_wireless.types.wireless_gateway_service_type

        out["service_type"] = (
            capo_iot_wireless.types.wireless_gateway_service_type.deserialize_json(
                data["ServiceType"]
            )
        )
    if "ServiceEndpoint" in data:
        out["service_endpoint"] = data["ServiceEndpoint"]
    if "ServerTrust" in data:
        out["server_trust"] = data["ServerTrust"]
    return out
