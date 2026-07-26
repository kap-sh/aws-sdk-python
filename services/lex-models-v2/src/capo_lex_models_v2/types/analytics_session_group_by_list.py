"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionGroupByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_session_group_by_specification

AnalyticsSessionGroupByList: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_session_group_by_specification.AnalyticsSessionGroupBySpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionGroupByList) -> list:
    import capo_lex_models_v2.types.analytics_session_group_by_specification

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_session_group_by_specification.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionGroupByList:
    import capo_lex_models_v2.types.analytics_session_group_by_specification

    out: AnalyticsSessionGroupByList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_session_group_by_specification.deserialize_json(
                item
            )
        )
    return out
