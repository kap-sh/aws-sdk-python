"""Generated from Smithy shape ``com.amazonaws.signer#SigningProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_signer.errors import DeserializationError

SigningProfileStatus: TypeAlias = Literal[
    "Active",
    "Canceled",
    "Revoked",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Canceled",
        "Revoked",
    )
)


def serialize_json(value: SigningProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> SigningProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SigningProfileStatus value: {data!r}")
    return cast(SigningProfileStatus, data)
