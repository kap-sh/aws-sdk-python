"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallStatusValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

FirewallStatusValue: TypeAlias = Literal[
    "PROVISIONING",
    "DELETING",
    "READY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "DELETING",
        "READY",
    )
)


def serialize_aws_json_1_0(value: FirewallStatusValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FirewallStatusValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirewallStatusValue value: {data!r}")
    return cast(FirewallStatusValue, data)
