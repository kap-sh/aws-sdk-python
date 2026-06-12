"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceManagedType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

ResourceManagedType: TypeAlias = Literal[
    "AWS_MANAGED_THREAT_SIGNATURES",
    "AWS_MANAGED_DOMAIN_LISTS",
    "ACTIVE_THREAT_DEFENSE",
    "PARTNER_MANAGED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_MANAGED_THREAT_SIGNATURES",
        "AWS_MANAGED_DOMAIN_LISTS",
        "ACTIVE_THREAT_DEFENSE",
        "PARTNER_MANAGED",
    )
)


def serialize_aws_json_1_0(value: ResourceManagedType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceManagedType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceManagedType value: {data!r}")
    return cast(ResourceManagedType, data)
