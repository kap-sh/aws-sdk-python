"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_summary

EvaluationSummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.evaluation_summary.EvaluationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSummaries) -> list:
    import aws_sdk_bedrock.types.evaluation_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.evaluation_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationSummaries:
    import aws_sdk_bedrock.types.evaluation_summary

    out: EvaluationSummaries = []
    for item in data:
        out.append(aws_sdk_bedrock.types.evaluation_summary.deserialize_json(item))
    return out
