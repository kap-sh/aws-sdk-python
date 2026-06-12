"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListEventIntegrationAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.max_results
    import aws_sdk_appintegrations.types.name
    import aws_sdk_appintegrations.types.next_token


class ListEventIntegrationAssociationsRequest(TypedDict):
    event_integration_name: "aws_sdk_appintegrations.types.name.Name"
    """<p>The name of the event integration. </p>"""
    next_token: NotRequired["aws_sdk_appintegrations.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_appintegrations.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventIntegrationAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventIntegrationAssociationsRequest:
    out: ListEventIntegrationAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
