"""Generated from Smithy shape ``com.amazonaws.codeartifact#OriginRestrictions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_origin_restriction_mode
    import capo_codeartifact.types.package_group_origin_restriction_type

OriginRestrictions: TypeAlias = dict[
    "capo_codeartifact.types.package_group_origin_restriction_type.PackageGroupOriginRestrictionType",
    "capo_codeartifact.types.package_group_origin_restriction_mode.PackageGroupOriginRestrictionMode",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: OriginRestrictions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codeartifact.types.package_group_origin_restriction_mode
        import capo_codeartifact.types.package_group_origin_restriction_type

        out[
            capo_codeartifact.types.package_group_origin_restriction_type.serialize_json(
                key
            )
        ] = capo_codeartifact.types.package_group_origin_restriction_mode.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> OriginRestrictions:
    out: OriginRestrictions = {}
    for key, value in data.items():
        import capo_codeartifact.types.package_group_origin_restriction_mode
        import capo_codeartifact.types.package_group_origin_restriction_type

        out[
            capo_codeartifact.types.package_group_origin_restriction_type.deserialize_json(
                key
            )
        ] = capo_codeartifact.types.package_group_origin_restriction_mode.deserialize_json(
            value
        )
    return out
