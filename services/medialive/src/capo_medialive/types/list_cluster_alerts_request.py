"""Generated from Smithy shape ``com.amazonaws.medialive#ListClusterAlertsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.max_results


class ListClusterAlertsRequest(TypedDict, closed=True):
    cluster_id: "capo_medialive.types.__string.__string"
    """The unique ID of the cluster"""
    max_results: NotRequired["capo_medialive.types.max_results.MaxResults"]
    """The maximum number of items to return"""
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """The next pagination token"""
    state_filter: NotRequired["capo_medialive.types.__string.__string"]
    """Specifies the set of alerts to return based on their state. SET - Return only alerts with SET state. CLEARED - Return only alerts with CLEARED state. ALL - Return all alerts."""


# --- restJson1 ser/de ---
def serialize_json(value: ListClusterAlertsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClusterAlertsRequest:
    out: ListClusterAlertsRequest = {}  # type: ignore[typeddict-item]
    return out
