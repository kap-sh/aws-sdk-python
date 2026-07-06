"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteFeedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.feed_arn
    import aws_sdk_elementalinference.types.feed_id
    import aws_sdk_elementalinference.types.feed_status


class DeleteFeedResponse(TypedDict, closed=True):
    arn: "aws_sdk_elementalinference.types.feed_arn.FeedArn"
    """<p>The ARN of the deleted feed.</p>"""
    id: "aws_sdk_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the deleted feed.</p>"""
    status: "aws_sdk_elementalinference.types.feed_status.FeedStatus"
    """<p>The current status of the feed. When deletion of the feed has succeeded, the status will be DELETED. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFeedResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import aws_sdk_elementalinference.types.feed_status

    out["status"] = aws_sdk_elementalinference.types.feed_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteFeedResponse:
    out: DeleteFeedResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteFeedResponse.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteFeedResponse.id required")
    if "status" in data:
        import aws_sdk_elementalinference.types.feed_status

        out["status"] = aws_sdk_elementalinference.types.feed_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteFeedResponse.status required")
    return out
