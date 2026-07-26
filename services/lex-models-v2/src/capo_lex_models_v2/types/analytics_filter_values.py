"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_filter_value

AnalyticsFilterValues: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_filter_value.AnalyticsFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> AnalyticsFilterValues:
    return list(data)
