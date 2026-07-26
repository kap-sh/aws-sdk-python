"""Generated from Smithy shape ``com.amazonaws.amplify#SubDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.sub_domain

SubDomains: TypeAlias = list["capo_amplify.types.sub_domain.SubDomain"]


# --- restJson1 ser/de ---
def serialize_json(value: SubDomains) -> list:
    import capo_amplify.types.sub_domain

    out: list = []
    for item in value:
        out.append(capo_amplify.types.sub_domain.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubDomains:
    import capo_amplify.types.sub_domain

    out: SubDomains = []
    for item in data:
        out.append(capo_amplify.types.sub_domain.deserialize_json(item))
    return out
