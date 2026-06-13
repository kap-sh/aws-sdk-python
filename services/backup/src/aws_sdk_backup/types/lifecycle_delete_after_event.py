"""Generated from Smithy shape ``com.amazonaws.backup#LifecycleDeleteAfterEvent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

LifecycleDeleteAfterEvent: TypeAlias = Literal["DELETE_AFTER_COPY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DELETE_AFTER_COPY",))


def serialize_json(value: LifecycleDeleteAfterEvent) -> str:
    return value


def deserialize_json(data: str) -> LifecycleDeleteAfterEvent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifecycleDeleteAfterEvent value: {data!r}")
    return cast(LifecycleDeleteAfterEvent, data)
