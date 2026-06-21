"""Generated from Smithy shape ``com.amazonaws.apigateway#CacheClusterStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Returns the status of the CacheCluster.</p>"""
CacheClusterStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "AVAILABLE",
    "DELETE_IN_PROGRESS",
    "NOT_AVAILABLE",
    "FLUSH_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CacheClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> CacheClusterStatus:
    return cast(CacheClusterStatus, data)
