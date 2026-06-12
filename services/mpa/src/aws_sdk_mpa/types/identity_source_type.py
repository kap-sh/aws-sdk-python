"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

IdentitySourceType: TypeAlias = Literal["IAM_IDENTITY_CENTER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IAM_IDENTITY_CENTER",))


def serialize_json(value: IdentitySourceType) -> str:
    return value


def deserialize_json(data: str) -> IdentitySourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentitySourceType value: {data!r}")
    return cast(IdentitySourceType, data)
