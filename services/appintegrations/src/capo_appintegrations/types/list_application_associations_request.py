"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListApplicationAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.arn_or_uuid
    import capo_appintegrations.types.max_results
    import capo_appintegrations.types.next_token


class ListApplicationAssociationsRequest(TypedDict, closed=True):
    application_id: "capo_appintegrations.types.arn_or_uuid.ArnOrUUID"
    """<p>A unique identifier for the Application.</p>"""
    next_token: NotRequired["capo_appintegrations.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_appintegrations.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationAssociationsRequest:
    out: ListApplicationAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
