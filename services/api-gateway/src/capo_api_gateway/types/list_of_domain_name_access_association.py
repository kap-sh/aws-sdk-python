"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfDomainNameAccessAssociation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.domain_name_access_association

ListOfDomainNameAccessAssociation: TypeAlias = list[
    "capo_api_gateway.types.domain_name_access_association.DomainNameAccessAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDomainNameAccessAssociation) -> list:
    import capo_api_gateway.types.domain_name_access_association

    out: list = []
    for item in value:
        out.append(
            capo_api_gateway.types.domain_name_access_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfDomainNameAccessAssociation:
    import capo_api_gateway.types.domain_name_access_association

    out: ListOfDomainNameAccessAssociation = []
    for item in data:
        out.append(
            capo_api_gateway.types.domain_name_access_association.deserialize_json(item)
        )
    return out
