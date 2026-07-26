"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfSection``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.section

__listOfSection: TypeAlias = list["capo_apigatewayv2.types.section.Section"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSection) -> list:
    import capo_apigatewayv2.types.section

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.section.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSection:
    import capo_apigatewayv2.types.section

    out: __listOfSection = []
    for item in data:
        out.append(capo_apigatewayv2.types.section.deserialize_json(item))
    return out
