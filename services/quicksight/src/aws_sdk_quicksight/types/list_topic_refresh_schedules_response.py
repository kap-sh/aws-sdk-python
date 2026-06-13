"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTopicRefreshSchedulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.topic_id
    import aws_sdk_quicksight.types.topic_refresh_schedule_summaries


class ListTopicRefreshSchedulesResponse(TypedDict):
    topic_id: NotRequired["aws_sdk_quicksight.types.topic_id.TopicId"]
    """<p>The ID for the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    refresh_schedules: NotRequired[
        "aws_sdk_quicksight.types.topic_refresh_schedule_summaries.TopicRefreshScheduleSummaries"
    ]
    """<p>The list of topic refresh schedules.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicRefreshSchedulesResponse) -> dict:
    out: dict = {}
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "refresh_schedules" in value:
        import aws_sdk_quicksight.types.topic_refresh_schedule_summaries

        out["RefreshSchedules"] = (
            aws_sdk_quicksight.types.topic_refresh_schedule_summaries.serialize_json(
                value["refresh_schedules"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListTopicRefreshSchedulesResponse:
    out: ListTopicRefreshSchedulesResponse = {}  # type: ignore[typeddict-item]
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    if "RefreshSchedules" in data:
        import aws_sdk_quicksight.types.topic_refresh_schedule_summaries

        out["refresh_schedules"] = (
            aws_sdk_quicksight.types.topic_refresh_schedule_summaries.deserialize_json(
                data["RefreshSchedules"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
