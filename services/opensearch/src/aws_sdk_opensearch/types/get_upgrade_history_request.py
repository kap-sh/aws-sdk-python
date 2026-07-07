"""Generated from Smithy shape ``com.amazonaws.opensearch#GetUpgradeHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.max_results
    import aws_sdk_opensearch.types.next_token


class GetUpgradeHistoryRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of an existing domain.</p>"""
    max_results: "aws_sdk_opensearch.types.max_results.MaxResults"
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>GetUpgradeHistory</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>GetUpgradeHistory</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeHistoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUpgradeHistoryRequest:
    out: GetUpgradeHistoryRequest = {}  # type: ignore[typeddict-item]
    return out
