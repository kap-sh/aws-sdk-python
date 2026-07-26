"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTopicRefreshScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_id


class UpdateTopicRefreshScheduleResponse(TypedDict, closed=True):
    topic_id: NotRequired["capo_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic that you want to modify. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    dataset_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicRefreshScheduleResponse) -> dict:
    out: dict = {}
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateTopicRefreshScheduleResponse:
    out: UpdateTopicRefreshScheduleResponse = {}  # type: ignore[typeddict-item]
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
