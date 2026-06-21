"""Generated from Smithy shape ``com.amazonaws.securityir#MembershipAccountRelationshipStatus``."""

from typing import Literal, TypeAlias, cast

MembershipAccountRelationshipStatus: TypeAlias = Literal[
    "Associated",
    "Disassociated",
    "Unassociated",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipAccountRelationshipStatus) -> str:
    return value


def deserialize_json(data: str) -> MembershipAccountRelationshipStatus:
    return cast(MembershipAccountRelationshipStatus, data)
