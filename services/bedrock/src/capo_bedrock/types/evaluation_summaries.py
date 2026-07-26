"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_summary

EvaluationSummaries: TypeAlias = list[
    "capo_bedrock.types.evaluation_summary.EvaluationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSummaries) -> list:
    import capo_bedrock.types.evaluation_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.evaluation_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationSummaries:
    import capo_bedrock.types.evaluation_summary

    out: EvaluationSummaries = []
    for item in data:
        out.append(capo_bedrock.types.evaluation_summary.deserialize_json(item))
    return out
