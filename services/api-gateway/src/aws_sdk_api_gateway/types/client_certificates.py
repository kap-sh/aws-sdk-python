"""Generated from Smithy shape ``com.amazonaws.apigateway#ClientCertificates``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_client_certificate
    import aws_sdk_api_gateway.types.string


class ClientCertificates(TypedDict):
    items: NotRequired[
        "aws_sdk_api_gateway.types.list_of_client_certificate.ListOfClientCertificate"
    ]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientCertificates) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_client_certificate

        out["item"] = (
            aws_sdk_api_gateway.types.list_of_client_certificate.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClientCertificates:
    out: ClientCertificates = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_client_certificate

        out["items"] = (
            aws_sdk_api_gateway.types.list_of_client_certificate.deserialize_json(
                data["item"]
            )
        )
    return out
