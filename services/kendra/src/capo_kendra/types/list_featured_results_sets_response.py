"""Generated from Smithy shape ``com.amazonaws.kendra#ListFeaturedResultsSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.featured_results_set_summary_items
    import capo_kendra.types.next_token


class ListFeaturedResultsSetsResponse(TypedDict, closed=True):
    featured_results_set_summary_items: NotRequired[
        "capo_kendra.types.featured_results_set_summary_items.FeaturedResultsSetSummaryItems"
    ]
    """<p>An array of summary information for one or more featured results sets.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns a pagination token in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFeaturedResultsSetsResponse) -> dict:
    out: dict = {}
    if "featured_results_set_summary_items" in value:
        import capo_kendra.types.featured_results_set_summary_items

        out["FeaturedResultsSetSummaryItems"] = (
            capo_kendra.types.featured_results_set_summary_items.serialize_aws_json_1_1(
                value["featured_results_set_summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFeaturedResultsSetsResponse:
    out: ListFeaturedResultsSetsResponse = {}  # type: ignore[typeddict-item]
    if "FeaturedResultsSetSummaryItems" in data:
        import capo_kendra.types.featured_results_set_summary_items

        out["featured_results_set_summary_items"] = (
            capo_kendra.types.featured_results_set_summary_items.deserialize_aws_json_1_1(
                data["FeaturedResultsSetSummaryItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
