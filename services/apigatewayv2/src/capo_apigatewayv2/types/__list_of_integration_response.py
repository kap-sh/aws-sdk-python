"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfIntegrationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.integration_response

__listOfIntegrationResponse: TypeAlias = list[
    "capo_apigatewayv2.types.integration_response.IntegrationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfIntegrationResponse) -> list:
    import capo_apigatewayv2.types.integration_response

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.integration_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfIntegrationResponse:
    import capo_apigatewayv2.types.integration_response

    out: __listOfIntegrationResponse = []
    for item in data:
        out.append(capo_apigatewayv2.types.integration_response.deserialize_json(item))
    return out
