"""Generated from Smithy shape ``com.amazonaws.forecast#EvaluationType``."""

from typing import Literal, TypeAlias, cast

EvaluationType: TypeAlias = Literal[
    "SUMMARY",
    "COMPUTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EvaluationType:
    return cast(EvaluationType, data)
