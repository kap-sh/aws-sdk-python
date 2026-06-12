"""Generated from Smithy shape ``com.amazonaws.kendra#ListFeaturedResultsSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.featured_results_set_summary_items
    import aws_sdk_kendra.types.next_token


class ListFeaturedResultsSetsResponse(TypedDict):
    featured_results_set_summary_items: NotRequired[
        "aws_sdk_kendra.types.featured_results_set_summary_items.FeaturedResultsSetSummaryItems"
    ]
    """<p>An array of summary information for one or more featured results sets.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns a pagination token in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFeaturedResultsSetsResponse) -> dict:
    out: dict = {}
    if "featured_results_set_summary_items" in value:
        import aws_sdk_kendra.types.featured_results_set_summary_items

        out["FeaturedResultsSetSummaryItems"] = (
            aws_sdk_kendra.types.featured_results_set_summary_items.serialize_aws_json_1_1(
                value["featured_results_set_summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFeaturedResultsSetsResponse:
    out: ListFeaturedResultsSetsResponse = {}  # type: ignore[typeddict-item]
    if "FeaturedResultsSetSummaryItems" in data:
        import aws_sdk_kendra.types.featured_results_set_summary_items

        out["featured_results_set_summary_items"] = (
            aws_sdk_kendra.types.featured_results_set_summary_items.deserialize_aws_json_1_1(
                data["FeaturedResultsSetSummaryItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
