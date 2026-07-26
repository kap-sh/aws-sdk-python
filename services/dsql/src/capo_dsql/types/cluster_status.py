"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current status of a cluster.</p>"""
ClusterStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "IDLE",
    "INACTIVE",
    "UPDATING",
    "DELETING",
    "DELETED",
    "FAILED",
    "PENDING_SETUP",
    "PENDING_DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> ClusterStatus:
    return cast(ClusterStatus, data)
