"""Generated from Smithy shape ``com.amazonaws.outposts#DecommissionRequestStatus``."""

from typing import Literal, TypeAlias, cast

DecommissionRequestStatus: TypeAlias = Literal[
    "SKIPPED",
    "BLOCKED",
    "REQUESTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DecommissionRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> DecommissionRequestStatus:
    return cast(DecommissionRequestStatus, data)
