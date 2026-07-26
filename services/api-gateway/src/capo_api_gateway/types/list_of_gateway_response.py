"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfGatewayResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.gateway_response

ListOfGatewayResponse: TypeAlias = list[
    "capo_api_gateway.types.gateway_response.GatewayResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfGatewayResponse) -> list:
    import capo_api_gateway.types.gateway_response

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.gateway_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfGatewayResponse:
    import capo_api_gateway.types.gateway_response

    out: ListOfGatewayResponse = []
    for item in data:
        out.append(capo_api_gateway.types.gateway_response.deserialize_json(item))
    return out
