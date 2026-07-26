"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id


class GetFeedRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed to query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFeedRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFeedRequest:
    out: GetFeedRequest = {}  # type: ignore[typeddict-item]
    return out
