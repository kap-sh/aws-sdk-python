"""Generated from Smithy shape ``com.amazonaws.apigateway#CacheClusterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

"""<p>Returns the status of the CacheCluster.</p>"""
CacheClusterStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "AVAILABLE",
    "DELETE_IN_PROGRESS",
    "NOT_AVAILABLE",
    "FLUSH_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "AVAILABLE",
        "DELETE_IN_PROGRESS",
        "NOT_AVAILABLE",
        "FLUSH_IN_PROGRESS",
    )
)


def serialize_json(value: CacheClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> CacheClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CacheClusterStatus value: {data!r}")
    return cast(CacheClusterStatus, data)
