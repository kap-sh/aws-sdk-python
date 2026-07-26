"""Generated from Smithy shape ``com.amazonaws.amp#ListScrapersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.pagination_token
    import capo_amp.types.scraper_filters


class ListScrapersRequest(TypedDict, closed=True):
    filters: NotRequired["capo_amp.types.scraper_filters.ScraperFilters"]
    """<p>(Optional) A list of key-value pairs to filter the list of scrapers returned. Keys include <code>status</code>, <code>sourceArn</code>, <code>destinationArn</code>, and <code>alias</code>.</p> <p>Filters on the same key are <code>OR</code>'d together, and filters on different keys are <code>AND</code>'d together. For example, <code>status=ACTIVE&amp;status=CREATING&amp;alias=Test</code>, will return all scrapers that have the alias Test, and are either in status ACTIVE or CREATING.</p> <p>To find all active scrapers that are sending metrics to a specific Amazon Managed Service for Prometheus workspace, you would use the ARN of the workspace in a query:</p> <p> <code>status=ACTIVE&amp;destinationArn=arn:aws:aps:us-east-1:123456789012:workspace/ws-example1-1234-abcd-56ef-123456789012</code> </p> <p>If this is included, it filters the results to only the scrapers that match the filter.</p>"""
    next_token: NotRequired["capo_amp.types.pagination_token.PaginationToken"]
    """<p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["int"]
    """<p>Optional) The maximum number of scrapers to return in one <code>ListScrapers</code> operation. The range is 1-1000.</p> <p>If you omit this parameter, the default of 100 is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScrapersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListScrapersRequest:
    out: ListScrapersRequest = {}  # type: ignore[typeddict-item]
    return out
