"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobStatus``."""

from typing import Literal, TypeAlias, cast

ServiceJobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "PENDING",
    "RUNNABLE",
    "SCHEDULED",
    "STARTING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ServiceJobStatus:
    return cast(ServiceJobStatus, data)
