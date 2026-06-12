"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PackageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "COPYING",
        "COPY_FAILED",
        "VALIDATING",
        "VALIDATION_FAILED",
        "AVAILABLE",
        "DELETING",
        "DELETED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: PackageStatus) -> str:
    return value


def deserialize_json(data: str) -> PackageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageStatus value: {data!r}")
    return cast(PackageStatus, data)
