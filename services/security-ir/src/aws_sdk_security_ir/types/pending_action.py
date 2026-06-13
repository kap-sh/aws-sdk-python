"""Generated from Smithy shape ``com.amazonaws.securityir#PendingAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

PendingAction: TypeAlias = Literal[
    "Customer",
    "None",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Customer",
        "None",
    )
)


def serialize_json(value: PendingAction) -> str:
    return value


def deserialize_json(data: str) -> PendingAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PendingAction value: {data!r}")
    return cast(PendingAction, data)
