"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfGatewayResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.gateway_response

ListOfGatewayResponse: TypeAlias = list[
    "aws_sdk_api_gateway.types.gateway_response.GatewayResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfGatewayResponse) -> list:
    import aws_sdk_api_gateway.types.gateway_response

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.gateway_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfGatewayResponse:
    import aws_sdk_api_gateway.types.gateway_response

    out: ListOfGatewayResponse = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.gateway_response.deserialize_json(item))
    return out
