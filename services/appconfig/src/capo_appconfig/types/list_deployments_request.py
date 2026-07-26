"""Generated from Smithy shape ``com.amazonaws.appconfig#ListDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.id
    import capo_appconfig.types.max_results
    import capo_appconfig.types.next_token


class ListDeploymentsRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    environment_id: "capo_appconfig.types.id.Id"
    """<p>The environment ID.</p>"""
    max_results: NotRequired["capo_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items that may be returned for this call. If there are items that have not yet been returned, the response will include a non-null <code>NextToken</code> that you can provide in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_appconfig.types.next_token.NextToken"]
    """<p>The token returned by a prior call to this operation indicating the next set of results to be returned. If not specified, the operation will return the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDeploymentsRequest:
    out: ListDeploymentsRequest = {}  # type: ignore[typeddict-item]
    return out
