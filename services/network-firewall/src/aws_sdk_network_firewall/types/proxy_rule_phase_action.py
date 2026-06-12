"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRulePhaseAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

ProxyRulePhaseAction: TypeAlias = Literal[
    "ALLOW",
    "DENY",
    "ALERT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
        "ALERT",
    )
)


def serialize_aws_json_1_0(value: ProxyRulePhaseAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProxyRulePhaseAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProxyRulePhaseAction value: {data!r}")
    return cast(ProxyRulePhaseAction, data)
