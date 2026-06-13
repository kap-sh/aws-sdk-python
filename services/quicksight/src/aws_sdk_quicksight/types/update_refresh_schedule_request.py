"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateRefreshScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.refresh_schedule
    import aws_sdk_quicksight.types.resource_id


class UpdateRefreshScheduleRequest(TypedDict):
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dataset.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    schedule: "aws_sdk_quicksight.types.refresh_schedule.RefreshSchedule"
    """<p>The refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRefreshScheduleRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.refresh_schedule

    out["Schedule"] = aws_sdk_quicksight.types.refresh_schedule.serialize_json(
        value["schedule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRefreshScheduleRequest:
    out: UpdateRefreshScheduleRequest = {}  # type: ignore[typeddict-item]
    if "Schedule" in data:
        import aws_sdk_quicksight.types.refresh_schedule

        out["schedule"] = aws_sdk_quicksight.types.refresh_schedule.deserialize_json(
            data["Schedule"]
        )
    else:
        raise DeserializationError("UpdateRefreshScheduleRequest.schedule required")
    return out
