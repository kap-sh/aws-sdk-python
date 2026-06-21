"""Generated from Smithy shape ``com.amazonaws.glue#StatisticEvaluationLevel``."""

from typing import Literal, TypeAlias, cast

StatisticEvaluationLevel: TypeAlias = Literal[
    "Dataset",
    "Column",
    "Multicolumn",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticEvaluationLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatisticEvaluationLevel:
    return cast(StatisticEvaluationLevel, data)
