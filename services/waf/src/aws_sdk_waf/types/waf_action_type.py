"""Generated from Smithy shape ``com.amazonaws.waf#WafActionType``."""

from typing import Literal, TypeAlias, cast

WafActionType: TypeAlias = Literal[
    "BLOCK",
    "ALLOW",
    "COUNT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WafActionType:
    return cast(WafActionType, data)
