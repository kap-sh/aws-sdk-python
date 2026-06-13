"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkflowmonitor.errors import DeserializationError

TargetType: TypeAlias = Literal["ACCOUNT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACCOUNT",))


def serialize_json(value: TargetType) -> str:
    return value


def deserialize_json(data: str) -> TargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetType value: {data!r}")
    return cast(TargetType, data)
