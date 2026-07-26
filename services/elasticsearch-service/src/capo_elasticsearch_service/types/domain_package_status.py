"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainPackageStatus``."""

from typing import Literal, TypeAlias, cast

DomainPackageStatus: TypeAlias = Literal[
    "ASSOCIATING",
    "ASSOCIATION_FAILED",
    "ACTIVE",
    "DISSOCIATING",
    "DISSOCIATION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainPackageStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainPackageStatus:
    return cast(DomainPackageStatus, data)
