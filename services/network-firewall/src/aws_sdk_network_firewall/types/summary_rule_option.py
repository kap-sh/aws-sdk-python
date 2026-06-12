"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SummaryRuleOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

SummaryRuleOption: TypeAlias = Literal[
    "SID",
    "MSG",
    "METADATA",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SID",
        "MSG",
        "METADATA",
    )
)


def serialize_aws_json_1_0(value: SummaryRuleOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SummaryRuleOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SummaryRuleOption value: {data!r}")
    return cast(SummaryRuleOption, data)
