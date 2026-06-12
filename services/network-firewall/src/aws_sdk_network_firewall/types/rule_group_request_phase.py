"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroupRequestPhase``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

RuleGroupRequestPhase: TypeAlias = Literal[
    "PRE_DNS",
    "PRE_REQ",
    "POST_RES",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE_DNS",
        "PRE_REQ",
        "POST_RES",
    )
)


def serialize_aws_json_1_0(value: RuleGroupRequestPhase) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleGroupRequestPhase:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleGroupRequestPhase value: {data!r}")
    return cast(RuleGroupRequestPhase, data)
