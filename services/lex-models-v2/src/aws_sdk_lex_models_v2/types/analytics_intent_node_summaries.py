"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentNodeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_node_summary

AnalyticsIntentNodeSummaries: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_intent_node_summary.AnalyticsIntentNodeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentNodeSummaries) -> list:
    import aws_sdk_lex_models_v2.types.analytics_intent_node_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_node_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentNodeSummaries:
    import aws_sdk_lex_models_v2.types.analytics_intent_node_summary

    out: AnalyticsIntentNodeSummaries = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_node_summary.deserialize_json(
                item
            )
        )
    return out
