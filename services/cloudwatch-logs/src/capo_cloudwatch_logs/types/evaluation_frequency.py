"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EvaluationFrequency``."""

from typing import Literal, TypeAlias, cast

EvaluationFrequency: TypeAlias = Literal[
    "ONE_MIN",
    "FIVE_MIN",
    "TEN_MIN",
    "FIFTEEN_MIN",
    "THIRTY_MIN",
    "ONE_HOUR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EvaluationFrequency:
    return cast(EvaluationFrequency, data)
