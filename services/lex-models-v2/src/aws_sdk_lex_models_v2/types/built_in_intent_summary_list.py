"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInIntentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.built_in_intent_summary

BuiltInIntentSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.built_in_intent_summary.BuiltInIntentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BuiltInIntentSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.built_in_intent_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.built_in_intent_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BuiltInIntentSummaryList:
    import aws_sdk_lex_models_v2.types.built_in_intent_summary

    out: BuiltInIntentSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.built_in_intent_summary.deserialize_json(item)
        )
    return out
