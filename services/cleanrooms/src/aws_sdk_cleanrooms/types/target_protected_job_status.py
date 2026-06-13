"""Generated from Smithy shape ``com.amazonaws.cleanrooms#TargetProtectedJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

TargetProtectedJobStatus: TypeAlias = Literal["CANCELLED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CANCELLED",))


def serialize_json(value: TargetProtectedJobStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetProtectedJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetProtectedJobStatus value: {data!r}")
    return cast(TargetProtectedJobStatus, data)
