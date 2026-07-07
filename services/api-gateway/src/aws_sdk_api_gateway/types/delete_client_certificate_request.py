"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteClientCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteClientCertificateRequest(TypedDict, closed=True):
    client_certificate_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the ClientCertificate resource to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClientCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClientCertificateRequest:
    out: DeleteClientCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
