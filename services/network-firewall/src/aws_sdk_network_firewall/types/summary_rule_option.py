"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SummaryRuleOption``."""

from typing import Literal, TypeAlias, cast

SummaryRuleOption: TypeAlias = Literal[
    "SID",
    "MSG",
    "METADATA",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryRuleOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SummaryRuleOption:
    return cast(SummaryRuleOption, data)
