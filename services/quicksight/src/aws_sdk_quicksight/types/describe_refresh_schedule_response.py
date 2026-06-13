"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeRefreshScheduleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.refresh_schedule
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeRefreshScheduleResponse(TypedDict):
    refresh_schedule: NotRequired[
        "aws_sdk_quicksight.types.refresh_schedule.RefreshSchedule"
    ]
    """<p>The refresh schedule.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRefreshScheduleResponse) -> dict:
    out: dict = {}
    if "refresh_schedule" in value:
        import aws_sdk_quicksight.types.refresh_schedule

        out["RefreshSchedule"] = (
            aws_sdk_quicksight.types.refresh_schedule.serialize_json(
                value["refresh_schedule"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DescribeRefreshScheduleResponse:
    out: DescribeRefreshScheduleResponse = {}  # type: ignore[typeddict-item]
    if "RefreshSchedule" in data:
        import aws_sdk_quicksight.types.refresh_schedule

        out["refresh_schedule"] = (
            aws_sdk_quicksight.types.refresh_schedule.deserialize_json(
                data["RefreshSchedule"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
