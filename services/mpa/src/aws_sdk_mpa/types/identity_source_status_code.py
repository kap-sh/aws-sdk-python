"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

IdentitySourceStatusCode: TypeAlias = Literal[
    "ACCESS_DENIED",
    "DELETION_FAILED",
    "IDC_INSTANCE_NOT_FOUND",
    "IDC_INSTANCE_NOT_VALID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED",
        "DELETION_FAILED",
        "IDC_INSTANCE_NOT_FOUND",
        "IDC_INSTANCE_NOT_VALID",
    )
)


def serialize_json(value: IdentitySourceStatusCode) -> str:
    return value


def deserialize_json(data: str) -> IdentitySourceStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentitySourceStatusCode value: {data!r}")
    return cast(IdentitySourceStatusCode, data)
