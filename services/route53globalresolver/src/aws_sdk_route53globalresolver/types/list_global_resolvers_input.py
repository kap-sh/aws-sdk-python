"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListGlobalResolversInput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListGlobalResolversInput(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of Route 53 Global Resolver instances to return in the response. Valid range is 1-100.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next page of results. This value is returned in the response if there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGlobalResolversInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGlobalResolversInput:
    out: ListGlobalResolversInput = {}  # type: ignore[typeddict-item]
    return out
