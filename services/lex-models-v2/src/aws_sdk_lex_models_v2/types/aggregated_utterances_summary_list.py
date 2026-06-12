"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.aggregated_utterances_summary

AggregatedUtterancesSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.aggregated_utterances_summary.AggregatedUtterancesSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedUtterancesSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.aggregated_utterances_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.aggregated_utterances_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AggregatedUtterancesSummaryList:
    import aws_sdk_lex_models_v2.types.aggregated_utterances_summary

    out: AggregatedUtterancesSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.aggregated_utterances_summary.deserialize_json(
                item
            )
        )
    return out
