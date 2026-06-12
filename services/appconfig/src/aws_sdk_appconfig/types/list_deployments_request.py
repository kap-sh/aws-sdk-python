"""Generated from Smithy shape ``com.amazonaws.appconfig#ListDeploymentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.max_results
    import aws_sdk_appconfig.types.next_token


class ListDeploymentsRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    environment_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The environment ID.</p>"""
    max_results: NotRequired["aws_sdk_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items that may be returned for this call. If there are items that have not yet been returned, the response will include a non-null <code>NextToken</code> that you can provide in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_appconfig.types.next_token.NextToken"]
    """<p>The token returned by a prior call to this operation indicating the next set of results to be returned. If not specified, the operation will return the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDeploymentsRequest:
    out: ListDeploymentsRequest = {}  # type: ignore[typeddict-item]
    return out
