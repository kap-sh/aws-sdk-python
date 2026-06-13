"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ListFindingsMetricsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_codeguru_security.types.next_token


class ListFindingsMetricsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_codeguru_security.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the <code>nextToken</code> element is returned in the response. Use <code>nextToken</code> in a subsequent request to retrieve additional results. If not specified, returns 1000 results.</p>"""
    start_date: "datetime.datetime"
    """<p>The start date of the interval which you want to retrieve metrics from. Rounds to the nearest day.</p>"""
    end_date: "datetime.datetime"
    """<p>The end date of the interval which you want to retrieve metrics from. Round to the nearest day.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsMetricsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFindingsMetricsRequest:
    out: ListFindingsMetricsRequest = {}  # type: ignore[typeddict-item]
    return out
