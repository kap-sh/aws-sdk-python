"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PerObjectSyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

PerObjectSyncStatus: TypeAlias = Literal[
    "PENDING",
    "IN_SYNC",
    "CAPACITY_CONSTRAINED",
    "NOT_SUBSCRIBED",
    "DEPRECATED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_SYNC",
        "CAPACITY_CONSTRAINED",
        "NOT_SUBSCRIBED",
        "DEPRECATED",
    )
)


def serialize_aws_json_1_0(value: PerObjectSyncStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PerObjectSyncStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PerObjectSyncStatus value: {data!r}")
    return cast(PerObjectSyncStatus, data)
