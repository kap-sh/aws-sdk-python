"""Generated from Smithy shape ``com.amazonaws.backup#LifecycleDeleteAfterEvent``."""

from typing import Literal, TypeAlias, cast

LifecycleDeleteAfterEvent: TypeAlias = Literal["DELETE_AFTER_COPY",]


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleDeleteAfterEvent) -> str:
    return value


def deserialize_json(data: str) -> LifecycleDeleteAfterEvent:
    return cast(LifecycleDeleteAfterEvent, data)
