"""Generated from Smithy shape ``com.amazonaws.connecthealth#ProviderRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

ProviderRole: TypeAlias = Literal["CLINICIAN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CLINICIAN",))


def serialize_json(value: ProviderRole) -> str:
    return value


def deserialize_json(data: str) -> ProviderRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProviderRole value: {data!r}")
    return cast(ProviderRole, data)
