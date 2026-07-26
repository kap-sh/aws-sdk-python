"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAllowedRepositoryUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_allowed_repository_update_type
    import capo_codeartifact.types.repository_name_list

PackageGroupAllowedRepositoryUpdate: TypeAlias = dict[
    "capo_codeartifact.types.package_group_allowed_repository_update_type.PackageGroupAllowedRepositoryUpdateType",
    "capo_codeartifact.types.repository_name_list.RepositoryNameList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PackageGroupAllowedRepositoryUpdate) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codeartifact.types.package_group_allowed_repository_update_type
        import capo_codeartifact.types.repository_name_list

        out[
            capo_codeartifact.types.package_group_allowed_repository_update_type.serialize_json(
                key
            )
        ] = capo_codeartifact.types.repository_name_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PackageGroupAllowedRepositoryUpdate:
    out: PackageGroupAllowedRepositoryUpdate = {}
    for key, value in data.items():
        import capo_codeartifact.types.package_group_allowed_repository_update_type
        import capo_codeartifact.types.repository_name_list

        out[
            capo_codeartifact.types.package_group_allowed_repository_update_type.deserialize_json(
                key
            )
        ] = capo_codeartifact.types.repository_name_list.deserialize_json(value)
    return out
