"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_result

AnalyticsIntentResults: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_intent_result.AnalyticsIntentResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentResults) -> list:
    import aws_sdk_lex_models_v2.types.analytics_intent_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentResults:
    import aws_sdk_lex_models_v2.types.analytics_intent_result

    out: AnalyticsIntentResults = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_result.deserialize_json(item)
        )
    return out
