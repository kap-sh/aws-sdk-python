"""Generated from Smithy shape ``com.amazonaws.apigateway#GetClientCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetClientCertificateRequest(TypedDict):
    client_certificate_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the ClientCertificate resource to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClientCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetClientCertificateRequest:
    out: GetClientCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
