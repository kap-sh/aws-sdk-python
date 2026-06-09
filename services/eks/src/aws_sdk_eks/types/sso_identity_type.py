"""Generated from Smithy shape ``com.amazonaws.eks#SsoIdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

SsoIdentityType: TypeAlias = Literal[
    "SSO_USER",
    "SSO_GROUP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSO_USER",
        "SSO_GROUP",
    )
)


def serialize_json(value: SsoIdentityType) -> str:
    return value


def deserialize_json(data: str) -> SsoIdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SsoIdentityType value: {data!r}")
    return cast(SsoIdentityType, data)
