"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.aggregated_utterances_filter

AggregatedUtterancesFilters: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.aggregated_utterances_filter.AggregatedUtterancesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedUtterancesFilters) -> list:
    import aws_sdk_lex_models_v2.types.aggregated_utterances_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.aggregated_utterances_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AggregatedUtterancesFilters:
    import aws_sdk_lex_models_v2.types.aggregated_utterances_filter

    out: AggregatedUtterancesFilters = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.aggregated_utterances_filter.deserialize_json(
                item
            )
        )
    return out
