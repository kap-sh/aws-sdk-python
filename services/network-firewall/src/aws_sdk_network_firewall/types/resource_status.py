"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

ResourceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "ERROR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
        "ERROR",
    )
)


def serialize_aws_json_1_0(value: ResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceStatus value: {data!r}")
    return cast(ResourceStatus, data)
