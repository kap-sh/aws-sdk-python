"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#ListEmailContactsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListEmailContactsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["str"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEmailContactsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEmailContactsRequest:
    out: ListEmailContactsRequest = {}  # type: ignore[typeddict-item]
    return out
