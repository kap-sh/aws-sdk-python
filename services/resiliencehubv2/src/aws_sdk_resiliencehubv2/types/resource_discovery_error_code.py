"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceDiscoveryErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_PERMISSIONS",
        "STACK_NOT_FOUND",
        "CLUSTER_NOT_FOUND",
        "STATE_FILE_NOT_FOUND",
        "ACCESS_DENIED",
        "UNSUPPORTED_CLUSTER",
        "INTERNAL_ERROR",
    )
)


def serialize_json(value: ResourceDiscoveryErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ResourceDiscoveryErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceDiscoveryErrorCode value: {data!r}"
        )
    return cast(ResourceDiscoveryErrorCode, data)
