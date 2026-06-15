"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListDataIntegrationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.max_results
    import aws_sdk_appintegrations.types.next_token


class ListDataIntegrationsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_appintegrations.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_appintegrations.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataIntegrationsRequest:
    out: ListDataIntegrationsRequest = {}  # type: ignore[typeddict-item]
    return out
