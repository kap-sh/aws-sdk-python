"""Generated from Smithy shape ``com.amazonaws.mpa#IdentityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

IdentityStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
    "INVALID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACCEPTED",
        "REJECTED",
        "INVALID",
    )
)


def serialize_json(value: IdentityStatus) -> str:
    return value


def deserialize_json(data: str) -> IdentityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityStatus value: {data!r}")
    return cast(IdentityStatus, data)
