"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#IntentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.intent_summary

IntentSummaryList: TypeAlias = list[
    "aws_sdk_lex_runtime_service.types.intent_summary.IntentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentSummaryList) -> list:
    import aws_sdk_lex_runtime_service.types.intent_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_runtime_service.types.intent_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntentSummaryList:
    import aws_sdk_lex_runtime_service.types.intent_summary

    out: IntentSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_runtime_service.types.intent_summary.deserialize_json(item)
        )
    return out
