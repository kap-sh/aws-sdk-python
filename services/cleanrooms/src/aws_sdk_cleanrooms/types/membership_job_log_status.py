"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipJobLogStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

MembershipJobLogStatus: TypeAlias = Literal[
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


def serialize_json(value: MembershipJobLogStatus) -> str:
    return value


def deserialize_json(data: str) -> MembershipJobLogStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MembershipJobLogStatus value: {data!r}")
    return cast(MembershipJobLogStatus, data)
