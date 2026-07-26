"""Generated from Smithy shape ``com.amazonaws.iot#PackageVersionStatus``."""

from typing import Literal, TypeAlias, cast

PackageVersionStatus: TypeAlias = Literal[
    "DRAFT",
    "PUBLISHED",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionStatus:
    return cast(PackageVersionStatus, data)
