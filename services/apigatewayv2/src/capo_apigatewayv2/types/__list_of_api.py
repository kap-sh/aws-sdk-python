"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfApi``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.api

__listOfApi: TypeAlias = list["capo_apigatewayv2.types.api.Api"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfApi) -> list:
    import capo_apigatewayv2.types.api

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.api.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfApi:
    import capo_apigatewayv2.types.api

    out: __listOfApi = []
    for item in data:
        out.append(capo_apigatewayv2.types.api.deserialize_json(item))
    return out
