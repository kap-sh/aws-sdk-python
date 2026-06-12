"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_session_filter

AnalyticsSessionFilters: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_session_filter.AnalyticsSessionFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionFilters) -> list:
    import aws_sdk_lex_models_v2.types.analytics_session_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionFilters:
    import aws_sdk_lex_models_v2.types.analytics_session_filter

    out: AnalyticsSessionFilters = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_filter.deserialize_json(item)
        )
    return out
