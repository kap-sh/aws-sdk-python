"""Generated from Smithy shape ``com.amazonaws.securityir#MembershipStatus``."""

from typing import Literal, TypeAlias, cast

MembershipStatus: TypeAlias = Literal[
    "Active",
    "Cancelled",
    "Terminated",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipStatus) -> str:
    return value


def deserialize_json(data: str) -> MembershipStatus:
    return cast(MembershipStatus, data)
