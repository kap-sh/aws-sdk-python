"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#TargetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_notifications.errors import DeserializationError

TargetStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "UNREACHABLE",
    "INACTIVE",
    "DEACTIVATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "UNREACHABLE",
        "INACTIVE",
        "DEACTIVATED",
    )
)


def serialize_json(value: TargetStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetStatus value: {data!r}")
    return cast(TargetStatus, data)
