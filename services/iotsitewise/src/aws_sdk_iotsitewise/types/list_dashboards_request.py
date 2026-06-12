"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDashboardsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.max_results
    import aws_sdk_iotsitewise.types.next_token


class ListDashboardsRequest(TypedDict):
    project_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the project.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["aws_sdk_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDashboardsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDashboardsRequest:
    out: ListDashboardsRequest = {}  # type: ignore[typeddict-item]
    return out
