"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceGroupByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_specification

AnalyticsUtteranceGroupByList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_utterance_group_by_specification.AnalyticsUtteranceGroupBySpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceGroupByList) -> list:
    import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_group_by_specification.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceGroupByList:
    import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_specification

    out: AnalyticsUtteranceGroupByList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_group_by_specification.deserialize_json(
                item
            )
        )
    return out
