"""Generated from Smithy shape ``com.amazonaws.amplify#DomainAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.domain_association

DomainAssociations: TypeAlias = list[
    "capo_amplify.types.domain_association.DomainAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainAssociations) -> list:
    import capo_amplify.types.domain_association

    out: list = []
    for item in value:
        out.append(capo_amplify.types.domain_association.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainAssociations:
    import capo_amplify.types.domain_association

    out: DomainAssociations = []
    for item in data:
        out.append(capo_amplify.types.domain_association.deserialize_json(item))
    return out
