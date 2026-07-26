"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_stage_result

AnalyticsIntentStageResults: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_stage_result.AnalyticsIntentStageResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageResults) -> list:
    import capo_lex_models_v2.types.analytics_intent_stage_result

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentStageResults:
    import capo_lex_models_v2.types.analytics_intent_stage_result

    out: AnalyticsIntentStageResults = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_result.deserialize_json(
                item
            )
        )
    return out
