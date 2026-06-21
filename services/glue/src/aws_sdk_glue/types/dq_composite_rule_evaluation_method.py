"""Generated from Smithy shape ``com.amazonaws.glue#DQCompositeRuleEvaluationMethod``."""

from typing import Literal, TypeAlias, cast

DQCompositeRuleEvaluationMethod: TypeAlias = Literal[
    "COLUMN",
    "ROW",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DQCompositeRuleEvaluationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DQCompositeRuleEvaluationMethod:
    return cast(DQCompositeRuleEvaluationMethod, data)
