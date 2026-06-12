"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

IdentitySourceStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "ERROR",
    )
)


def serialize_json(value: IdentitySourceStatus) -> str:
    return value


def deserialize_json(data: str) -> IdentitySourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentitySourceStatus value: {data!r}")
    return cast(IdentitySourceStatus, data)
