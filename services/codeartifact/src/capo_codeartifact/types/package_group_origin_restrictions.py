"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupOriginRestrictions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_origin_restriction
    import capo_codeartifact.types.package_group_origin_restriction_type

PackageGroupOriginRestrictions: TypeAlias = dict[
    "capo_codeartifact.types.package_group_origin_restriction_type.PackageGroupOriginRestrictionType",
    "capo_codeartifact.types.package_group_origin_restriction.PackageGroupOriginRestriction",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PackageGroupOriginRestrictions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codeartifact.types.package_group_origin_restriction
        import capo_codeartifact.types.package_group_origin_restriction_type

        out[
            capo_codeartifact.types.package_group_origin_restriction_type.serialize_json(
                key
            )
        ] = capo_codeartifact.types.package_group_origin_restriction.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> PackageGroupOriginRestrictions:
    out: PackageGroupOriginRestrictions = {}
    for key, value in data.items():
        import capo_codeartifact.types.package_group_origin_restriction
        import capo_codeartifact.types.package_group_origin_restriction_type

        out[
            capo_codeartifact.types.package_group_origin_restriction_type.deserialize_json(
                key
            )
        ] = capo_codeartifact.types.package_group_origin_restriction.deserialize_json(
            value
        )
    return out
