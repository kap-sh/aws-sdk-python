"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsSetSummaryItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.featured_results_set_summary

FeaturedResultsSetSummaryItems: TypeAlias = list[
    "capo_kendra.types.featured_results_set_summary.FeaturedResultsSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsSetSummaryItems) -> list:
    import capo_kendra.types.featured_results_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.featured_results_set_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FeaturedResultsSetSummaryItems:
    import capo_kendra.types.featured_results_set_summary

    out: FeaturedResultsSetSummaryItems = []
    for item in data:
        out.append(
            capo_kendra.types.featured_results_set_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
