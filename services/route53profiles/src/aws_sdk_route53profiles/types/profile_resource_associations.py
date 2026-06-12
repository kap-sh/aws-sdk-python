"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileResourceAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.profile_resource_association

ProfileResourceAssociations: TypeAlias = list[
    "aws_sdk_route53profiles.types.profile_resource_association.ProfileResourceAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileResourceAssociations) -> list:
    import aws_sdk_route53profiles.types.profile_resource_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53profiles.types.profile_resource_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProfileResourceAssociations:
    import aws_sdk_route53profiles.types.profile_resource_association

    out: ProfileResourceAssociations = []
    for item in data:
        out.append(
            aws_sdk_route53profiles.types.profile_resource_association.deserialize_json(
                item
            )
        )
    return out
