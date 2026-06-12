"""Generated from Smithy shape ``com.amazonaws.amplify#DomainAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.domain_association

DomainAssociations: TypeAlias = list[
    "aws_sdk_amplify.types.domain_association.DomainAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainAssociations) -> list:
    import aws_sdk_amplify.types.domain_association

    out: list = []
    for item in value:
        out.append(aws_sdk_amplify.types.domain_association.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainAssociations:
    import aws_sdk_amplify.types.domain_association

    out: DomainAssociations = []
    for item in data:
        out.append(aws_sdk_amplify.types.domain_association.deserialize_json(item))
    return out
