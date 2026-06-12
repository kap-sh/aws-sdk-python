"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

LinkAssociationState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: LinkAssociationState) -> str:
    return value


def deserialize_json(data: str) -> LinkAssociationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LinkAssociationState value: {data!r}")
    return cast(LinkAssociationState, data)
