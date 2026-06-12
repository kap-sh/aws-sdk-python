"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_item

BatchDeleteEvaluationJobItems: TypeAlias = list[
    "aws_sdk_bedrock.types.batch_delete_evaluation_job_item.BatchDeleteEvaluationJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobItems) -> list:
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.batch_delete_evaluation_job_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchDeleteEvaluationJobItems:
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_item

    out: BatchDeleteEvaluationJobItems = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.batch_delete_evaluation_job_item.deserialize_json(
                item
            )
        )
    return out
