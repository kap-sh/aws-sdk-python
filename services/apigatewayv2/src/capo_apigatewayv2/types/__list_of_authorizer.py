"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfAuthorizer``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.authorizer

__listOfAuthorizer: TypeAlias = list["capo_apigatewayv2.types.authorizer.Authorizer"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAuthorizer) -> list:
    import capo_apigatewayv2.types.authorizer

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.authorizer.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAuthorizer:
    import capo_apigatewayv2.types.authorizer

    out: __listOfAuthorizer = []
    for item in data:
        out.append(capo_apigatewayv2.types.authorizer.deserialize_json(item))
    return out
