"""Generated from Smithy shape ``com.amazonaws.sagemaker#ConditionOutcome``."""

from typing import Literal, TypeAlias, cast

ConditionOutcome: TypeAlias = Literal[
    "True",
    "False",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionOutcome) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConditionOutcome:
    return cast(ConditionOutcome, data)
