"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRefreshDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.topic_refresh_status


class TopicRefreshDetails(TypedDict, closed=True):
    refresh_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic refresh.</p>"""
    refresh_id: NotRequired["aws_sdk_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the refresh, which occurs as a result of topic creation or topic update.</p>"""
    refresh_status: NotRequired[
        "aws_sdk_quicksight.types.topic_refresh_status.TopicRefreshStatus"
    ]
    """<p>The status of the refresh job that indicates whether the job is still running, completed successfully, or failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRefreshDetails) -> dict:
    out: dict = {}
    if "refresh_arn" in value:
        out["RefreshArn"] = value["refresh_arn"]
    if "refresh_id" in value:
        out["RefreshId"] = value["refresh_id"]
    if "refresh_status" in value:
        import aws_sdk_quicksight.types.topic_refresh_status

        out["RefreshStatus"] = (
            aws_sdk_quicksight.types.topic_refresh_status.serialize_json(
                value["refresh_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicRefreshDetails:
    out: TopicRefreshDetails = {}  # type: ignore[typeddict-item]
    if "RefreshArn" in data:
        out["refresh_arn"] = data["RefreshArn"]
    if "RefreshId" in data:
        out["refresh_id"] = data["RefreshId"]
    if "RefreshStatus" in data:
        import aws_sdk_quicksight.types.topic_refresh_status

        out["refresh_status"] = (
            aws_sdk_quicksight.types.topic_refresh_status.deserialize_json(
                data["RefreshStatus"]
            )
        )
    return out
