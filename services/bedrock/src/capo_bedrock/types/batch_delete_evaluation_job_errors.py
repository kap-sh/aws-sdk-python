"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.batch_delete_evaluation_job_error

BatchDeleteEvaluationJobErrors: TypeAlias = list[
    "capo_bedrock.types.batch_delete_evaluation_job_error.BatchDeleteEvaluationJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobErrors) -> list:
    import capo_bedrock.types.batch_delete_evaluation_job_error

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.batch_delete_evaluation_job_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchDeleteEvaluationJobErrors:
    import capo_bedrock.types.batch_delete_evaluation_job_error

    out: BatchDeleteEvaluationJobErrors = []
    for item in data:
        out.append(
            capo_bedrock.types.batch_delete_evaluation_job_error.deserialize_json(item)
        )
    return out
