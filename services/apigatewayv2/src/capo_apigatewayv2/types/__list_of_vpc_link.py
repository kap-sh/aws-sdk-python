"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfVpcLink``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.vpc_link

__listOfVpcLink: TypeAlias = list["capo_apigatewayv2.types.vpc_link.VpcLink"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVpcLink) -> list:
    import capo_apigatewayv2.types.vpc_link

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.vpc_link.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVpcLink:
    import capo_apigatewayv2.types.vpc_link

    out: __listOfVpcLink = []
    for item in data:
        out.append(capo_apigatewayv2.types.vpc_link.deserialize_json(item))
    return out
