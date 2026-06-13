"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DirectoryRegistrationStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

DirectoryRegistrationStatusReason: TypeAlias = Literal[
    "DIRECTORY_ACCESS_DENIED",
    "DIRECTORY_RESOURCE_NOT_FOUND",
    "DIRECTORY_NOT_ACTIVE",
    "DIRECTORY_NOT_REACHABLE",
    "DIRECTORY_TYPE_NOT_SUPPORTED",
    "INTERNAL_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECTORY_ACCESS_DENIED",
        "DIRECTORY_RESOURCE_NOT_FOUND",
        "DIRECTORY_NOT_ACTIVE",
        "DIRECTORY_NOT_REACHABLE",
        "DIRECTORY_TYPE_NOT_SUPPORTED",
        "INTERNAL_FAILURE",
    )
)


def serialize_json(value: DirectoryRegistrationStatusReason) -> str:
    return value


def deserialize_json(data: str) -> DirectoryRegistrationStatusReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectoryRegistrationStatusReason value: {data!r}"
        )
    return cast(DirectoryRegistrationStatusReason, data)
