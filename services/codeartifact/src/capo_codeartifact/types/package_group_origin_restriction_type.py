"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupOriginRestrictionType``."""

from typing import Literal, TypeAlias, cast

PackageGroupOriginRestrictionType: TypeAlias = Literal[
    "EXTERNAL_UPSTREAM",
    "INTERNAL_UPSTREAM",
    "PUBLISH",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupOriginRestrictionType) -> str:
    return value


def deserialize_json(data: str) -> PackageGroupOriginRestrictionType:
    return cast(PackageGroupOriginRestrictionType, data)
