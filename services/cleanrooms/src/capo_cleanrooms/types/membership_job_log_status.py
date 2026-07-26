"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipJobLogStatus``."""

from typing import Literal, TypeAlias, cast

MembershipJobLogStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipJobLogStatus) -> str:
    return value


def deserialize_json(data: str) -> MembershipJobLogStatus:
    return cast(MembershipJobLogStatus, data)
