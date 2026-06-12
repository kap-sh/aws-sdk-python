"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ConfigurationSyncState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

ConfigurationSyncState: TypeAlias = Literal[
    "PENDING",
    "IN_SYNC",
    "CAPACITY_CONSTRAINED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_SYNC",
        "CAPACITY_CONSTRAINED",
    )
)


def serialize_aws_json_1_0(value: ConfigurationSyncState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConfigurationSyncState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationSyncState value: {data!r}")
    return cast(ConfigurationSyncState, data)
