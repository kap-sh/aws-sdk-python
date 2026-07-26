"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfDomainName``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.domain_name

ListOfDomainName: TypeAlias = list["capo_api_gateway.types.domain_name.DomainName"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDomainName) -> list:
    import capo_api_gateway.types.domain_name

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.domain_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfDomainName:
    import capo_api_gateway.types.domain_name

    out: ListOfDomainName = []
    for item in data:
        out.append(capo_api_gateway.types.domain_name.deserialize_json(item))
    return out
