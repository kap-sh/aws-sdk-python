"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTopicRefreshScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_id
    import capo_quicksight.types.topic_refresh_schedule


class UpdateTopicRefreshScheduleRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic whose refresh schedule you want to update.</p>"""
    topic_id: "capo_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to modify. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    dataset_id: "capo_quicksight.types.string.String"
    """<p>The ID of the dataset.</p>"""
    refresh_schedule: (
        "capo_quicksight.types.topic_refresh_schedule.TopicRefreshSchedule"
    )
    """<p>The definition of a refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicRefreshScheduleRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.topic_refresh_schedule

    out["RefreshSchedule"] = (
        capo_quicksight.types.topic_refresh_schedule.serialize_json(
            value["refresh_schedule"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTopicRefreshScheduleRequest:
    out: UpdateTopicRefreshScheduleRequest = {}  # type: ignore[typeddict-item]
    if "RefreshSchedule" in data:
        import capo_quicksight.types.topic_refresh_schedule

        out["refresh_schedule"] = (
            capo_quicksight.types.topic_refresh_schedule.deserialize_json(
                data["RefreshSchedule"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTopicRefreshScheduleRequest.refresh_schedule required"
        )
    return out
