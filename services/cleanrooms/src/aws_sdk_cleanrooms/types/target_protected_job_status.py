"""Generated from Smithy shape ``com.amazonaws.cleanrooms#TargetProtectedJobStatus``."""

from typing import Literal, TypeAlias, cast

TargetProtectedJobStatus: TypeAlias = Literal["CANCELLED",]


# --- restJson1 ser/de ---
def serialize_json(value: TargetProtectedJobStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetProtectedJobStatus:
    return cast(TargetProtectedJobStatus, data)
