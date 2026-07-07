"""Generated from Smithy shape ``com.amazonaws.securityhub#ListFindingAggregatorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token


class ListFindingAggregatorsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token returned with the previous set of results. Identifies the next set of results to return.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. This operation currently only returns a single result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingAggregatorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFindingAggregatorsRequest:
    out: ListFindingAggregatorsRequest = {}  # type: ignore[typeddict-item]
    return out
