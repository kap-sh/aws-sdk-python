"""Generated from Smithy shape ``com.amazonaws.deadline#MembershipLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

MembershipLevel: TypeAlias = Literal[
    "VIEWER",
    "CONTRIBUTOR",
    "OWNER",
    "MANAGER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VIEWER",
        "CONTRIBUTOR",
        "OWNER",
        "MANAGER",
    )
)


def serialize_json(value: MembershipLevel) -> str:
    return value


def deserialize_json(data: str) -> MembershipLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MembershipLevel value: {data!r}")
    return cast(MembershipLevel, data)
