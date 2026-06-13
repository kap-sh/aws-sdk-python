"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCodeSecurityIntegrationsRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListCodeSecurityIntegrationsRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeSecurityIntegrationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCodeSecurityIntegrationsRequest:
    out: ListCodeSecurityIntegrationsRequest = {}  # type: ignore[typeddict-item]
    return out
