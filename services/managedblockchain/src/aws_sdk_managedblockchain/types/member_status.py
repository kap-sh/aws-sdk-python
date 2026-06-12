"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

MemberStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "CREATE_FAILED",
    "UPDATING",
    "DELETING",
    "DELETED",
    "INACCESSIBLE_ENCRYPTION_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "CREATE_FAILED",
        "UPDATING",
        "DELETING",
        "DELETED",
        "INACCESSIBLE_ENCRYPTION_KEY",
    )
)


def serialize_json(value: MemberStatus) -> str:
    return value


def deserialize_json(data: str) -> MemberStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberStatus value: {data!r}")
    return cast(MemberStatus, data)
