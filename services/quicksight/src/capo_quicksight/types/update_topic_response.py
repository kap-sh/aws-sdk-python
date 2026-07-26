"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTopicResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_id


class UpdateTopicResponse(TypedDict, closed=True):
    topic_id: NotRequired["capo_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic that you want to modify. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    refresh_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic refresh.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicResponse) -> dict:
    out: dict = {}
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "refresh_arn" in value:
        out["RefreshArn"] = value["refresh_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateTopicResponse:
    out: UpdateTopicResponse = {}  # type: ignore[typeddict-item]
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "RefreshArn" in data:
        out["refresh_arn"] = data["RefreshArn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
