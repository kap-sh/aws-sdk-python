"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyModifyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

ProxyModifyState: TypeAlias = Literal[
    "MODIFYING",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MODIFYING",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: ProxyModifyState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProxyModifyState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProxyModifyState value: {data!r}")
    return cast(ProxyModifyState, data)
