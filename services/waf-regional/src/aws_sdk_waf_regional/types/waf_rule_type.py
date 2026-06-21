"""Generated from Smithy shape ``com.amazonaws.wafregional#WafRuleType``."""

from typing import Literal, TypeAlias, cast

WafRuleType: TypeAlias = Literal[
    "REGULAR",
    "RATE_BASED",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafRuleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WafRuleType:
    return cast(WafRuleType, data)
