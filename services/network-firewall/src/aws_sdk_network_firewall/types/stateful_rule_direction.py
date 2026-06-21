"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleDirection``."""

from typing import Literal, TypeAlias, cast

StatefulRuleDirection: TypeAlias = Literal[
    "FORWARD",
    "ANY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRuleDirection) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatefulRuleDirection:
    return cast(StatefulRuleDirection, data)
