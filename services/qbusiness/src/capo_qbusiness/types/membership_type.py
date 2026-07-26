"""Generated from Smithy shape ``com.amazonaws.qbusiness#MembershipType``."""

from typing import Literal, TypeAlias, cast

MembershipType: TypeAlias = Literal[
    "INDEX",
    "DATASOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipType) -> str:
    return value


def deserialize_json(data: str) -> MembershipType:
    return cast(MembershipType, data)
