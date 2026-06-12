"""Generated from Smithy shape ``com.amazonaws.guardduty#AutoEnableMembers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

AutoEnableMembers: TypeAlias = Literal[
    "NEW",
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "ALL",
        "NONE",
    )
)


def serialize_json(value: AutoEnableMembers) -> str:
    return value


def deserialize_json(data: str) -> AutoEnableMembers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoEnableMembers value: {data!r}")
    return cast(AutoEnableMembers, data)
