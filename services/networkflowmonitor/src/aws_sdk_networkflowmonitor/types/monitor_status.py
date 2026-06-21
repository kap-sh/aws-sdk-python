"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorStatus``."""

from typing import Literal, TypeAlias, cast

MonitorStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "INACTIVE",
    "ERROR",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorStatus) -> str:
    return value


def deserialize_json(data: str) -> MonitorStatus:
    return cast(MonitorStatus, data)
