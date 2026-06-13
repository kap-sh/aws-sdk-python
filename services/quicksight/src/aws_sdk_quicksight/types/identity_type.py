"""Generated from Smithy shape ``com.amazonaws.quicksight#IdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

IdentityType: TypeAlias = Literal[
    "IAM",
    "QUICKSIGHT",
    "IAM_IDENTITY_CENTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "QUICKSIGHT",
        "IAM_IDENTITY_CENTER",
    )
)


def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityType value: {data!r}")
    return cast(IdentityType, data)
