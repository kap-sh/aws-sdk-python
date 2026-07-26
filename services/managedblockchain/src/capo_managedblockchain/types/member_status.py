"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: MemberStatus) -> str:
    return value


def deserialize_json(data: str) -> MemberStatus:
    return cast(MemberStatus, data)
