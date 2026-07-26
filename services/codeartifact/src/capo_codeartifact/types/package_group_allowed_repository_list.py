"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAllowedRepositoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_allowed_repository

PackageGroupAllowedRepositoryList: TypeAlias = list[
    "capo_codeartifact.types.package_group_allowed_repository.PackageGroupAllowedRepository"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupAllowedRepositoryList) -> list:
    import capo_codeartifact.types.package_group_allowed_repository

    out: list = []
    for item in value:
        out.append(
            capo_codeartifact.types.package_group_allowed_repository.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PackageGroupAllowedRepositoryList:
    import capo_codeartifact.types.package_group_allowed_repository

    out: PackageGroupAllowedRepositoryList = []
    for item in data:
        out.append(
            capo_codeartifact.types.package_group_allowed_repository.deserialize_json(
                item
            )
        )
    return out
