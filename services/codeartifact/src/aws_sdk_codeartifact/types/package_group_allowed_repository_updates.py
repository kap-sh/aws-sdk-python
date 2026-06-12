"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAllowedRepositoryUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_group_allowed_repository_update
    import aws_sdk_codeartifact.types.package_group_origin_restriction_type

PackageGroupAllowedRepositoryUpdates: TypeAlias = dict[
    "aws_sdk_codeartifact.types.package_group_origin_restriction_type.PackageGroupOriginRestrictionType",
    "aws_sdk_codeartifact.types.package_group_allowed_repository_update.PackageGroupAllowedRepositoryUpdate",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PackageGroupAllowedRepositoryUpdates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_codeartifact.types.package_group_allowed_repository_update
        import aws_sdk_codeartifact.types.package_group_origin_restriction_type

        out[
            aws_sdk_codeartifact.types.package_group_origin_restriction_type.serialize_json(
                key
            )
        ] = aws_sdk_codeartifact.types.package_group_allowed_repository_update.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> PackageGroupAllowedRepositoryUpdates:
    out: PackageGroupAllowedRepositoryUpdates = {}
    for key, value in data.items():
        import aws_sdk_codeartifact.types.package_group_allowed_repository_update
        import aws_sdk_codeartifact.types.package_group_origin_restriction_type

        out[
            aws_sdk_codeartifact.types.package_group_origin_restriction_type.deserialize_json(
                key
            )
        ] = aws_sdk_codeartifact.types.package_group_allowed_repository_update.deserialize_json(
            value
        )
    return out
