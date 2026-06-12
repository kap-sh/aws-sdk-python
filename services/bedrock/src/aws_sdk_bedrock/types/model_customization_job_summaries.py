"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCustomizationJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_customization_job_summary

ModelCustomizationJobSummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.model_customization_job_summary.ModelCustomizationJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelCustomizationJobSummaries) -> list:
    import aws_sdk_bedrock.types.model_customization_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.model_customization_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ModelCustomizationJobSummaries:
    import aws_sdk_bedrock.types.model_customization_job_summary

    out: ModelCustomizationJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.model_customization_job_summary.deserialize_json(item)
        )
    return out
