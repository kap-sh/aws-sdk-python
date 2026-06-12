"""Generated from Smithy shape ``com.amazonaws.auditmanager#ShareRequestAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ShareRequestAction: TypeAlias = Literal[
    "ACCEPT",
    "DECLINE",
    "REVOKE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCEPT",
        "DECLINE",
        "REVOKE",
    )
)


def serialize_json(value: ShareRequestAction) -> str:
    return value


def deserialize_json(data: str) -> ShareRequestAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareRequestAction value: {data!r}")
    return cast(ShareRequestAction, data)
