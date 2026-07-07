"""Generated from Smithy shape ``com.amazonaws.apigateway#ClientCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string
    import aws_sdk_api_gateway.types.timestamp


class ClientCertificate(TypedDict, closed=True):
    client_certificate_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The identifier of the client certificate.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of the client certificate.</p>"""
    pem_encoded_certificate: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .</p>"""
    created_date: NotRequired["aws_sdk_api_gateway.types.timestamp.Timestamp"]
    """<p>The timestamp when the client certificate was created.</p>"""
    expiration_date: NotRequired["aws_sdk_api_gateway.types.timestamp.Timestamp"]
    """<p>The timestamp when the client certificate will expire.</p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientCertificate) -> dict:
    out: dict = {}
    if "client_certificate_id" in value:
        out["clientCertificateId"] = value["client_certificate_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "pem_encoded_certificate" in value:
        out["pemEncodedCertificate"] = value["pem_encoded_certificate"]
    if "created_date" in value:
        import aws_sdk_api_gateway.types.timestamp

        out["createdDate"] = aws_sdk_api_gateway.types.timestamp.serialize_json(
            value["created_date"]
        )
    if "expiration_date" in value:
        import aws_sdk_api_gateway.types.timestamp

        out["expirationDate"] = aws_sdk_api_gateway.types.timestamp.serialize_json(
            value["expiration_date"]
        )
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ClientCertificate:
    out: ClientCertificate = {}  # type: ignore[typeddict-item]
    if "clientCertificateId" in data:
        out["client_certificate_id"] = data["clientCertificateId"]
    if "description" in data:
        out["description"] = data["description"]
    if "pemEncodedCertificate" in data:
        out["pem_encoded_certificate"] = data["pemEncodedCertificate"]
    if "createdDate" in data:
        import aws_sdk_api_gateway.types.timestamp

        out["created_date"] = aws_sdk_api_gateway.types.timestamp.deserialize_json(
            data["createdDate"]
        )
    if "expirationDate" in data:
        import aws_sdk_api_gateway.types.timestamp

        out["expiration_date"] = aws_sdk_api_gateway.types.timestamp.deserialize_json(
            data["expirationDate"]
        )
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    return out
