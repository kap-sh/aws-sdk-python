"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTopicResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.topic_id


class CreateTopicResponse(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_id: NotRequired["aws_sdk_quicksight.types.topic_id.TopicId"]
    """<p>The ID for the topic that you want to create. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    refresh_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic refresh.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "refresh_arn" in value:
        out["RefreshArn"] = value["refresh_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateTopicResponse:
    out: CreateTopicResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "RefreshArn" in data:
        out["refresh_arn"] = data["RefreshArn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
