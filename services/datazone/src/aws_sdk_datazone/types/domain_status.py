"""Generated from Smithy shape ``com.amazonaws.datazone#DomainStatus``."""

from typing import Literal, TypeAlias, cast

DomainStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "CREATION_FAILED",
    "DELETING",
    "DELETED",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainStatus:
    return cast(DomainStatus, data)
