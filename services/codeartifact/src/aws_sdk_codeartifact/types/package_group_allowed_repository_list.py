"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAllowedRepositoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_group_allowed_repository

PackageGroupAllowedRepositoryList: TypeAlias = list[
    "aws_sdk_codeartifact.types.package_group_allowed_repository.PackageGroupAllowedRepository"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupAllowedRepositoryList) -> list:
    import aws_sdk_codeartifact.types.package_group_allowed_repository

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeartifact.types.package_group_allowed_repository.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PackageGroupAllowedRepositoryList:
    import aws_sdk_codeartifact.types.package_group_allowed_repository

    out: PackageGroupAllowedRepositoryList = []
    for item in data:
        out.append(
            aws_sdk_codeartifact.types.package_group_allowed_repository.deserialize_json(
                item
            )
        )
    return out
