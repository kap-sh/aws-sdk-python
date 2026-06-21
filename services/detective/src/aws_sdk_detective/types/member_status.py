"""Generated from Smithy shape ``com.amazonaws.detective#MemberStatus``."""

from typing import Literal, TypeAlias, cast

MemberStatus: TypeAlias = Literal[
    "INVITED",
    "VERIFICATION_IN_PROGRESS",
    "VERIFICATION_FAILED",
    "ENABLED",
    "ACCEPTED_BUT_DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberStatus) -> str:
    return value


def deserialize_json(data: str) -> MemberStatus:
    return cast(MemberStatus, data)
