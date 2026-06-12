"""Generated from Smithy shape ``com.amazonaws.auditmanager#DelegationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

DelegationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "UNDER_REVIEW",
    "COMPLETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "UNDER_REVIEW",
        "COMPLETE",
    )
)


def serialize_json(value: DelegationStatus) -> str:
    return value


def deserialize_json(data: str) -> DelegationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DelegationStatus value: {data!r}")
    return cast(DelegationStatus, data)
