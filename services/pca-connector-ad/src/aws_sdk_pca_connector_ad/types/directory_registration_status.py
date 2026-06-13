"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DirectoryRegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

DirectoryRegistrationStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: DirectoryRegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> DirectoryRegistrationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectoryRegistrationStatus value: {data!r}"
        )
    return cast(DirectoryRegistrationStatus, data)
