"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RuleState``."""

from typing import Literal, TypeAlias, cast

RuleState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleState:
    return cast(RuleState, data)
