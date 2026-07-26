"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupOriginRestrictionMode``."""

from typing import Literal, TypeAlias, cast

PackageGroupOriginRestrictionMode: TypeAlias = Literal[
    "ALLOW",
    "ALLOW_SPECIFIC_REPOSITORIES",
    "BLOCK",
    "INHERIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupOriginRestrictionMode) -> str:
    return value


def deserialize_json(data: str) -> PackageGroupOriginRestrictionMode:
    return cast(PackageGroupOriginRestrictionMode, data)
