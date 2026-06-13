"""Generated from Smithy shape ``com.amazonaws.securityagent#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Error code for pentest job failure.</p>"""
ErrorCode: TypeAlias = Literal[
    "CLIENT_ERROR",
    "INTERNAL_ERROR",
    "STOPPED_BY_USER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLIENT_ERROR",
        "INTERNAL_ERROR",
        "STOPPED_BY_USER",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
