"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PackageStatus``."""

from typing import Literal, TypeAlias, cast

PackageStatus: TypeAlias = Literal[
    "COPYING",
    "COPY_FAILED",
    "VALIDATING",
    "VALIDATION_FAILED",
    "AVAILABLE",
    "DELETING",
    "DELETED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageStatus) -> str:
    return value


def deserialize_json(data: str) -> PackageStatus:
    return cast(PackageStatus, data)
