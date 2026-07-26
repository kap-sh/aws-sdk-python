"""Generated from Smithy shape ``com.amazonaws.deadline#SessionLifecycleTargetStatus``."""

from typing import Literal, TypeAlias, cast

SessionLifecycleTargetStatus: TypeAlias = Literal["ENDED",]


# --- restJson1 ser/de ---
def serialize_json(value: SessionLifecycleTargetStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionLifecycleTargetStatus:
    return cast(SessionLifecycleTargetStatus, data)
