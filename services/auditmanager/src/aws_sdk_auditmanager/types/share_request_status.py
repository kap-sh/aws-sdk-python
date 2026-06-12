"""Generated from Smithy shape ``com.amazonaws.auditmanager#ShareRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ShareRequestStatus: TypeAlias = Literal[
    "ACTIVE",
    "REPLICATING",
    "SHARED",
    "EXPIRING",
    "FAILED",
    "EXPIRED",
    "DECLINED",
    "REVOKED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "REPLICATING",
        "SHARED",
        "EXPIRING",
        "FAILED",
        "EXPIRED",
        "DECLINED",
        "REVOKED",
    )
)


def serialize_json(value: ShareRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> ShareRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareRequestStatus value: {data!r}")
    return cast(ShareRequestStatus, data)
