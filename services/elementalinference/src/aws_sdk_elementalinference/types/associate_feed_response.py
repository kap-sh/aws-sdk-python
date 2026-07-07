"""Generated from Smithy shape ``com.amazonaws.elementalinference#AssociateFeedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.feed_arn
    import aws_sdk_elementalinference.types.feed_id


class AssociateFeedResponse(TypedDict, closed=True):
    arn: "aws_sdk_elementalinference.types.feed_arn.FeedArn"
    """<p>The ARN of the feed.</p>"""
    id: "aws_sdk_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateFeedResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> AssociateFeedResponse:
    out: AssociateFeedResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AssociateFeedResponse.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssociateFeedResponse.id required")
    return out
