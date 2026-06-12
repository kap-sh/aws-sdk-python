"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainPackageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

DomainPackageStatus: TypeAlias = Literal[
    "ASSOCIATING",
    "ASSOCIATION_FAILED",
    "ACTIVE",
    "DISSOCIATING",
    "DISSOCIATION_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATING",
        "ASSOCIATION_FAILED",
        "ACTIVE",
        "DISSOCIATING",
        "DISSOCIATION_FAILED",
    )
)


def serialize_json(value: DomainPackageStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainPackageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainPackageStatus value: {data!r}")
    return cast(DomainPackageStatus, data)
