"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAllowedRepositoryUpdateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

PackageGroupAllowedRepositoryUpdateType: TypeAlias = Literal[
    "ADDED",
    "REMOVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADDED",
        "REMOVED",
    )
)


def serialize_json(value: PackageGroupAllowedRepositoryUpdateType) -> str:
    return value


def deserialize_json(data: str) -> PackageGroupAllowedRepositoryUpdateType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PackageGroupAllowedRepositoryUpdateType value: {data!r}"
        )
    return cast(PackageGroupAllowedRepositoryUpdateType, data)
