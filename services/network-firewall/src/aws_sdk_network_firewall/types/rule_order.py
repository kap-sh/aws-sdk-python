"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

RuleOrder: TypeAlias = Literal[
    "DEFAULT_ACTION_ORDER",
    "STRICT_ORDER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT_ACTION_ORDER",
        "STRICT_ORDER",
    )
)


def serialize_aws_json_1_0(value: RuleOrder) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleOrder value: {data!r}")
    return cast(RuleOrder, data)
