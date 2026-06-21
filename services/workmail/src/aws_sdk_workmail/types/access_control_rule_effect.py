"""Generated from Smithy shape ``com.amazonaws.workmail#AccessControlRuleEffect``."""

from typing import Literal, TypeAlias, cast

AccessControlRuleEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlRuleEffect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessControlRuleEffect:
    return cast(AccessControlRuleEffect, data)
