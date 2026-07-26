"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationMode``."""

from typing import Literal, TypeAlias, cast

EvaluationMode: TypeAlias = Literal[
    "DETECTIVE",
    "PROACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EvaluationMode:
    return cast(EvaluationMode, data)
