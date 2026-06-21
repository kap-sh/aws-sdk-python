"""Generated from Smithy shape ``com.amazonaws.configservice#RuleEvaluationVisibility``."""

from typing import Literal, TypeAlias, cast

RuleEvaluationVisibility: TypeAlias = Literal[
    "EXTERNAL",
    "INTERNAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleEvaluationVisibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleEvaluationVisibility:
    return cast(RuleEvaluationVisibility, data)
