"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_session_result

AnalyticsSessionResults: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_session_result.AnalyticsSessionResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionResults) -> list:
    import aws_sdk_lex_models_v2.types.analytics_session_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionResults:
    import aws_sdk_lex_models_v2.types.analytics_session_result

    out: AnalyticsSessionResults = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_result.deserialize_json(item)
        )
    return out
