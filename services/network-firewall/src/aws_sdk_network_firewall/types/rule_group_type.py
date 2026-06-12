"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

RuleGroupType: TypeAlias = Literal[
    "STATELESS",
    "STATEFUL",
    "STATEFUL_DOMAIN",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATELESS",
        "STATEFUL",
        "STATEFUL_DOMAIN",
    )
)


def serialize_aws_json_1_0(value: RuleGroupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleGroupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleGroupType value: {data!r}")
    return cast(RuleGroupType, data)
