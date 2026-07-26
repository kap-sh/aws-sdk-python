"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionGroupByKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_session_group_by_key

AnalyticsSessionGroupByKeys: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_session_group_by_key.AnalyticsSessionGroupByKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionGroupByKeys) -> list:
    import capo_lex_models_v2.types.analytics_session_group_by_key

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_session_group_by_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionGroupByKeys:
    import capo_lex_models_v2.types.analytics_session_group_by_key

    out: AnalyticsSessionGroupByKeys = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_session_group_by_key.deserialize_json(
                item
            )
        )
    return out
