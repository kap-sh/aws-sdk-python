"""Generated from Smithy shape ``com.amazonaws.medialive#ListAlertsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListAlertsRequest(TypedDict, closed=True):
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """The unique ID of the channel"""
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    """The maximum number of items to return"""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The next pagination token"""
    state_filter: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specifies the set of alerts to return based on their state. SET - Return only alerts with SET state. CLEARED - Return only alerts with CLEARED state. ALL - Return all alerts."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAlertsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAlertsRequest:
    out: ListAlertsRequest = {}  # type: ignore[typeddict-item]
    return out
