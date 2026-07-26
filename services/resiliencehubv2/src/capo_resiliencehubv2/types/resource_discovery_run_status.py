"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceDiscoveryRunStatus``."""

from typing import Literal, TypeAlias, cast

ResourceDiscoveryRunStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "COMPLETED_WITH_FAILURES",
    "NOT_STARTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDiscoveryRunStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceDiscoveryRunStatus:
    return cast(ResourceDiscoveryRunStatus, data)
