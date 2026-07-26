"""Generated from Smithy shape ``com.amazonaws.medialive#ListNodesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.max_results


class ListNodesRequest(TypedDict, closed=True):
    cluster_id: "capo_medialive.types.__string.__string"
    """The ID of the cluster"""
    max_results: NotRequired["capo_medialive.types.max_results.MaxResults"]
    """The maximum number of items to return."""
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """The token to retrieve the next page of results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNodesRequest:
    out: ListNodesRequest = {}  # type: ignore[typeddict-item]
    return out
