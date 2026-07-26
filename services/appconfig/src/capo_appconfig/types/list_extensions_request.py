"""Generated from Smithy shape ``com.amazonaws.appconfig#ListExtensionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.max_results
    import capo_appconfig.types.next_token
    import capo_appconfig.types.query_name


class ListExtensionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_appconfig.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""
    name: NotRequired["capo_appconfig.types.query_name.QueryName"]
    """<p>The extension name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExtensionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExtensionsRequest:
    out: ListExtensionsRequest = {}  # type: ignore[typeddict-item]
    return out
