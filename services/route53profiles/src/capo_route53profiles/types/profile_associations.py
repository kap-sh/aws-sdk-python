"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53profiles.types.profile_association

ProfileAssociations: TypeAlias = list[
    "capo_route53profiles.types.profile_association.ProfileAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileAssociations) -> list:
    import capo_route53profiles.types.profile_association

    out: list = []
    for item in value:
        out.append(capo_route53profiles.types.profile_association.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileAssociations:
    import capo_route53profiles.types.profile_association

    out: ProfileAssociations = []
    for item in data:
        out.append(
            capo_route53profiles.types.profile_association.deserialize_json(item)
        )
    return out
