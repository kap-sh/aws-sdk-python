"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipQueryLogStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

MembershipQueryLogStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: MembershipQueryLogStatus) -> str:
    return value


def deserialize_json(data: str) -> MembershipQueryLogStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MembershipQueryLogStatus value: {data!r}")
    return cast(MembershipQueryLogStatus, data)
