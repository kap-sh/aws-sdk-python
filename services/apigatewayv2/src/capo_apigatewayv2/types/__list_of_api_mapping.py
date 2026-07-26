"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfApiMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.api_mapping

__listOfApiMapping: TypeAlias = list["capo_apigatewayv2.types.api_mapping.ApiMapping"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfApiMapping) -> list:
    import capo_apigatewayv2.types.api_mapping

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.api_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfApiMapping:
    import capo_apigatewayv2.types.api_mapping

    out: __listOfApiMapping = []
    for item in data:
        out.append(capo_apigatewayv2.types.api_mapping.deserialize_json(item))
    return out
