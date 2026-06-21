"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceDiscoveryErrorCode``."""

from typing import Literal, TypeAlias, cast

ResourceDiscoveryErrorCode: TypeAlias = Literal[
    "INVALID_PERMISSIONS",
    "STACK_NOT_FOUND",
    "CLUSTER_NOT_FOUND",
    "STATE_FILE_NOT_FOUND",
    "ACCESS_DENIED",
    "UNSUPPORTED_CLUSTER",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDiscoveryErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ResourceDiscoveryErrorCode:
    return cast(ResourceDiscoveryErrorCode, data)
