"""Generated from Smithy shape ``com.amazonaws.securityir#ClosureCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

ClosureCode: TypeAlias = Literal[
    "Investigation Completed",
    "Not Resolved",
    "False Positive",
    "Duplicate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Investigation Completed",
        "Not Resolved",
        "False Positive",
        "Duplicate",
    )
)


def serialize_json(value: ClosureCode) -> str:
    return value


def deserialize_json(data: str) -> ClosureCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClosureCode value: {data!r}")
    return cast(ClosureCode, data)
