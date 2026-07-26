"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfDomainName``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.domain_name

__listOfDomainName: TypeAlias = list["capo_apigatewayv2.types.domain_name.DomainName"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDomainName) -> list:
    import capo_apigatewayv2.types.domain_name

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.domain_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDomainName:
    import capo_apigatewayv2.types.domain_name

    out: __listOfDomainName = []
    for item in data:
        out.append(capo_apigatewayv2.types.domain_name.deserialize_json(item))
    return out
