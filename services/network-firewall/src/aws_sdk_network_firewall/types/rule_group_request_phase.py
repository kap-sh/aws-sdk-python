"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroupRequestPhase``."""

from typing import Literal, TypeAlias, cast

RuleGroupRequestPhase: TypeAlias = Literal[
    "PRE_DNS",
    "PRE_REQ",
    "POST_RES",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleGroupRequestPhase) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleGroupRequestPhase:
    return cast(RuleGroupRequestPhase, data)
