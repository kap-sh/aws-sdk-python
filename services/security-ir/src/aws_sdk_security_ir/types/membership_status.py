"""Generated from Smithy shape ``com.amazonaws.securityir#MembershipStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

MembershipStatus: TypeAlias = Literal[
    "Active",
    "Cancelled",
    "Terminated",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Cancelled",
        "Terminated",
    )
)


def serialize_json(value: MembershipStatus) -> str:
    return value


def deserialize_json(data: str) -> MembershipStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MembershipStatus value: {data!r}")
    return cast(MembershipStatus, data)
