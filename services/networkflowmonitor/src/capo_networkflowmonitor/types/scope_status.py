"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ScopeStatus``."""

from typing import Literal, TypeAlias, cast

ScopeStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "IN_PROGRESS",
    "FAILED",
    "DEACTIVATING",
    "DEACTIVATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeStatus) -> str:
    return value


def deserialize_json(data: str) -> ScopeStatus:
    return cast(ScopeStatus, data)
