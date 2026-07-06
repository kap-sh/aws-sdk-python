"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCodeSecurityScanConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.next_token


class ListCodeSecurityScanConfigurationsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeSecurityScanConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCodeSecurityScanConfigurationsRequest:
    out: ListCodeSecurityScanConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
