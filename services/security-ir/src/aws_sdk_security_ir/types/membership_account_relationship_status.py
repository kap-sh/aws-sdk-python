"""Generated from Smithy shape ``com.amazonaws.securityir#MembershipAccountRelationshipStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

MembershipAccountRelationshipStatus: TypeAlias = Literal[
    "Associated",
    "Disassociated",
    "Unassociated",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Associated",
        "Disassociated",
        "Unassociated",
    )
)


def serialize_json(value: MembershipAccountRelationshipStatus) -> str:
    return value


def deserialize_json(data: str) -> MembershipAccountRelationshipStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MembershipAccountRelationshipStatus value: {data!r}"
        )
    return cast(MembershipAccountRelationshipStatus, data)
