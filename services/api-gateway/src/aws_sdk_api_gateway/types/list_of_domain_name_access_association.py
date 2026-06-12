"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfDomainNameAccessAssociation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.domain_name_access_association

ListOfDomainNameAccessAssociation: TypeAlias = list[
    "aws_sdk_api_gateway.types.domain_name_access_association.DomainNameAccessAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDomainNameAccessAssociation) -> list:
    import aws_sdk_api_gateway.types.domain_name_access_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_api_gateway.types.domain_name_access_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOfDomainNameAccessAssociation:
    import aws_sdk_api_gateway.types.domain_name_access_association

    out: ListOfDomainNameAccessAssociation = []
    for item in data:
        out.append(
            aws_sdk_api_gateway.types.domain_name_access_association.deserialize_json(
                item
            )
        )
    return out
