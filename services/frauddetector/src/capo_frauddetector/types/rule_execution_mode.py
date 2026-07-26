"""Generated from Smithy shape ``com.amazonaws.frauddetector#RuleExecutionMode``."""

from typing import Literal, TypeAlias, cast

RuleExecutionMode: TypeAlias = Literal[
    "ALL_MATCHED",
    "FIRST_MATCHED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleExecutionMode:
    return cast(RuleExecutionMode, data)
