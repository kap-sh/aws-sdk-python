"""Generated from Smithy shape ``com.amazonaws.signer#SigningStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_signer.errors import DeserializationError

SigningStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Succeeded",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Failed",
        "Succeeded",
    )
)


def serialize_json(value: SigningStatus) -> str:
    return value


def deserialize_json(data: str) -> SigningStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SigningStatus value: {data!r}")
    return cast(SigningStatus, data)
