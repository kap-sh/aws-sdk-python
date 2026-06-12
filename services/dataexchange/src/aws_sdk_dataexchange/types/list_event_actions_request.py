"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListEventActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.max_results


class ListEventActionsRequest(TypedDict):
    event_source_id: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The unique identifier for the event source.</p>"""
    max_results: "aws_sdk_dataexchange.types.max_results.MaxResults"
    """<p>The maximum number of results returned by a single call.</p>"""
    next_token: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventActionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventActionsRequest:
    out: ListEventActionsRequest = {}  # type: ignore[typeddict-item]
    return out
