"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_invocation_job_summary

ModelInvocationJobSummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.model_invocation_job_summary.ModelInvocationJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobSummaries) -> list:
    import aws_sdk_bedrock.types.model_invocation_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.model_invocation_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ModelInvocationJobSummaries:
    import aws_sdk_bedrock.types.model_invocation_job_summary

    out: ModelInvocationJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.model_invocation_job_summary.deserialize_json(item)
        )
    return out
