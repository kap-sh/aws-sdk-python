"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCopyJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.model_copy_job_summary

ModelCopyJobSummaries: TypeAlias = list[
    "capo_bedrock.types.model_copy_job_summary.ModelCopyJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelCopyJobSummaries) -> list:
    import capo_bedrock.types.model_copy_job_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.model_copy_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelCopyJobSummaries:
    import capo_bedrock.types.model_copy_job_summary

    out: ModelCopyJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.model_copy_job_summary.deserialize_json(item))
    return out
