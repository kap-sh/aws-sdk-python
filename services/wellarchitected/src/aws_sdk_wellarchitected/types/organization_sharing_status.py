"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationSharingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

OrganizationSharingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: OrganizationSharingStatus) -> str:
    return value


def deserialize_json(data: str) -> OrganizationSharingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrganizationSharingStatus value: {data!r}")
    return cast(OrganizationSharingStatus, data)
