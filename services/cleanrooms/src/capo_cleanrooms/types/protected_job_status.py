"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobStatus``."""

from typing import Literal, TypeAlias, cast

ProtectedJobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "STARTED",
    "CANCELLED",
    "CANCELLING",
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ProtectedJobStatus:
    return cast(ProtectedJobStatus, data)
