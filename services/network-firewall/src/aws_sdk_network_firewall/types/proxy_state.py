"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

ProxyState: TypeAlias = Literal[
    "ATTACHING",
    "ATTACHED",
    "DETACHING",
    "DETACHED",
    "ATTACH_FAILED",
    "DETACH_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTACHING",
        "ATTACHED",
        "DETACHING",
        "DETACHED",
        "ATTACH_FAILED",
        "DETACH_FAILED",
    )
)


def serialize_aws_json_1_0(value: ProxyState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProxyState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProxyState value: {data!r}")
    return cast(ProxyState, data)
