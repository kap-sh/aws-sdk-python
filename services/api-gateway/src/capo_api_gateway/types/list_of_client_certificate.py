"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfClientCertificate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.client_certificate

ListOfClientCertificate: TypeAlias = list[
    "capo_api_gateway.types.client_certificate.ClientCertificate"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfClientCertificate) -> list:
    import capo_api_gateway.types.client_certificate

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.client_certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfClientCertificate:
    import capo_api_gateway.types.client_certificate

    out: ListOfClientCertificate = []
    for item in data:
        out.append(capo_api_gateway.types.client_certificate.deserialize_json(item))
    return out
