"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionStatus``."""

from typing import Literal, TypeAlias, cast

PackageVersionStatus: TypeAlias = Literal[
    "Published",
    "Unfinished",
    "Unlisted",
    "Archived",
    "Disposed",
    "Deleted",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionStatus:
    return cast(PackageVersionStatus, data)
