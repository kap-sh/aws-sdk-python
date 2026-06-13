"""Generated from Smithy shape ``com.amazonaws.ssmsap#HostRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

HostRole: TypeAlias = Literal[
    "LEADER",
    "WORKER",
    "STANDBY",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEADER",
        "WORKER",
        "STANDBY",
        "UNKNOWN",
    )
)


def serialize_json(value: HostRole) -> str:
    return value


def deserialize_json(data: str) -> HostRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HostRole value: {data!r}")
    return cast(HostRole, data)
