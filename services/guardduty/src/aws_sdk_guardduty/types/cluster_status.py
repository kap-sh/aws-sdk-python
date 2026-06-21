"""Generated from Smithy shape ``com.amazonaws.guardduty#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

ClusterStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "UPDATING",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> ClusterStatus:
    return cast(ClusterStatus, data)
