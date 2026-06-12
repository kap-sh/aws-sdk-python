"""Generated from Smithy shape ``com.amazonaws.batch#EFSAuthorizationConfigIAM``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

EFSAuthorizationConfigIAM: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: EFSAuthorizationConfigIAM) -> str:
    return value


def deserialize_json(data: str) -> EFSAuthorizationConfigIAM:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EFSAuthorizationConfigIAM value: {data!r}")
    return cast(EFSAuthorizationConfigIAM, data)
