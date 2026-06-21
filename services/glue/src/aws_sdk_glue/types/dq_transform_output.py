"""Generated from Smithy shape ``com.amazonaws.glue#DQTransformOutput``."""

from typing import Literal, TypeAlias, cast

DQTransformOutput: TypeAlias = Literal[
    "PrimaryInput",
    "EvaluationResults",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DQTransformOutput) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DQTransformOutput:
    return cast(DQTransformOutput, data)
