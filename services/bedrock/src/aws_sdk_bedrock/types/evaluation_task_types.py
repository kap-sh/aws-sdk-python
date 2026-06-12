"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationTaskTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_task_type

EvaluationTaskTypes: TypeAlias = list[
    "aws_sdk_bedrock.types.evaluation_task_type.EvaluationTaskType"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationTaskTypes) -> list:
    import aws_sdk_bedrock.types.evaluation_task_type

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.evaluation_task_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationTaskTypes:
    import aws_sdk_bedrock.types.evaluation_task_type

    out: EvaluationTaskTypes = []
    for item in data:
        out.append(aws_sdk_bedrock.types.evaluation_task_type.deserialize_json(item))
    return out
