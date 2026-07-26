"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListInterfaceRelationshipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListInterfaceRelationshipsRequest(TypedDict, closed=True):
    interface_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request. Default: 50</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInterfaceRelationshipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInterfaceRelationshipsRequest:
    out: ListInterfaceRelationshipsRequest = {}  # type: ignore[typeddict-item]
    return out
