"""Generated from Smithy shape ``com.amazonaws.deadline#SessionLifecycleTargetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

SessionLifecycleTargetStatus: TypeAlias = Literal["ENDED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ENDED",))


def serialize_json(value: SessionLifecycleTargetStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionLifecycleTargetStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SessionLifecycleTargetStatus value: {data!r}"
        )
    return cast(SessionLifecycleTargetStatus, data)
