"""Generated from Smithy shape ``com.amazonaws.wafv2#ActionValue``."""

from typing import Literal, TypeAlias, cast

ActionValue: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
    "COUNT",
    "CAPTCHA",
    "CHALLENGE",
    "EXCLUDED_AS_COUNT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionValue:
    return cast(ActionValue, data)
