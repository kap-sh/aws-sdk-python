"""Generated from Smithy shape ``com.amazonaws.appconfig#ListDeploymentStrategiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.max_results
    import aws_sdk_appconfig.types.next_token


class ListDeploymentStrategiesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_appconfig.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentStrategiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDeploymentStrategiesRequest:
    out: ListDeploymentStrategiesRequest = {}  # type: ignore[typeddict-item]
    return out
