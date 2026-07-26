"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_filter

AnalyticsIntentFilters: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_filter.AnalyticsIntentFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentFilters) -> list:
    import capo_lex_models_v2.types.analytics_intent_filter

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentFilters:
    import capo_lex_models_v2.types.analytics_intent_filter

    out: AnalyticsIntentFilters = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_filter.deserialize_json(item)
        )
    return out
