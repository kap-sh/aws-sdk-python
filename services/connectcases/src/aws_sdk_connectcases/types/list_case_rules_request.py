"""Generated from Smithy shape ``com.amazonaws.connectcases#ListCaseRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.max_results
    import aws_sdk_connectcases.types.next_token


class ListCaseRulesRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>Unique identifier of a Cases domain.</p>"""
    max_results: NotRequired["aws_sdk_connectcases.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCaseRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCaseRulesRequest:
    out: ListCaseRulesRequest = {}  # type: ignore[typeddict-item]
    return out
