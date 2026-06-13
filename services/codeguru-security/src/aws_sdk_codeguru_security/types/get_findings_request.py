"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#GetFindingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.next_token
    import aws_sdk_codeguru_security.types.scan_name
    import aws_sdk_codeguru_security.types.status


class GetFindingsRequest(TypedDict):
    scan_name: "aws_sdk_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan you want to retrieve findings from.</p>"""
    next_token: NotRequired["aws_sdk_codeguru_security.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the <code>nextToken</code> element is returned in the response. Use <code>nextToken</code> in a subsequent request to retrieve additional results. If not specified, returns 1000 results.</p>"""
    status: NotRequired["aws_sdk_codeguru_security.types.status.Status"]
    """<p>The status of the findings you want to get. Pass either <code>Open</code>, <code>Closed</code>, or <code>All</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFindingsRequest:
    out: GetFindingsRequest = {}  # type: ignore[typeddict-item]
    return out
