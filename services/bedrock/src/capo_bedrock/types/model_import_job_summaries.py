"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelImportJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.model_import_job_summary

ModelImportJobSummaries: TypeAlias = list[
    "capo_bedrock.types.model_import_job_summary.ModelImportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelImportJobSummaries) -> list:
    import capo_bedrock.types.model_import_job_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.model_import_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelImportJobSummaries:
    import capo_bedrock.types.model_import_job_summary

    out: ModelImportJobSummaries = []
    for item in data:
        out.append(capo_bedrock.types.model_import_job_summary.deserialize_json(item))
    return out
