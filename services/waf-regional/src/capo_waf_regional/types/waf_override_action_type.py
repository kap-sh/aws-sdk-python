"""Generated from Smithy shape ``com.amazonaws.wafregional#WafOverrideActionType``."""

from typing import Literal, TypeAlias, cast

WafOverrideActionType: TypeAlias = Literal[
    "NONE",
    "COUNT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafOverrideActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WafOverrideActionType:
    return cast(WafOverrideActionType, data)
