"""Generated from Smithy shape ``com.amazonaws.securityir#MembershipAccountRelationshipType``."""

from typing import Literal, TypeAlias, cast

MembershipAccountRelationshipType: TypeAlias = Literal[
    "Organization",
    "Unrelated",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipAccountRelationshipType) -> str:
    return value


def deserialize_json(data: str) -> MembershipAccountRelationshipType:
    return cast(MembershipAccountRelationshipType, data)
