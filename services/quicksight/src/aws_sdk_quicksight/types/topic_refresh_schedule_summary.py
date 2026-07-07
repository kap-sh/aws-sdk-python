"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRefreshScheduleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.topic_refresh_schedule


class TopicRefreshScheduleSummary(TypedDict, closed=True):
    dataset_id: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The ID of the dataset.</p>"""
    dataset_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_name: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The name of the dataset.</p>"""
    refresh_schedule: NotRequired[
        "aws_sdk_quicksight.types.topic_refresh_schedule.TopicRefreshSchedule"
    ]
    """<p>The definition of a refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRefreshScheduleSummary) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["DatasetId"] = value["dataset_id"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "refresh_schedule" in value:
        import aws_sdk_quicksight.types.topic_refresh_schedule

        out["RefreshSchedule"] = (
            aws_sdk_quicksight.types.topic_refresh_schedule.serialize_json(
                value["refresh_schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicRefreshScheduleSummary:
    out: TopicRefreshScheduleSummary = {}  # type: ignore[typeddict-item]
    if "DatasetId" in data:
        out["dataset_id"] = data["DatasetId"]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "RefreshSchedule" in data:
        import aws_sdk_quicksight.types.topic_refresh_schedule

        out["refresh_schedule"] = (
            aws_sdk_quicksight.types.topic_refresh_schedule.deserialize_json(
                data["RefreshSchedule"]
            )
        )
    return out
