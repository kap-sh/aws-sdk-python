"""Generated from Smithy shape ``com.amazonaws.quicksight#ListDashboardVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string


class ListDashboardVersionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard that you're listing versions for.</p>"""
    dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the dashboard.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDashboardVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDashboardVersionsRequest:
    out: ListDashboardVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
