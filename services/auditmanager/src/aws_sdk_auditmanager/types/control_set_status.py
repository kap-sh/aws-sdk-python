"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ControlSetStatus: TypeAlias = Literal[
    "ACTIVE",
    "UNDER_REVIEW",
    "REVIEWED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "UNDER_REVIEW",
        "REVIEWED",
    )
)


def serialize_json(value: ControlSetStatus) -> str:
    return value


def deserialize_json(data: str) -> ControlSetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlSetStatus value: {data!r}")
    return cast(ControlSetStatus, data)
