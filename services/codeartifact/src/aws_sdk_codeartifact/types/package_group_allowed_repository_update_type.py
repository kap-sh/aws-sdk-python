"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAllowedRepositoryUpdateType``."""

from typing import Literal, TypeAlias, cast

PackageGroupAllowedRepositoryUpdateType: TypeAlias = Literal[
    "ADDED",
    "REMOVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupAllowedRepositoryUpdateType) -> str:
    return value


def deserialize_json(data: str) -> PackageGroupAllowedRepositoryUpdateType:
    return cast(PackageGroupAllowedRepositoryUpdateType, data)
