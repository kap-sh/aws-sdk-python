"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipQueryLogStatus``."""

from typing import Literal, TypeAlias, cast

MembershipQueryLogStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipQueryLogStatus) -> str:
    return value


def deserialize_json(data: str) -> MembershipQueryLogStatus:
    return cast(MembershipQueryLogStatus, data)
