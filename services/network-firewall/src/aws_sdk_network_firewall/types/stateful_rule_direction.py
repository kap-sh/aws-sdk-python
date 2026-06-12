"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

StatefulRuleDirection: TypeAlias = Literal[
    "FORWARD",
    "ANY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FORWARD",
        "ANY",
    )
)


def serialize_aws_json_1_0(value: StatefulRuleDirection) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatefulRuleDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatefulRuleDirection value: {data!r}")
    return cast(StatefulRuleDirection, data)
