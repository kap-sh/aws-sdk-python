"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RecommendedIntentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.recommended_intent_summary

RecommendedIntentSummaryList: TypeAlias = list[
    "capo_lex_models_v2.types.recommended_intent_summary.RecommendedIntentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedIntentSummaryList) -> list:
    import capo_lex_models_v2.types.recommended_intent_summary

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.recommended_intent_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommendedIntentSummaryList:
    import capo_lex_models_v2.types.recommended_intent_summary

    out: RecommendedIntentSummaryList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.recommended_intent_summary.deserialize_json(item)
        )
    return out
