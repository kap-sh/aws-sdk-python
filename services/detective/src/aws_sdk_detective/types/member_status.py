"""Generated from Smithy shape ``com.amazonaws.detective#MemberStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

MemberStatus: TypeAlias = Literal[
    "INVITED",
    "VERIFICATION_IN_PROGRESS",
    "VERIFICATION_FAILED",
    "ENABLED",
    "ACCEPTED_BUT_DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVITED",
        "VERIFICATION_IN_PROGRESS",
        "VERIFICATION_FAILED",
        "ENABLED",
        "ACCEPTED_BUT_DISABLED",
    )
)


def serialize_json(value: MemberStatus) -> str:
    return value


def deserialize_json(data: str) -> MemberStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberStatus value: {data!r}")
    return cast(MemberStatus, data)
