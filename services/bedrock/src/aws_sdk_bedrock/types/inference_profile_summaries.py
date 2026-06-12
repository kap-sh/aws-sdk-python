"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_profile_summary

InferenceProfileSummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.inference_profile_summary.InferenceProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProfileSummaries) -> list:
    import aws_sdk_bedrock.types.inference_profile_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.inference_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InferenceProfileSummaries:
    import aws_sdk_bedrock.types.inference_profile_summary

    out: InferenceProfileSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.inference_profile_summary.deserialize_json(item)
        )
    return out
