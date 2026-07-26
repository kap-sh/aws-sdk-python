"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DomainNameConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.domain_name_configuration

DomainNameConfigurations: TypeAlias = list[
    "capo_apigatewayv2.types.domain_name_configuration.DomainNameConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameConfigurations) -> list:
    import capo_apigatewayv2.types.domain_name_configuration

    out: list = []
    for item in value:
        out.append(
            capo_apigatewayv2.types.domain_name_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DomainNameConfigurations:
    import capo_apigatewayv2.types.domain_name_configuration

    out: DomainNameConfigurations = []
    for item in data:
        out.append(
            capo_apigatewayv2.types.domain_name_configuration.deserialize_json(item)
        )
    return out
