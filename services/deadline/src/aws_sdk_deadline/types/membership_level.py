"""Generated from Smithy shape ``com.amazonaws.deadline#MembershipLevel``."""

from typing import Literal, TypeAlias, cast

MembershipLevel: TypeAlias = Literal[
    "VIEWER",
    "CONTRIBUTOR",
    "OWNER",
    "MANAGER",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipLevel) -> str:
    return value


def deserialize_json(data: str) -> MembershipLevel:
    return cast(MembershipLevel, data)
