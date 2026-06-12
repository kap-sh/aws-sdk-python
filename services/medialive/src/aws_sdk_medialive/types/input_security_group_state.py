"""Generated from Smithy shape ``com.amazonaws.medialive#InputSecurityGroupState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Placeholder documentation for InputSecurityGroupState"""
InputSecurityGroupState: TypeAlias = Literal[
    "IDLE",
    "IN_USE",
    "UPDATING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDLE",
        "IN_USE",
        "UPDATING",
        "DELETED",
    )
)


def serialize_json(value: InputSecurityGroupState) -> str:
    return value


def deserialize_json(data: str) -> InputSecurityGroupState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputSecurityGroupState value: {data!r}")
    return cast(InputSecurityGroupState, data)
