"""Generated from Smithy shape ``com.amazonaws.kendra#QuerySuggestionsBlockListSummaryItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.query_suggestions_block_list_summary

QuerySuggestionsBlockListSummaryItems: TypeAlias = list[
    "capo_kendra.types.query_suggestions_block_list_summary.QuerySuggestionsBlockListSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuerySuggestionsBlockListSummaryItems) -> list:
    import capo_kendra.types.query_suggestions_block_list_summary

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.query_suggestions_block_list_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QuerySuggestionsBlockListSummaryItems:
    import capo_kendra.types.query_suggestions_block_list_summary

    out: QuerySuggestionsBlockListSummaryItems = []
    for item in data:
        out.append(
            capo_kendra.types.query_suggestions_block_list_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
