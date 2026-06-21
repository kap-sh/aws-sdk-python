"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAssociationType``."""

from typing import Literal, TypeAlias, cast

PackageGroupAssociationType: TypeAlias = Literal[
    "STRONG",
    "WEAK",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupAssociationType) -> str:
    return value


def deserialize_json(data: str) -> PackageGroupAssociationType:
    return cast(PackageGroupAssociationType, data)
