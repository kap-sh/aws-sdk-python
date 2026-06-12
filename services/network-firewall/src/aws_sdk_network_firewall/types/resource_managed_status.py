"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceManagedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

ResourceManagedStatus: TypeAlias = Literal[
    "MANAGED",
    "ACCOUNT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANAGED",
        "ACCOUNT",
    )
)


def serialize_aws_json_1_0(value: ResourceManagedStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceManagedStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceManagedStatus value: {data!r}")
    return cast(ResourceManagedStatus, data)
