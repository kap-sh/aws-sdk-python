"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsPathFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_path_filter

AnalyticsPathFilters: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_path_filter.AnalyticsPathFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsPathFilters) -> list:
    import capo_lex_models_v2.types.analytics_path_filter

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.analytics_path_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalyticsPathFilters:
    import capo_lex_models_v2.types.analytics_path_filter

    out: AnalyticsPathFilters = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_path_filter.deserialize_json(item)
        )
    return out
