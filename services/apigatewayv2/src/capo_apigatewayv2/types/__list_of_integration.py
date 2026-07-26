"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfIntegration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.integration

__listOfIntegration: TypeAlias = list["capo_apigatewayv2.types.integration.Integration"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfIntegration) -> list:
    import capo_apigatewayv2.types.integration

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.integration.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfIntegration:
    import capo_apigatewayv2.types.integration

    out: __listOfIntegration = []
    for item in data:
        out.append(capo_apigatewayv2.types.integration.deserialize_json(item))
    return out
