"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListGatewaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.max_results
    import aws_sdk_iotsitewise.types.next_token


class ListGatewaysRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["aws_sdk_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewaysRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGatewaysRequest:
    out: ListGatewaysRequest = {}  # type: ignore[typeddict-item]
    return out
