"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_session_result

AnalyticsSessionResults: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_session_result.AnalyticsSessionResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionResults) -> list:
    import capo_lex_models_v2.types.analytics_session_result

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_session_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionResults:
    import capo_lex_models_v2.types.analytics_session_result

    out: AnalyticsSessionResults = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_session_result.deserialize_json(item)
        )
    return out
