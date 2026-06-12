"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ControlStatus: TypeAlias = Literal[
    "UNDER_REVIEW",
    "REVIEWED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNDER_REVIEW",
        "REVIEWED",
        "INACTIVE",
    )
)


def serialize_json(value: ControlStatus) -> str:
    return value


def deserialize_json(data: str) -> ControlStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlStatus value: {data!r}")
    return cast(ControlStatus, data)
