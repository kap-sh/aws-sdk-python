"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

DependencyDiscoveryStatus: TypeAlias = Literal[
    "ENABLED",
    "INITIALIZING",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "INITIALIZING",
        "DISABLED",
    )
)


def serialize_json(value: DependencyDiscoveryStatus) -> str:
    return value


def deserialize_json(data: str) -> DependencyDiscoveryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DependencyDiscoveryStatus value: {data!r}")
    return cast(DependencyDiscoveryStatus, data)
