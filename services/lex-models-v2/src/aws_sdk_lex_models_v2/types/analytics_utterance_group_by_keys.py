"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceGroupByKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_key

AnalyticsUtteranceGroupByKeys: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_utterance_group_by_key.AnalyticsUtteranceGroupByKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceGroupByKeys) -> list:
    import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_key

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_group_by_key.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceGroupByKeys:
    import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_key

    out: AnalyticsUtteranceGroupByKeys = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_group_by_key.deserialize_json(
                item
            )
        )
    return out
