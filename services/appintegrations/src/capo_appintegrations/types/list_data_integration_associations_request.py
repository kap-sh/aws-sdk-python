"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListDataIntegrationAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.identifier
    import capo_appintegrations.types.max_results
    import capo_appintegrations.types.next_token


class ListDataIntegrationAssociationsRequest(TypedDict, closed=True):
    data_integration_identifier: "capo_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier for the DataIntegration.</p>"""
    next_token: NotRequired["capo_appintegrations.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_appintegrations.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataIntegrationAssociationsRequest:
    out: ListDataIntegrationAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
