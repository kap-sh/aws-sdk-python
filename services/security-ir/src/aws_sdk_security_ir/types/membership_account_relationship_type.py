"""Generated from Smithy shape ``com.amazonaws.securityir#MembershipAccountRelationshipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

MembershipAccountRelationshipType: TypeAlias = Literal[
    "Organization",
    "Unrelated",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Organization",
        "Unrelated",
    )
)


def serialize_json(value: MembershipAccountRelationshipType) -> str:
    return value


def deserialize_json(data: str) -> MembershipAccountRelationshipType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MembershipAccountRelationshipType value: {data!r}"
        )
    return cast(MembershipAccountRelationshipType, data)
