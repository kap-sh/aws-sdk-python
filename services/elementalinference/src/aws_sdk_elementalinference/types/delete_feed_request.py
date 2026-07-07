"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.feed_id


class DeleteFeedRequest(TypedDict, closed=True):
    id: "aws_sdk_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFeedRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFeedRequest:
    out: DeleteFeedRequest = {}  # type: ignore[typeddict-item]
    return out
