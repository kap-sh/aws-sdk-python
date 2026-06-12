"""Generated from Smithy shape ``com.amazonaws.auditmanager#ShareRequestType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ShareRequestType: TypeAlias = Literal[
    "SENT",
    "RECEIVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SENT",
        "RECEIVED",
    )
)


def serialize_json(value: ShareRequestType) -> str:
    return value


def deserialize_json(data: str) -> ShareRequestType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareRequestType value: {data!r}")
    return cast(ShareRequestType, data)
