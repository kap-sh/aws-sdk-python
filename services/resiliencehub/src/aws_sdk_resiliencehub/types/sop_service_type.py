"""Generated from Smithy shape ``com.amazonaws.resiliencehub#SopServiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

SopServiceType: TypeAlias = Literal["SSM",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SSM",))


def serialize_json(value: SopServiceType) -> str:
    return value


def deserialize_json(data: str) -> SopServiceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SopServiceType value: {data!r}")
    return cast(SopServiceType, data)
